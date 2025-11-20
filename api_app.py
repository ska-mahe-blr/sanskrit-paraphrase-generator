from flask import Flask, request, jsonify
import re
import io
import contextlib
import html
from my_packages.process_paraphrase import paraphrase_generator

app = Flask(__name__)

@app.route('/api/paraphrase', methods=['POST'])
def api_paraphrase():
    """
    API endpoint for paraphrasing tagged input.
    Input: JSON {"input_text": "<tagged-input>"}
    Output: JSON {"output": ..., "output_history": ...} or {"outputs": [...], ...} or {"error": ..., ...}
    """
    data = request.get_json()
    input_text = data.get('input_text', '').strip()
    output_history = [f"Original Input: {html.escape(input_text)}"]
    current_input = input_text
    step = 0
    while True:
        match = re.search(r'<([^<>-]+)-([^<>]+)>([^-<>]*)', current_input)
        if not match:
            incomplete_match = re.search(r'<([^<>-]+)-([^<>]+)>', current_input)
            if incomplete_match:
                return jsonify({
                    'error': f'Tag is missing in input: {incomplete_match.group(0)}',
                    'output_history': output_history
                })
            return jsonify({
                'output': current_input,
                'output_history': output_history
            })
        x_raw = match.group(1)
        y_raw = match.group(2)
        tag = match.group(3)
        if not tag:
            return jsonify({
                'error': f'Tag is missing in input: {match.group(0)}',
                'output_history': output_history
            })
        if tag in ['T1', 'T2', 'T3', 'T4', 'T5',
                   'T6', 'T7', 'Tn','Tm',
                   'K1', 'K2', 'K3', 'K4', 'K5', "K6", 'K7', 
                   'Bs3', 'Bs5', 'Bs7', 'Bsmn', 'BvS',
                   'Di', 'Ds', 'd']:
            pass
        elif tag in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 
                     'Tds', 'Tdt', 'Tdu', 'Tg', 'Tk', 'Tp',
                     'Tb', 'U', 'Km', 'Bs2', 'Bs4', 'Bs6', 
                     'Bsd', 'Bsp', 'Bsg', 'Bvp', 'Bss',
                     'Bsu', 'Bv', 'Bvs', 'BvU', 'Bb', 'E', 'S']:
            return jsonify({
                'error': f'Unsupported tag: {tag} in input: {match.group(0)}',
                'output_history': output_history
            })
        else:
            return jsonify({
                'error': f'Invalid tag: {tag} in input: {match.group(0)}',
                'output_history': output_history
            })
        x_parts = x_raw.split('_')
        y_parts = y_raw.split('_')
        replacement = '_'.join(x_parts + y_parts)
        prev_x = x_parts[:-1]
        prev_y = y_parts[:-1]
        x = x_parts[-1]
        y = y_parts[-1]
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            paraphrase_generator(x, y, tag)
        output_lines = [line for line in buf.getvalue().strip().split('\n') if line.strip()]
        output_lines = list(set(output_lines))
        new_output_lines = []
        for line in output_lines:
            words = line.split()
            if not words:
                continue
            for i, w in enumerate(words):
                if w.lower().startswith(x[:3].lower()) and prev_x:
                    words[i] = "_".join(prev_x + [w])
                if w.lower().startswith(y[:3].lower()) and prev_y:
                    words[i] = "_".join(prev_y + [w])
            new_output_lines.append(" ".join(words))
        output_lines = new_output_lines
        if len(output_lines) > 1:
            output_history.append(
                f"Step {step+1}: Processing: {match.group(0)} Multiple outputs found."
            )
            return jsonify({
                'outputs': output_lines,
                'output_history': output_history,
                'step': step + 1,
                'input_text': current_input
            })
        elif len(output_lines) == 1:
            output_history.append(
                f"Step {step+1}: Processing: {match.group(0)} Generated output: {output_lines[0]}"
            )
            replaced = (current_input[:match.start()] + replacement + current_input[match.end():]).replace('  ', ' ')
            current_input = replaced.strip()
            step += 1
            continue
        else:
            output_history.append(f'No output generated for step {step + 1} in line: {current_input}')
            return jsonify({
                'error': 'No output generated',
                'output_history': output_history
            })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
