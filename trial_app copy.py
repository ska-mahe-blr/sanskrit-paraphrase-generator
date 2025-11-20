from flask import Flask, render_template, request, Response, redirect, url_for, session
import re
import io
import contextlib
from my_packages.process_paraphrase import paraphrase_generator
import html
from flask import jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        session['input_text'] = input_text
        session['step'] = 0
        session['current_input'] = input_text.strip()
        session['output_history'] = [f"Original Input: {html.escape(input_text.strip())}"]
        return redirect(url_for('process_step'))
    return render_template('index.html')

@app.route('/process_step', methods=['GET', 'POST'])
def process_step():
    if request.method == 'POST' and 'input_text' in request.form and request.path == '/process_step':
        input_text = request.form['input_text'].strip()
        session['input_text'] = input_text
        session['current_input'] = input_text
        session['step'] = 0
        session['output_history'] = [f"Original Input: {html.escape(input_text)}"]
        session['x_chain'] = []
        session['y_chain'] = []

    while True:
        current_input = session.get('current_input', '')
        step = session.get('step', 0)
        output_history = session.get('output_history', [])

        match = re.search(r'<([^<>-]+)-([^<>]+)>([^-<>]*)', current_input)
        # If no match, check for missing tag pattern and show error
        if not match:
            incomplete_match = re.search(r'<([^<>-]+)-([^<>]+)>', current_input)
            if incomplete_match:
                error_html = f'<span style="color:red;">Error: Tag is missing in input: {html.escape(incomplete_match.group(0))}</span><br>'
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return error_html
                return render_template('index.html', output_html=error_html)
            html_out = "<br>".join(output_history)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return html_out
            return render_template('index.html', output_html=html_out)

        x_raw = match.group(1)
        y_raw = match.group(2)
        tag = match.group(3)

        # If tag is missing (empty string), show error and stop loop
        if not tag:
            error_html = f'<span style="color:red;">Error: Tag is missing in input: {html.escape(match.group(0))}</span><br>'
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return error_html
            return render_template('index.html', output_html=error_html)
        
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
            error_html = f'<span style="color:red;">Error: Unsupported tag. We are still working on it. "{html.escape(tag)}" in input: {html.escape(match.group(0))}</span><br>'
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return error_html
            return render_template('index.html', output_html=error_html)
        else:
            error_html = f'<span style="color:red;">Error: Invalid tag "{html.escape(tag)}" in input: {html.escape(match.group(0))}</span><br>'
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return error_html
            return render_template('index.html', output_html=error_html)

        # For replacement, join x and y components with underscores
        x_parts = x_raw.split('_')
        print("X parts:", x_parts)
        y_parts = y_raw.split('_')
        print("Y parts:", y_parts)
        replacement = '_'.join(x_parts + y_parts)

        prev_x = x_parts[:-1]
        print("Prev X:", prev_x)
        prev_y = y_parts[:-1]
        print("Prev Y:", prev_y)

        # Paraphrase using last word of x and y
        x = x_parts[-1]
        print("x:", x)
        y = y_parts[-1]
        print("y:", y)
        print("Tag:", tag)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            paraphrase_generator(x, y, tag)
        output_lines = [line for line in buf.getvalue().strip().split('\n') if line.strip()]
        output_lines = list(set(output_lines))  # Remove duplicates

        new_output_lines = []
        for line in output_lines:
            words = line.split()
            if not words:
                continue

            for i, w in enumerate(words):
                # Check against x
                if w.lower().startswith(x[:3].lower()) and prev_x:
                    words[i] = "_".join(prev_x + [w])

                # Check against y
                if w.lower().startswith(y[:3].lower()) and prev_y:
                    words[i] = "_".join(prev_y + [w])

            new_output_lines.append(" ".join(words))

        output_lines = new_output_lines

        if len(output_lines) > 1:
            output_history.append(
                f"Step {step+1}:<br>Processing: {html.escape(match.group(0))}<br>Multiple outputs found, please choose one below."
            )
            session['output_history'] = output_history
            html_out = render_template(
                'choose_output.html',
                outputs=output_lines,
                step=step,
                input_text=current_input,
                output_history=output_history
            )
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return html_out
            return render_template('index.html', output_html=html_out)
        elif len(output_lines) == 1:
            output_history.append(
                f"Step {step+1}:<br>Processing: {html.escape(match.group(0))}<br>Generated output: {html.escape(output_lines[0])}"
            )
            session['output_history'] = output_history
            replaced = (current_input[:match.start()] + replacement + current_input[match.end():]).replace('  ', ' ')
            session['current_input'] = replaced.strip()
            session['step'] = step + 1
            continue
        else:
            html_out = "<br>".join(output_history + [f'<span style="color:red;">Error: No output generated for step {step + 1} in line: {html.escape(current_input)}</span><br>'])
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return html_out
            return render_template('index.html', output_html=html_out)

@app.route('/choose_output', methods=['POST'])
def choose_output():
    selected_output = request.form.get('selected_output')
    step = session.get('step', 0)
    current_input = session.get('current_input', '')
    match = re.search(r'<([^<>-]+)-([^<>-]+)>([^-<>]+)', current_input)
    if not match:
        return "Error: No match found."
    output_history = session.get('output_history', [])

    # Remove previous "Multiple outputs found" entry
    for i in range(len(output_history)-1, -1, -1):
        if "Multiple outputs found" in output_history[i]:
            output_history.pop(i)
            break

    # Add only the selected output to history
    output_history.append(
        f"Step {step+1}:<br>Tagged input: {html.escape(match.group(0))}<br>Chosen Output: {html.escape(selected_output)}"
    )
    session['output_history'] = output_history

    # Replace the matched tag with a new tag (not the output text)
    x_raw = match.group(1)
    y_raw = match.group(2)
    x_parts = x_raw.split('_')
    y_parts = y_raw.split('_')
    replacement = '_'.join(x_parts + y_parts)
    replaced = (current_input[:match.start()] + replacement + current_input[match.end():]).replace('  ', ' ')
    session['current_input'] = replaced.strip()
    session['step'] = step + 1
    return process_step()

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