import subprocess
import re

def generate_x_root(x, lifgam, vibhakti):
    ############################################
    # Calling all_gen.bin

    all_gen_path = "/home/mahe/scl/morph_bin/all_gen.bin"

    # Input to be passed (as a string)
    input_data = f"{x}<vargaH:nA><lifgam:{lifgam}><viBakwiH:{vibhakti}><vacanam:eka><level:1>"

    #print(f"Input to lt-proc: \n {input_data}")
    # Run lt-proc with the binary file
    result = subprocess.run(
        ["lt-proc", "-c", all_gen_path],
        input=input_data,
        capture_output=True,
        text=True
    )

    # If there's any error (stderr)
    if result.stderr:
        print("Error:")
        print(result.stderr)
    else:
        result = result.stdout
        # Print the output (stdout)
        #print("Output:")
        #print(result)

    x1 = result.split('/')[1].strip('$')
    
    return x1

def generate_y_root(y, y_vibhakti):
        
    ############################################
    # Calling all_morf.bin

    all_morf_path = "/home/mahe/scl/morph_bin/all_morf.bin"
    # Input to be passed (as a string)
    input_data = y
    
    #print(f"Input to lt-proc all_morf.bin: \n {input_data}")
    # Run lt-proc with the binary file
    result = subprocess.run(
        ["lt-proc", "-c", all_morf_path],
        input=input_data,
        capture_output=True,
        text=True
    )
    # If there's any error (stderr)
    if result.stderr:
        print("Error:")
        print(result.stderr)
    else:
        result = result.stdout
        # Print the output (stdout)
        #print("Output:")
        #print(result)

    # ^SriwaH/Sri1<kqw_prawyayaH:kwa><XAwuH:SriF><gaNaH:BvAxiH>$
    # Remove prefix and suffix
    cleaned = re.sub(r'^\^[^/]+/|\$$', '', result)

    # Match word + one or more <key:value> entries
    pattern = r'([A-Za-z0-9]+(?:<[^:>]+:[^>]+>)+)'
    groups = re.findall(pattern, cleaned)

    #for group in groups:
    #    print(f'checking group: {group}')

    # Filter groups containing <vargaH:nA>
    filtered_groups = [group for group in groups if '<vargaH:nA>' in group]

    y_list = []

    for group in filtered_groups:
        # Getting the lifgam
        match = re.search(r'<lifgam:([^>]+)>', group)
        if match:
            #print(f'matched group: {group}')
            lifgam = match.group(1)  
            # Extract the head word (before the first <)
            y_inter = re.match(r'^([A-Za-zāīūṛṅñṭḍṇśṣḷḹA-Za-z0-9_]+)<', group)
            y_inter = y_inter.group(1)
            #print(f'y: {y_inter}')
            #print(f"lifgams: {len(lifgam)}")
            #print(f"lifgam value: {lifgam}")
        
            ############################################
            # Calling all_gen.bin

            all_gen_path = "/home/mahe/scl/morph_bin/all_gen.bin"

            # Input to be passed (as a string)
            input_data = f"{y_inter}<vargaH:nA><lifgam:{lifgam}><viBakwiH:{y_vibhakti}><vacanam:eka><level:1>"

            #print(f"Input to lt-proc all_gen.bin: \n {input_data}")
            # Run lt-proc with the binary file
            result = subprocess.run(
                ["lt-proc", "-c", all_gen_path],
                input=input_data,
                capture_output=True,
                text=True
            )

            # If there's any error (stderr)
            if result.stderr:
                print("Error:")
                print(result.stderr)
            else:
                result = result.stdout
                # Print the output (stdout)
                #print("Output:")
                #print(result)

            if '/' in result:
                parts = result.strip('$').split('/')  # remove trailing $ first, then split
                remaining_parts = parts[1:]  # remove the first part
                for y in remaining_parts:
                    y_list.append(y)
            else:
                print(f"Warning: '/' not found in result: {result}")
    
    return y_list

        