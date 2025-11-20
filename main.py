import re
import io
import contextlib
from my_packages.process_paraphrase import paraphrase_generator

file_path = "trial_examples.txt"


with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

for original_input in lines:
    # Strip whitespace and prepare the input
    original_input = [original_input.strip()]
    x_chain = []
    prev_y = None

    print(f"\nOriginal Input: {original_input[0]}")

    iteration = 0

    # Loop through the current strings until no more matches are found
    while True:
        match = re.search(r'<([^<>-]+)-([^<>-]+)>([^-<>]+)', original_input[0])

        if match is None:
            break

        # Extract x, y and tag from the current match 
        tagged_input = match.group(0)
        print('Tagged input:', tagged_input)

        if iteration == 0:
            x_raw = match.group(1)
        else:
            x_raw = prev_y 

        x = x_raw.split()[-1]
        y_raw = match.group(2)
        y = y_raw.split()[-1]
        tag = match.group(3)

        if x == y:
            break

        x_chain.append(x)

        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            paraphrase_generator(x, y, tag)
        output_lines = buf.getvalue().strip().split('\n')
        
        seen_outputs = set()
        for output in output_lines:
            if len(x_raw) > 1:
                words = [w for w in output.split() if w.startswith(x)]
                rem_x = ' '.join(x_raw.split()[:-1])
                if words:
                    output = output.replace(words[0], (rem_x + ' ' + words[0]).strip())

            if len(y_raw) > 1:
                words = [w for w in output.split() if w.startswith(y)]
                rem_y = ' '.join(y_raw.split()[:-1])
                if words:
                    output = output.replace(words[0], (rem_y + ' ' + words[0]).strip())

            output = ' '.join(output.split())  # Remove extra spaces between words
            if output not in seen_outputs:
                print(f"Output: {output}")
                seen_outputs.add(output)

        prev_y = y

        # Replace the matched part in the original input
        #replaced = (original_input[0][:match.start()] + output + original_input[0][match.end():]).replace('  ', ' ')
        #original_input[0] = ' '.join(replaced.split())  # Remove extra spaces globally
        #print(f"Replaced input: {original_input[0]}")

        replacement = f"{x_raw} {y_raw}"
        replaced = (original_input[0][:match.start()] + replacement + original_input[0][match.end():]).replace('  ', ' ')
        original_input[0] = ' '.join(replaced.split())  # Remove extra spaces globally
        #print(f"Replaced input: {original_input[0]}")

        #break
        
