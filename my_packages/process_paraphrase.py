import re
import json
import subprocess
import my_packages.generator as generator

def paraphrase_generator(x, y, tag):

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

    if tag == 'A5':
        # For A5: <x-y>A5 => x’{1} y{1} यस्मिन् देशे
        y_list = generator.generate_y_root_B(y, 1)
        
        # Remove duplicate values in dictionary
        # Using dictionary comprehension
        temp = {val: key for key, val in y_list.items()}
        y_list = {val: key for key, val in temp.items()}
        print(y_list)
        for y1, lifgam in y_list.items():
            x1 = generator.generate_x_root(x,lifgam, 1)
            print(f"{x1} {y1} yasmin xeSe")

    for lifgam in lifgams:
    
        match tag:

            # For A<num>
            case tag if tag[0] == 'A' and tag[1].isdigit():

                match tag:

                    # For A2: <x-y>A2 => x{3} विपरीतम् वृत्तम् viparIwam vqwwam
                    case tag if tag == 'A2':
                        x1 = generator.generate_x_root(x,lifgam, 3)

                        print(f'{x1} viparIwam vqwwam') # NOT WORKING

                    # For A4: <x-y>A4 => x{6} y’{6} समाहारः
                    case tag if tag == 'A4':
                        x1 = generator.generate_x_root(x,lifgam, 6)

                        y_list = generator.generate_y_root(y, 6)

                        for y1 in list(set(y_list)):
                            print(f"{x1} {y1} samAhAraH") # NOT WORKING
                    
                    # For A7: <x-y>A7 => y{6} x
                    case tag if tag == 'A7':
                        
                        y_list = generator.generate_y_root(y, 6)
                        print(y_list)
                        for y1 in list(set(y_list)):
                            print(f"{y1} {x}")# NOT WORKING

                    
 

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

                    # For Bs2: <x-y>Bs2 => x{1} y{1} यत ्{g}{2}
                    case tag if tag[-2:] == 's2':
                        x1 = generator.generate_x_root_B(x,lifgam, 1)
                        print(x1, y, 'in')
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, lifgam in y_list.items():
                            if lifgam == 'puM':
                                z1 = 'yaM'
                            elif lifgam == 'swrI':
                                z1 = 'yAM'
                            else:
                                z1 = 'yaw'
                            print(f"{x1} {y1} {z1}")

                    # For Bs3: <x-y>Bs3 => x{1} y{1} येन/यया/येन
                    case tag if tag[-2:] == 's3':
                        x1 = generator.generate_x_root_Bs3(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, lifgam in y_list.items():
                            if lifgam == 'puM':
                                z1 = 'yena'
                            elif lifgam == 'swrI':
                                z1 = 'yayA'
                            else:
                                z1 = 'yena'
                            print(f"{x1} {y1} {z1}")

                    # For Bs4: <x-y>Bs4 => x{1} y{1} यस्मै/यस्यै/यस्मै
                    case tag if tag[-2:] == 's4':
                        x1 = generator.generate_x_root_Bs4(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, lifgam in y_list.items():
                            if lifgam == 'puM':
                                z1 = 'yasmE'
                            elif lifgam == 'swrI':
                                z1 = 'yasyE'
                            else:
                                z1 = 'yasmE'
                            print(f"{x1} {y1} {z1}") # NOT WORKING

                    # For Bs5: <x-y>Bs5 => x{1} y{1} यस्मात्/यस्याः/यस्मात्
                    case tag if tag[-2:] == 's5':
                        x1 = generator.generate_x_root_Bs3(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, lifgam in y_list.items():
                            if lifgam == 'puM':
                                z1 = 'yasmAw'
                            elif lifgam == 'swrI':
                                z1 = 'yasyAH'
                            else:
                                z1 = 'yasmAw'
                            print(f"{x1} {y1} {z1}")

                    # For Bs6: <x-y>Bs6 => x{1} y{1} यस्य/यस्याः/यस्य
                    case tag if tag[-2:] == 's6':
                        x1 = generator.generate_x_root_Bs3(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, lifgam in y_list.items():
                            if lifgam == 'puM':
                                z1 = 'yasya'
                            elif lifgam == 'swrI':
                                z1 = 'yasyAH'
                            else:
                                z1 = 'yasya'
                            print(f"{x1} {y1} {z1}") 

                    # For Bs7: <x-y>Bs7 => x{1} y{1} यस्मिन्/यस्याम्/यस्मिन्
                    case tag if tag[-2:] == 's7':
                        x1 = generator.generate_x_root_Bs3(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, lifgam in y_list.items():
                            if lifgam == 'puM':
                                z1 = 'yasmin'
                            elif lifgam == 'swrI':
                                z1 = 'yasyAm'
                            else:
                                z1 = 'yasmin'
                            print(f"{x1} {y1} {z1}") 

                    # For Bsd: <x-y>Bsd => x{6} च y{6} च यदन्तरालम्
                    case tag if tag[-2:] == 'sd':
                        x1 = generator.generate_x_root(x,lifgam, 6)
                            
                        y_list = generator.generate_y_root(y, 6)

                        for y1 in list(set(y_list)):
                            print(f"{x1} ca {y1} ca yaxanwarAlam")

                    # For Bsp: <x-y>Bsp => x{3} च y{3} च प्रहृत्य इदम् युद्धम् प्रवृत्तम्
                    case tag if tag[-2:] == 'sp':
                        x1 = generator.generate_x_root(x,lifgam, 3)
                            
                        y_list = generator.generate_y_root(y, 3)

                        for y1 in list(set(y_list)):
                            print(f"{x1} ca {y1} ca prahqwya ixam yuxXam pravqwwam")
                        

                    # For Bsg: <x-y>Bsg => x{7}-y{7} गृहित्वा इदम् युद्धम् प्रवृत्तम्
                    case tag if tag[-2:] == 'sg':
                        x1 = generator.generate_x_root(x,lifgam, 7)
                            
                        y_list = generator.generate_y_root(y, 7)

                        for y1 in list(set(y_list)):
                            print(f"{x1} {y1} gqhiwvA ixam yuxXam pravqwwam")

                    # For Bsmn: <x-y>Bsmn => न विद्यते y{1} यस्य/यस्याः/यस्य
                    case tag if tag[-3:] == 'smn':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, lifgam in y_list.items():
                            if lifgam == 'puM':
                                z1 = 'yasya'
                            elif lifgam == 'swrI':
                                z1 = 'yasyAH'
                            else:
                                z1 = 'yasya'
                            print(f"na vixyawe {y1} {z1}") 

                    # For Bss: <x-y>Bss = > x{1} वा y{1} यस्य/यस्याः/यस्य
                    case tag if tag[-2:] == 'ss':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, lifgam in y_list.items():
                            if lifgam == 'puM':
                                z1 = 'yasya'
                            elif lifgam == 'swrI':
                                z1 = 'yasyAH'
                            else:
                                z1 = 'yasya'
                            print(f"{x1} vA {y1} {z1}") 

                    # For Bsu: <x-y>Bsu => x{1} इव y{1} यस्य/यस्याः/यस्य
                    case tag if tag[-2:] == 'su':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, lifgam in y_list.items():
                            if lifgam == 'puM':
                                z1 = 'yasya'
                            elif lifgam == 'swrI':
                                z1 = 'yasyAH'
                            else:
                                z1 = 'yasya'
                            print(f"{x1} iva {y1} {z1}")

                    # For Bv: <x-y>Bv => x y{1} यस्य/यस्याः/यस्य
                    case tag if tag[-1:] == 'v':

                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, lifgam in y_list.items():
                            if lifgam == 'puM':
                                z1 = 'yasya'
                            elif lifgam == 'swrI':
                                z1 = 'yasyAH'
                            else:
                                z1 = 'yasya'
                            print(f"{x} {y1} {z1}")

                    # For Bvs: <x-y>Bvs => y{6} x’ ये सन्ति ते
                    case tag if tag[-2:] == 'vs':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root(y, 7)

                        for y1 in list(set(y_list)):
                            print(f"{y1} {x1} ye sanwi we")

                    # For BvS: <x-y>BvS => y{3} सह
                    case tag if tag[-2:] == 'vS':
                        y_list = generator.generate_y_root(y, 3)

                        for y1 in list(set(y_list)):
                            print(f"{y1} saha")

                    # For BvU: <x-y>BvU => x{6} इव y यस्य/यस्याः/यस्य
                    case tag if tag[-2:] == 'vU':
                        x1 = generator.generate_x_root(x,lifgam, 6)
                            
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, lifgam in y_list.items():
                            if lifgam == 'puM':
                                z1 = 'yasya'
                            elif lifgam == 'swrI':
                                z1 = 'yasyAH'
                            else:
                                z1 = 'yasya'
                            print(f"{x1} iva {y} {z1}")

            ############################################
            # For D Tag
            case tag if tag[0] == 'D':
                match tag:

                    # <x-y+>Di => x{1} च (y{1} च)+ ; Here + indicates one or more occurences.
                

                    case tag if tag[1] == 'i':

                        from itertools import product

                        x1 = generator.generate_x_root(x, lifgam, 1)

                        ys = y.split('-') if '-' in y else [y]

                        # Collect roots for each y-part
                        all_y_roots = []
                        for y_part in ys:
                            y_roots = generator.generate_y_root(y_part, 1)
                            y_roots = list(set(y_roots))  # optional deduplication
                            all_y_roots.append(y_roots)

                        # Cartesian product of all y-roots
                        for combo in product(*all_y_roots):
                            full_line = f'{x1} ca ' + ' ca '.join(combo)
                            print(full_line)
                    
                    # For Ds: <x-y+>Ds => x{1} च (y{1} च)+ एतत ्n समाहारः
                    case tag if tag[1] == 's':

                        from itertools import product

                        x1 = generator.generate_x_root(x, lifgam, 1)
                        print(x1)

                        ys = y.split('-') if '-' in y else [y]

                        y_length = len(ys)

                        # Collect roots for each y-part
                        all_y_roots = []
                        for y_part in ys:
                            y_roots = generator.generate_y_root_Bs2(y_part, 1)
                            y_roots = list(set(y_roots))  # optional deduplication
                            all_y_roots.append(y_roots)

                        # Cartesian product of all y-roots
                        for combo in product(*all_y_roots):

                            if y_length == 1:
                                full_line = f'{x1} ca ' + ' ca '.join(combo) + 'ewayoH samAhAraH'
                                print(full_line)
                            else:
                                full_line = f'{x1} ca ' + ' ca '.join(combo) + 'eweRAm samAhAraH'
                                print(full_line)

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

            
    #print("#############################################")
