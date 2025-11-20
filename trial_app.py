from flask import Flask, render_template, request, Response
import re
import io
import contextlib
from my_packages.process_paraphrase import paraphrase_generator
import html

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    outputs = []
    input_text = ''
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        lines = input_text.split('\n')

        def generate():
            first = True
            for original_input in lines:
                original_input = original_input.strip()
                if not original_input:
                    continue
                if not first:
                    yield "<br>"
                first = False
                original_input = [original_input]
                yield f"Original Input: {html.escape(original_input[0])}<br>"

                iteration = 0
                while True:
                    match = re.search(r'<([^<>-]+)-([^<>-]+)>([^-<>]+)', original_input[0])
                    if match is None:
                        break
                    x_raw = match.group(1)
                    y_raw = match.group(2)
                    tag = match.group(3)
                    x_parts = x_raw.split('_')
                    y_parts = y_raw.split('_')
                    custom_tagged_input = f"<{'_'.join(x_parts)}-{'_'.join(y_parts)}>{tag}"
                    yield f"Step {iteration + 1}:<br>"
                    yield f'Tagged input: {html.escape(custom_tagged_input)}<br>'
                    # Paraphrase: last word of x_parts and full y_raw
                    x = x_parts[-1]
                    y = y_parts[-1] 
                    buf = io.StringIO()
                    with contextlib.redirect_stdout(buf):
                        paraphrase_generator(x, y, tag)
                    output_lines = buf.getvalue().strip().split('\n')
                    print(output_lines)
                    prev_output = None
                    prefix = ' '.join(x_parts[:-1]) if len(x_parts) > 1 else ''
                    for output in output_lines:
                        out_words = output.split()
                        x_prefix = '_'.join(x_parts[:-1]) if len(x_parts) > 1 else ''
                        y_prefix = '_'.join(y_parts[:-1]) if len(y_parts) > 1 else ''
                        x_current = x_parts[-1]
                        y_current = y_parts[-1]
                        x_found = False
                        y_found = False
                        new_out = []
                        for word in out_words:
                            # Insert prev_x + paraphrased x (only if there is a previous x)
                            if not x_found and word[:3] == x_current[:3]:
                                if x_prefix:
                                    new_out.append(f"{x_prefix}_{word}")  # Use paraphrased word, not raw x
                                else:
                                    new_out.append(word)
                                x_found = True
                                continue
                            # Insert prev_y + paraphrased y (only if there is a previous y)
                            if not y_found and word[:3] == y_current[:3]:
                                if y_prefix:
                                    new_out.append(f"{y_prefix}_{word}")  # Use paraphrased word, not raw y
                                else:
                                    new_out.append(word)
                                y_found = True
                                continue
                            new_out.append(word)
                        out = ' '.join(new_out)
                        out = ' '.join(out.split())
                        if out != prev_output:
                            yield f"Output: {html.escape(out)}<br>"
                        prev_output = out
                    # Replace tag in input with all x_parts + all y_parts
                    replacement = '_'.join(x_parts + y_parts)
                    replaced = (original_input[0][:match.start()] + replacement + original_input[0][match.end():]).replace('  ', ' ')
                    original_input[0] = replaced.strip()
                    iteration += 1

                yield "<br>"
                #outputs.append(step_outputs)
                

        return Response(generate(), mimetype='text/html')
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, port=5001)