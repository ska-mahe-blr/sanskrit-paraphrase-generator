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

def generate_x_root_A4(x, lifgam, vibhakti):
    ############################################
    # Calling all_gen.bin

    all_gen_path = "/home/mahe/scl/morph_bin/all_gen.bin"

    # Input to be passed (as a string)
    input_data = f"{x}<vargaH:saMKyeyam><lifgam:a><viBakwiH:{vibhakti}><vacanam:bahu><level:1>"

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

def generate_x_root_A6(x, lifgam, vibhakti):
    ############################################
    # Calling all_gen.bin

    all_gen_path = "/home/mahe/scl/morph_bin/all_gen.bin"

    # Input to be passed (as a string)
    input_data = f"{x}<vargaH:saMKyeyam><lifgam:{lifgam}><viBakwiH:{vibhakti}><vacanam:bahu><level:1>"

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


def generate_x_root_Bs3(x, lifgam, vibhakti):
    ############################################
    # Calling all_morf.bin

    all_morf_path = "/home/mahe/scl/morph_bin/all_morf.bin"
    # Input to be passed (as a string)
    input_data = x
    
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
    #print(cleaned)

    match = re.match(r'^(?:\w+)?(?:<[^<>:]+:[^<>]+>)+', cleaned)
    input_1 = match.group() if match else None
    
    # Remove <lifgam:...> and <level:...> pairs
    input_1 = re.sub(r'<(?:lifgam|level):[^<>]*>', '', input_1)
    #print('in', input_1)
    ############################################
    # Calling all_gen.bin

    all_gen_path = "/home/mahe/scl/morph_bin/all_gen.bin"

    # <kqw_XAwu:Ap1><upasarga:pra><kqw_prawyayaH:kwa><XAwuH:ApLz><gaNaH:svAxiH>prApwa<vargaH:nA><lifgam:puM><viBakwiH:2><vacanam:eka><level:2>
    # Input to be passed (as a string)
    #print('in1: '+input_1)
    input_data = input_1 + f"{x}<vargaH:nA><lifgam:{lifgam}><viBakwiH:{vibhakti}><vacanam:eka><level:2>"

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

def generate_x_root_Bs4(x, lifgam, vibhakti):
    ############################################
    # Calling all_morf.bin

    all_morf_path = "/home/mahe/scl/morph_bin/all_morf.bin"
    # Input to be passed (as a string)
    input_data = x
    
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
    #print(cleaned)

    # Find all full analysis chunks like: word<key:val><key:val>...
    analyses = re.findall(r'(?:\w+)?(?:<[^<>:]+:[^<>]+>)+', cleaned)

    # Take the second one (index 1)
    input_1 = analyses[1]
    
    # Remove <lifgam:...> and <level:...> pairs
    input_1 = re.sub(r'<(?:lifgam|level):[^<>]*>', '', input_1)
    #print('in', input_1)
    ############################################
    # Calling all_gen.bin

    all_gen_path = "/home/mahe/scl/morph_bin/all_gen.bin"

    # <kqw_XAwu:Ap1><upasarga:pra><kqw_prawyayaH:kwa><XAwuH:ApLz><gaNaH:svAxiH>prApwa<vargaH:nA><lifgam:puM><viBakwiH:2><vacanam:eka><level:2>
    # Input to be passed (as a string)
    #print('in1: '+input_1)
    input_data = input_1 + f"{x}<vargaH:nA><lifgam:{lifgam}><viBakwiH:{vibhakti}><vacanam:eka><level:2>"

    #print(f"Input to lt-proc: \n {input_data}")
    # Run lt-proc with the binary file<unmawwa-gafgam>A5
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

def generate_x_root_T7(x, lifgam, vibhakti):
    ############################################
    # Calling all_gen.bin

    all_gen_path = "/home/mahe/scl/morph_bin/all_gen.bin"

    # Input to be passed (as a string)
    input_data = f"{x}<vargaH:nA><lifgam:{lifgam}><viBakwiH:{vibhakti}><vacanam:bahu><level:1>"

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

def generate_y_root_A4(y, y_vibhakti):
    ############################################
    # Calling samAsa_upaxa.bin 

    all_morf_path = "/home/mahe/scl/morph_bin/samAsa_upaxa.bin"
    # Input to be passed (as a string)
    input_data = y
    #print(f"Input to lt-proc samAsa_upaxa.bin: {input_data}")
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
    #print('filtered:',filtered_groups)
    y_list = []

    for group in filtered_groups:
        # Getting the lifgam
        match = re.search(r'<lifgam:([^>]+)>', group)
        if match:
            #print(f'matched group: {group}')
            lifgam = match.group(1) 
            y_inter = re.match(r'^([A-Za-zāīūṛṅñṭḍṇśṣḷḹA-Za-z0-9_]+)<', group)
            y_inter = y_inter.group(1)
            #print(f'y1: {y_inter}')
            #print(f"lifgams: {len(lifgam)}")
            #print(f"lifgam value: {lifgam}")

            ############################################
            # Calling samAsa_upaxa.bin again

            all_morf_path = "/home/mahe/scl/morph_bin/" \
            "samAsa_upaxa.bin"
            # Input to be passed (as a string)
            input_data = y_inter

            #print(f"Input to lt-proc samAsa_upaxa.bin again: {input_data}")
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
            filtered_groups = [group for group in groups if '<vargaH:SaUPaPuM>' in group]
            #print('filtered:',filtered_groups)
            y_list = {}

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
                    #y_list.update({y_inter: lifgam})
                    #print(f"lifgams: {len(lifgam)}")
                    #print(f"lifgam value: {lifgam}")

                    ############################################

                    # Calling all_gen.bin

                    all_gen_path = "/home/mahe/scl/morph_bin/all_gen.bin"

                    # Input to be passed (as a string)
                    input_data = f"{y_inter}<vargaH:nA><lifgam:{lifgam}><viBakwiH:{y_vibhakti}><vacanam:bahu><level:1>"

                    #print(f"Input to lt-proc all_gen.bin: {input_data}")
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
                            y_list.update({y: lifgam})
                            
                    else:
                        print(f"Warning: '/' not found in result: {result}")
    
    return y_list

def generate_y_root_A5(y, y_vibhakti):
    ############################################
    # Calling samAsa_upaxa.bin 

    all_morf_path = "/home/mahe/scl/morph_bin/samAsa_upaxa.bin"
    # Input to be passed (as a string)
    input_data = y
    #print(f"Input to lt-proc samAsa_upaxa.bin: {input_data}")
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
    #print('filtered:',filtered_groups)
    y_list = {}

    for group in filtered_groups:
        # Getting the lifgam
        match = re.search(r'<lifgam:([^>]+)>', group)
        if match:
            #print(f'matched group: {group}')
            lifgam = match.group(1) 
            y_inter = re.match(r'^([A-Za-zāīūṛṅñṭḍṇśṣḷḹA-Za-z0-9_]+)<', group)
            y_inter = y_inter.group(1)
            #print(f'y1: {y_inter}')
            #print(f"lifgams: {len(lifgam)}")
            #print(f"lifgam value: {lifgam}")

            ############################################
            # Calling samAsa_upaxa.bin again

            all_morf_path = "/home/mahe/scl/morph_bin/samAsa_upaxa.bin"
            # Input to be passed (as a string)
            input_data = y_inter

            #print(f"Input to lt-proc samAsa_upaxa.bin again: {input_data}")
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
                    y_list.update({y: lifgam})
                    
            else:
                print(f"Warning: '/' not found in result: {result}")
            # Match word + one or more <key:value> entries
            pattern = r'([A-Za-z0-9]+(?:<[^:>]+:[^>]+>)+)'
            groups = re.findall(pattern, cleaned)

            #for group in groups:
            #    print(f'checking group: {group}')

            # Filter groups containing <vargaH:nA>
            filtered_groups = [group for group in groups if '<vargaH:SaUPaPuM>' in group]
            #print('filtered:',filtered_groups)
            y_list = {}

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
                    y_list.update({y_inter: lifgam})
                    #print(f"lifgams: {len(lifgam)}")
                    #print(f"lifgam value: {lifgam}")
            
    
    return y_list

def generate_y_root_A6(y, y_vibhakti):
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

    y_list = {}

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
            input_data = f"{y_inter}<vargaH:nA><lifgam:{lifgam}><viBakwiH:{y_vibhakti}><vacanam:bahu><level:1>"

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
                    y_list.update({y: lifgam})
            else:
                print(f"Warning: '/' not found in result: {result}")
    
    return y_list

def generate_y_root_A7(y, y_vibhakti):
    ############################################
    # Calling samAsa_upaxa.bin 

    all_morf_path = "/home/mahe/scl/morph_bin/samAsa_upaxa.bin"
    # Input to be passed (as a string)
    input_data = y
    #print(f"Input to lt-proc samAsa_upaxa.bin: {input_data}")
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
    #print('filtered:',filtered_groups)
    y_list = []

    for group in filtered_groups:
        # Getting the lifgam
        match = re.search(r'<lifgam:([^>]+)>', group)
        if match:
            #print(f'matched group: {group}')
            lifgam = match.group(1) 
            y_inter = re.match(r'^([A-Za-zāīūṛṅñṭḍṇśṣḷḹA-Za-z0-9_]+)<', group)
            y_inter = y_inter.group(1)
            #print(f'y1: {y_inter}')
            #print(f"lifgams: {len(lifgam)}")
            #print(f"lifgam value: {lifgam}")

            ############################################
            # Calling samAsa_upaxa.bin again

            all_morf_path = "/home/mahe/scl/morph_bin/samAsa_upaxa.bin"
            # Input to be passed (as a string)
            input_data = y_inter

            #print(f"Input to lt-proc samAsa_upaxa.bin again: {input_data}")
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
            filtered_groups = [group for group in groups if '<vargaH:SaUPaPuM>' in group]
            #print('filtered:',filtered_groups)
            y_list = {}

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
                    #y_list.update({y_inter: lifgam})
                    #print(f"lifgams: {len(lifgam)}")
                    #print(f"lifgam value: {lifgam}")

                    ############################################

                    # Calling all_gen.bin

                    all_gen_path = "/home/mahe/scl/morph_bin/all_gen.bin"

                    # Input to be passed (as a string)
                    input_data = f"{y_inter}<vargaH:nA><lifgam:{lifgam}><viBakwiH:{y_vibhakti}><vacanam:eka><level:1>"

                    #print(f"Input to lt-proc all_gen.bin: {input_data}")
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
                            y_list.update({y: lifgam})
                            
                    else:
                        print(f"Warning: '/' not found in result: {result}")
    
    return y_list

def generate_y_root_Tds(y, y_vibhakti):
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
            input_data = f"{y_inter}<vargaH:nA><lifgam:{lifgam}><viBakwiH:{y_vibhakti}><vacanam:bahu><level:1>"

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


def generate_y_lifgam_Tp(y):
    ############################################
    # Calling all_morf.bin

    all_morf_path = "/home/mahe/scl/morph_bin/all_morf.bin"
    # Input to be passed (as a string)
    input_data = y
    
    #print(f"Input to lt-proc all_morf.bin:  {input_data}")
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

    match = re.search(r'<lifgam:([^>]+)>', result)
    
    if match:
            #print(f'matched group: {group}')
            lifgam = match.group(1)

    return lifgam

#def generate_y_root_Bs2(y, y_vibhakti):
    ############################################
    # Calling samAsa_upaxa.bin 

    all_morf_path = "/home/mahe/scl/morph_bin/samAsa_upaxa.bin"
    # Input to be passed (as a string)
    input_data = y
    #print(f"Input to lt-proc samAsa_upaxa.bin: {input_data}")
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
        print("Output1:")
        print(result)

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
    #print('filtered:',filtered_groups)
    y_list = {}

    for group in filtered_groups:
        # Getting the lifgam
        match = re.search(r'<lifgam:([^>]+)>', group)
        if match:
            #print(f'matched group: {group}')
            lifgam = match.group(1) 
            y_inter = re.match(r'^([A-Za-zāīūṛṅñṭḍṇśṣḷḹA-Za-z0-9_]+)<', group)
            y_inter = y_inter.group(1)
            #print(f'y1: {y_inter}')
            #print(f"lifgams: {len(lifgam)}")
            #print(f"lifgam value: {lifgam}")

            ############################################
            # Calling samAsa_upaxa.bin again

            all_morf_path = "/home/mahe/scl/morph_bin/samAsa_upaxa.bin"
            # Input to be passed (as a string)
            input_data = y_inter

            #print(f"Input to lt-proc samAsa_upaxa.bin again: {input_data}")
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
                print("Output2:")
                print(result)

            # ^SriwaH/Sri1<kqw_prawyayaH:kwa><XAwuH:SriF><gaNaH:BvAxiH>$
            # Remove prefix and suffix
            cleaned = re.sub(r'^\^[^/]+/|\$$', '', result)

            # Match word + one or more <key:value> entries
            pattern = r'([A-Za-z0-9]+(?:<[^:>]+:[^>]+>)+)'
            groups = re.findall(pattern, cleaned)

            #for group in groups:
            #    print(f'checking group: {group}')

            # Filter groups containing <vargaH:nA>
            filtered_groups = [group for group in groups if re.search(r'<vargaH:SaUPa[^ >]*>', group)]
            #print('filtered:',filtered_groups)
            y_list = {}

            for group in filtered_groups:
                
                # Getting the lifgam
                match = re.search(r'<(?:plifgam|lifgam):([^>]+)>', group)
                if match:
                    #print(f'matched group: {group}')
                    lifgam = match.group(1)  
                    # Extract the head word (before the first <)
                    y_inter = re.match(r'^([A-Za-zāīūṛṅñṭḍṇśṣḷḹA-Za-z0-9_]+)<', group)
                    y_inter = y_inter.group(1)
                    #print(f'y: {y_inter}')
                    #y_list.update({y_inter: lifgam})
                    #print(f"lifgams: {len(lifgam)}")
                    #print(f"lifgam value: {lifgam}")

                    ############################################

                    # Calling all_gen.bin

                    all_gen_path = "/home/mahe/scl/morph_bin/all_gen.bin"

                    # Input to be passed (as a string)
                    input_data = f"{y_inter}<vargaH:nA><lifgam:{lifgam}><viBakwiH:{y_vibhakti}><vacanam:eka><level:1>"

                    #print(f"Input to lt-proc all_gen.bin: {input_data}")
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
                            y_list.update({y: lifgam})
                            
                    else:
                        print(f"Warning: '/' not found in result: {result}")
    return y_list



def generate_y_root_B(y, y_vibhakti):
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
    #print('cleaned\n'+cleaned)

    # Match word + one or more <key:value> entries
    pattern = r'([A-Za-z0-9]+(?:<[^:>]+:[^>]+>)+)'
    groups = re.findall(pattern, cleaned)

    #for group in groups:
    #    print(f'checking group: {group}')

    # Filter groups containing <vargaH:nA>
    filtered_groups = [group for group in groups if '<vargaH:nA>' in group]
    #print(filtered_groups)
    y_list = {}

    for group in filtered_groups:
        # Getting the lifgam
        match = re.search(r'<lifgam:([^>]+)>', group)
        if match:
            #print(f'matched group: {group}')
            lifgam = match.group(1)  
            # Extract the head word (before the first <)
            y_inter = re.match(r'^([A-Za-zāīūṛṅñṭḍṇśṣḷḹA-Za-z0-9_]+)<', group)
            y_inter = y_inter.group(1)
            # print(f'y: {y_inter}')
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
                    y_list.update({y: lifgam})
                    
            else:
                print(f"Warning: '/' not found in result: {result}")
    
    return y_list

def generate_y_root_Bs2(y, y_vibhakti):
    ############################################
    # Calling samAsa_upaxa.bin 

    all_morf_path = "/home/mahe/scl/morph_bin/samAsa_upaxa.bin"
    # Input to be passed (as a string)
    input_data = y
    #print(f"Input to lt-proc samAsa_upaxa.bin: {input_data}")
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
        #print("Output1:", result)
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
    #print('filtered:',filtered_groups)
    y_list = {}

    for group in filtered_groups:
        # Getting the lifgam
        match = re.search(r'<lifgam:([^>]+)>', group)
        if match:
            #print(f'matched group: {group}')
            lifgam = match.group(1) 
            lifgam1 = lifgam
            y_inter = re.match(r'^([A-Za-zāīūṛṅñṭḍṇśṣḷḹA-Za-z0-9_]+)<', group)
            y_inter = y_inter.group(1)
            #print(f'y1: {y_inter}')
            #print(f"lifgams: {len(lifgam)}")
            #print(f"lifgam value: {lifgam}")

            ############################################
            # Calling samAsa_upaxa.bin again

            all_morf_path = "/home/mahe/scl/morph_bin/samAsa_upaxa.bin"
            # Input to be passed (as a string)
            input_data = y_inter

            #print(f"Input to lt-proc samAsa_upaxa.bin again: {input_data}")
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
                #print("Output2:", result)
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
            filtered_groups = [group for group in groups if re.search(r'<vargaH:SaUPa[^ >]*>', group)]
            #print('filtered:',filtered_groups)
            y_list = {}

            for group in filtered_groups:
                
                # Getting the lifgam
                match = re.search(r'<(?:plifgam|lifgam):([^>]+)>', group)
                if match:
                    #print(f'matched group: {group}')
                    lifgam = match.group(1)  
                    # Extract the head word (before the first <)
                    y_inter = re.match(r'^([A-Za-zāīūṛṅñṭḍṇśṣḷḹA-Za-z0-9_]+)<', group)
                    y_inter = y_inter.group(1)
                    #print(f'y: {y_inter}')
                    #y_list.update({y_inter: lifgam})
                    #print(f"lifgams: {len(lifgam)}")
                    #print(f"lifgam value: {lifgam}")

                    ############################################

                    # Calling all_gen.bin

                    all_gen_path = "/home/mahe/scl/morph_bin/all_gen.bin"

                    # Input to be passed (as a string)
                    input_data = f"{y_inter}<vargaH:nA><lifgam:{lifgam}><viBakwiH:{y_vibhakti}><vacanam:eka><level:1>"

                    #print(f"Input to lt-proc all_gen.bin: {input_data}")
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
                            y_list.update({y: [lifgam,lifgam1]})
                            
                    else:
                        print(f"Warning: '/' not found in result: {result}")
    return y_list
    
def generate_y_root_Bs4(y, y_vibhakti):
    ############################################
    # Calling samAsa_upaxa.bin 

    all_morf_path = "/home/mahe/scl/morph_bin/samAsa_upaxa.bin"
    # Input to be passed (as a string)
    input_data = y
    #print(f"Input to lt-proc samAsa_upaxa.bin: {input_data}")
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
    #print('filtered:',filtered_groups)
    y_list = {}

    for group in filtered_groups:
        # Getting the lifgam
        match = re.search(r'<lifgam:([^>]+)>', group)
        if match:
            #print(f'matched group: {group}')
            lifgam = match.group(1) 
            y_inter = re.match(r'^([A-Za-zāīūṛṅñṭḍṇśṣḷḹA-Za-z0-9_]+)<', group)
            y_inter = y_inter.group(1)
            #print(f'y1: {y_inter}')
            #print(f"lifgams: {len(lifgam)}")
            #print(f"lifgam value: {lifgam}")

            ############################################
            # Calling samAsa_upaxa.bin again

            all_morf_path = "/home/mahe/scl/morph_bin/samAsa_upaxa.bin"
            # Input to be passed (as a string)
            input_data = y_inter

            #print(f"Input to lt-proc samAsa_upaxa.bin again: {input_data}")
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
            filtered_groups = [group for group in groups if re.search(r'<vargaH:SaUPa[^ >]*>', group)]
            #print('filtered:',filtered_groups)
            y_list = {}

            for group in filtered_groups:
                
                # Getting the lifgam
                match = re.search(r'<(?:plifgam|lifgam):([^>]+)>', group)
                if match:
                    #print(f'matched group: {group}')
                    lifgam = match.group(1)  
                    # Extract the head word (before the first <)
                    y_inter = re.match(r'^([A-Za-zāīūṛṅñṭḍṇśṣḷḹA-Za-z0-9_]+)<', group)
                    y_inter = y_inter.group(1)
                    #print(f'y: {y_inter}')
                    #y_list.update({y_inter: lifgam})
                    #print(f"lifgams: {len(lifgam)}")
                    #print(f"lifgam value: {lifgam}")

                    ############################################

                    # Calling all_gen.bin

                    all_gen_path = "/home/mahe/scl/morph_bin/all_gen.bin"

                    # Input to be passed (as a string)
                    input_data = f"{y_inter}<vargaH:nA><lifgam:{lifgam}><viBakwiH:{y_vibhakti}><vacanam:eka><level:1>"

                    #print(f"Input to lt-proc all_gen.bin: {input_data}")
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
                            y_list.update({y: lifgam})
                            
                    else:
                        print(f"Warning: '/' not found in result: {result}")
    return y_list


def generate_y_root_Ds(y, y_vibhakti):
    ############################################
    # Calling sup_gen.bin

    sup_gen_path = "/home/mahe/scl/morph_bin/sup_gen.bin"
    # Input to be passed (as a string)
    input_data = y
    
    #print(f"Input to lt-proc sup_gen.bin: \n {input_data}")
    # Run lt-proc with the binary file
    result = subprocess.run(
        ["lt-proc", "-c", sup_gen_path],
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

    y_list = {}

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
                    y_list.update({y: lifgam})
                    
            else:
                print(f"Warning: '/' not found in result: {result}")
    
    return y_list


def generate_feminine_form(stem,tag):

    gaNa_ajAxi = ['ajA', 'edakA', 'kokilA', 'catakA', 'aSvA', 'mURikA', 'bAlA', 'hodA', 'pAkA', 'vawsA', 
                  'manxA', 'vilAwA', 'pUrvApihANA', 'pUrvApahANA', 'aparApahANA', 'saMBaswrAjinaSaNapiNdeByaH PalAw', 
                  'saxackANdaprAnwaSawEkeByaH puRpAw', 'SUxrA cAmahawpUrvA jAwiH', 'kruFcA', 'uRNihA', 'xevaviSA', 
                  'jyeRTA', 'kaniRTA', 'maXyamA', 'puMyogeZpi', 'mUlAnnaFaH', 'xaMRtrA']
    
    
    #4.1.4 अजाद्यतष्टाप्.
    if stem.endswith('a') or stem in gaNa_ajAxi:
        # Apply TAp (A)
        feminine_stem = stem[:-1] + 'A'

    #4.1.5 ऋन्नेभ्यो ङीप् 
    if stem.endswith('q'):
        # Apply fIp (I)
        feminine_stem = stem[:-1] + 'rI'
    if stem.endswith('n'):
        # Apply fIp (I)
        feminine_stem = stem + 'I'

    #4.1.7	वनो र च
    if stem.endswith('van'):
        # Apply fIp (I), the 'n' in van changes to 'r'
        feminine_stem = stem[:-1] + 'rI'

    #4.1.8 पादोऽन्यतरस्याम् (discussion)
    if stem.endswith('pAxa') :
        # Apply fIp (I) by vikalpa
        feminine_stem = stem + 'I'

    #4.1.9 टाबृचि
    if stem.endswith('pAxa') :
        # Apply TAp (A), this is only for the words denoting vedic mantras
        feminine_stem = stem + 'A'

    #4.1.13 डाबुभाभ्यामन्यतरस्याम्
    if stem.endswith('man') or (stem.endswith('an') and tag[0]=='B'): # for checking if B tag
        # Apply DAp (A)
        feminine_stem = stem[:-2] + 'A'

    #4.1.15	टिड्ढाणञ्द्वयसज्दघ्नञ्मात्रच्तयप्ठक्ठञ्कञ्क्वरपः (discussion)
    #if stem.in('T') or stem.has_a_suffix_beginning_with('Da') or stem.has_suffix('aN', 'aF', 'xvayasac', 'xaGnac', 'mAwrac',
    #                                                                            'wayap', 'Tak', 'TaF', 'kan', 'kvarap') :
    #    # Apply fIp (I)
    #    feminine_stem = stem + 'I'

    #4.1.16 यञश्च  (discussion)
    #if stem.has_suffix('yaF') :
    #    # # Apply fIp (I)
    #    feminine_stem = stem + 'I'

    #4.1.17 प्राचां ष्फ तद्धितः  (discussion)
    #if stem.has_suffix('yaF') :
    #    # Apply RPa (P). According to eastern grammarians
    #    feminine_stem = stem + 'P'

    #4.1.18 सर्वत्र लोहितादिकतन्तेभ्यः.  
    gaNa_lohiwAxi = ['lohiwa', 'SaMsiwa', 'baBru', 'valgu', 'maNdu', 'Safku', 'ligu', 'guhalu', 'manwu', 'mafkRu', 'aligu', 'jigIRu', 'manu', 
                    'wanwu', 'manAyIsUnu', 'kaWaka', 'kanWaka', 'qkRa', 'wqkRa', 'vqkRa', 'wanu', 'warukRa', 'walukRa', 'waNda', 'vawaNda', 
                    'kapikawa', 'kapi', 'kawa']
    if stem in gaNa_lohiwAxi:
        # Apply RPa (P).
        feminine_stem = stem + 'P'

    #4.1.19 कौरव्यमाण्डूकाभ्यां च  (discussion)
    #if stem.is_word('kaOravya') or stem.is_word('maNDUka'):
    #    # Apply RPa (P).
    #    feminine_stem = stem + 'P'

    #4.1.20 वयसि प्रथमे  (discussion)
    if stem.endswith('a$') :
        # Apply fIp (I). The word should denote early age
        feminine_stem = stem + 'I'

    return feminine_stem