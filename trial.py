from my_packages.process_paraphrase import paraphrase_generator

file_path = "tagged_examples.txt"

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

for original_input in lines:
    input_str = original_input.strip()
    prev_xs = []

    print(f"\nOriginal Input: {input_str}")
    
    while True:
        # Match the first <x-y>tag pattern (non-greedy)
        match = re.search(r'<([^<>-]+)-([^<>-]+)>([^-<>]+)', input_str)

        print(match)

        if not match:
            break  # No more matches

        x = match.group(1)
        y = match.group(2)
        tag = match.group(3)

        