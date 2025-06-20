import re
import io
import contextlib
from my_packages.process_paraphrase import paraphrase_generator

file_path = "tagged_examples.txt"

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

for original_input in lines:
    current_strings = [original_input.strip()]
    x_chain = []  # To keep track of raw x's
    prev_y = None

    print(f"\nOriginal Input: {original_input.strip()}")

    iteration = 0
    while True:
        new_strings = []
        any_match = False
        for input_str in current_strings:
            match = re.search(r'<([^<>-]+)-([^<>-]+)>([^-<>]+)', input_str)
            print(f"Processing: {input_str}")
            if not match:
                new_strings.append(input_str)
                continue

            any_match = True

            if iteration == 0:
                x_raw = match.group(1)
            else:
                x_raw = prev_y  # Use previous y as x from second iteration onwards

            x = x_raw.split()[-1]
            y = match.group(2)
            tag = match.group(3)

            # Track the chain of raw x's
            x_chain.append(x_raw)

            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                paraphrase_generator(x, y, tag)
            output_lines = buf.getvalue().strip().split('\n')

            for output in output_lines:
                print(f"  Generated output: {output}")
                replaced = input_str[:match.start()] + output + input_str[match.end():]
                print(f"  Used x chain: {x_chain}")
                new_strings.append(replaced)

            prev_y = y  # Update prev_y for next iteration

        current_strings = new_strings
        if not any_match:
            break
        iteration += 1

    print("Final Processed Outputs:")
    for s in current_strings:
        print(s)