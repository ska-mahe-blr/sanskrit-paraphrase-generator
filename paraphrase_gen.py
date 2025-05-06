import re
import json
import subprocess
import generator

file_path = "tagged_examples.txt"

with open(file_path, "r", encoding="utf-8") as file:
    inputs = file.readlines()

for tagged_input in inputs:

    # Updated regex to capture any characters for x, y, and tag
    pattern = r"<(.*?)-(.*?)>(.*)"

    match = re.match(pattern, tagged_input)

    if match:
        x = match.group(1)
        y = match.group(2)
        tag = match.group(3)
        print(f"x = {x}, y = {y}, tag = {tag}")
    else:
        print("Input format is incorrect.")

    #############################################
    # Getting the gender

    json_path = 'word_gender.json'

    # Read and parse the JSON
    with open(json_path, "r", encoding="utf-8") as file:
        gender = json.load(file)

    try:
        lifgams = gender[x]
        if isinstance(lifgams, str):
            lifgams = [lifgams]
    except KeyError:
        print(f"No gender info found for {x}")
          # skip to next input

  
    for lifgam in lifgams:

        match tag:

            # For A<num>
            case tag if tag[0] == 'A' and tag[1].isdigit():

                match tag:

                    # For A2: <x-y>A2 => x{3} विपरीतम् वृत्तम् viparIwam vqwwam
                    case tag if tag == 'A2':
                        x1 = generator.generate_x_root(x,lifgam, 3)

                        print(f'{x1} viparIwam vqwwam')

            ############################################
                       
            # For T<num>
            case tag if tag[0] == 'T' and tag[1].isdigit():
                # Getting vibhakti
                vibhakti = tag[1]
                x1 = generator.generate_x_root(x,lifgam, vibhakti)

                # For T2 to T7: <x-y>T(2:7) => x{(2:7)} y 
                if int(tag[1]) in range(2,8):
                    print(f"{x1} {y}")

                # For T1: <x-y>T1 => x{1} y{6}
                else:
                    y_list = generator.generate_y_root(y, 6)

                    for y1 in list(set(y_list)):
                        print(f"{x1} {y1}")

            # For Tn: <x-y>Tn => न y            
            case tag if tag == 'Tn':

                y_list = generator.generate_y_root(y, 1)

                for y1 in list(set(y_list)):
                    print(f"{x} {y1}")

            ############################################

            # For K<num>
            case tag if tag[0] == 'K' and tag[1].isdigit():
                match tag:

                    # For K1: <x-y>K1 => x{1} तत ् y{1} च
                    case tag if tag == 'K1':

                        x1 = generator.generate_x_root(x,lifgam, 1)

                        y_list = generator.generate_y_root(y, 1)

                        for y1 in list(set(y_list)):
                            print(f"{x1} waw {y1} ca")
                            
                    
                    # For K2: <x-y>K2 => x{1} च y{1} च
                    case tag if tag == 'K2':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                                
                        y_list = generator.generate_y_root(y, 1)

                        for y1 in list(set(y_list)):
                            print(f"{x1} ca {y1} ca")
                            

                    # For K3: <x-y>K3 => x{1}च असौ y{1} च
                    case tag if tag == 'K3':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                                
                        y_list = generator.generate_y_root(y, 1)

                        for y1 in list(set(y_list)):
                            print(f"{x1} ca asO {y1} ca")
                                

                    # For K4: <x-y>K4 => x{1} इव y{1}
                    case tag if tag == 'K4':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                                
                        y_list = generator.generate_y_root(y, 1)

                        for y1 in list(set(y_list)):
                            print(f"{x1} iva {y1}")
                             
                    
                    # For K5: <x-y>K5 => x{1} y{1} इव
                    case tag if tag == 'K5':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                                
                        y_list = generator.generate_y_root(y, 1)

                        for y1 in list(set(y_list)):
                            print(f"{x1} {y1} iva ")
                             

                    # For K6: <x-y>K6 => x{1} एव y{1}
                    case tag if tag == 'K6':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                                
                        y_list = generator.generate_y_root(y, 1)

                        for y1 in list(set(y_list)):
                            print(f"{x1} eva {y1}")
                             

                    # For K7: <x-y>K7 => x{1} इित y{1}
                    case tag if tag == 'K7':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                                
                        y_list = generator.generate_y_root(y, 1)

                        for y1 in list(set(y_list)):
                            print(f"{x1} iwi {y1}")
                             

            ############################################## 
            case tag if tag[0] == 'B':

                match tag:

                    case tag if tag[-2:] == 's2':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                                
                        y_list = generator.generate_y_root(y, 1)

            ############################################## 
            # For S: <x-y>S => y{1} x{1}                 
            case tag if tag[0] == 'S':
                x1 = generator.generate_x_root(x,lifgam, 1)
                                
                y_list = generator.generate_y_root(y, 1)

                for y1 in list(set(y_list)):
                    print(f"{y1} {x1}")

            ############################################## 
            # For d: <x-y>d => x y 
            case tag if tag[0] == 'd':    
                print(f"{x} {y}")

            
    print("#############################################")
