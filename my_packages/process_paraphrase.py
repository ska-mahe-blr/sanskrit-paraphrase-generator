import re
import json
import subprocess
import my_packages.generator as generator
import pandas as pd

def paraphrase_generator(x, y, tag):
    

    # For A1: <x-y>A1 => y{6} f{x} 
    # <upa-kqRNam>A1
    if tag == 'A1':

        df = pd.read_csv('lookup_data/a1.csv')

        tagged_input = f'<{x}-{y}>A1'

        if tagged_input in df['input'].values:
            ind = df[df['input'] == tagged_input].index[0]
            print(df.at[ind, 'output'].strip())

        else:
            print('No value found')

        return
    
    if tag == "A3":

        df = pd.read_csv('lookup_data/a3.csv')

        tagged_input = f'<{x}-{y}>A3'

        if tagged_input in df['input'].values:
            ind = df[df['input'] == tagged_input].index[0]
            print(df.at[ind, 'output'].strip())

        else:
            print('No value found')

        return
    
    # For A5: <x-y>A5 => x'{1} y{1} यस्मिन् देशे
    if tag == 'A5':
        
        y_list = generator.generate_y_root_A5(y, 1)
        
        for y1, lifgam in y_list.items():

            x1 = generator.generate_feminine_form(x, tag)

            print(f"{x1} {y1} yasmin xeSe")

    
    if tag == "Km":

        df = pd.read_csv('lookup_data/km.csv')

        tagged_input = f'<{x}-{y}>Km'

        if tagged_input in df['input'].values:
            ind = df[df['input'] == tagged_input].index[0]
            print(df.at[ind, 'output'].strip())

        else:
            print('No value found')

        return
    
    if tag == "Kn":

        df = pd.read_csv('lookup_data/kn.csv')

        tagged_input = f'<{x}-{y}>Kn'

        if tagged_input in df['input'].values:
            ind = df[df['input'] == tagged_input].index[0]
            print(df.at[ind, 'output'].strip())

        else:
            print('No value found')

        return


    if tag == "Tm":

        df = pd.read_csv('lookup_data/tm.csv')

        tagged_input = f'<{x}-{y}>Tm'

        if tagged_input in df['input'].values:
            ind = df[df['input'] == tagged_input].index[0]
            print(df.at[ind, 'output'].strip())

        else:
            print('No value found')

        return
    
    if tag == "Tp":

        df = pd.read_csv('lookup_data/tp_x.csv')

        if x in df['input'].values:
            ind = df[df['input'] == x].index[0]
            x_list = df.at[ind, 'output'].strip()

            y_lifgam = generator.generate_y_lifgam_Tp(y)
            
            for x in x_list.split('/'):
                print(f"{x} {y}")

        else:
            print('No value found')

        return
    
    if tag == "Tb":

        df = pd.read_csv('lookup_data/tb.csv')

        tagged_input = f'<{x}-{y}>Tb'

        if tagged_input in df['input'].values:
            ind = df[df['input'] == tagged_input].index[0]
            print(df.at[ind, 'output'].strip())

        else:
            print('No value found')

        return

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
                    # <akRa-pari>A2
                    case tag if tag == 'A2':

                        if y == 'pari':

                            x1 = generator.generate_x_root(x,lifgam, 3)
                            print(f'{x1} viparIwam vqwwam')

                        elif y == 'prawi':

                            x1 = generator.generate_x_root(x,lifgam, 6)
                            print(f'{x1} leSaH')
                            
                    
                    # For A4: <x-y>A4 => x{6} y’{6} समाहारः
                    # <sapwan-gafgam>A4
                    case tag if tag == 'A4':
                        x1 = generator.generate_x_root_A4(x,lifgam, 6)

                        y_list = generator.generate_y_root_A4(y, 6)

                        for y1, lifgam in y_list.items():
                            print(f"{x1} {y1} samAhAraH")

                    

                    # For A6: <x-y>A6 => x{6} y’{6} समाहारः
                    # <wri-muni>A6
                    case tag if tag == 'A6':
                        x1 = generator.generate_x_root_A6(x,lifgam, 6)

                        y_list = generator.generate_y_root_A6(y, 6)

                        for y1 in list(set(y_list)):
                            print(f"{x1} {y1} samAhAraH")

                    
                    # For A7: <x-y>A7 => y{6} x
                    # <pAre-gafgam>A7
                    case tag if tag == 'A7':
                        y_list = generator.generate_y_root_A7(y, 6)

                        for y1, lifgam in y_list.items():
                            print(f"{y1} {x}") 

                    
 

            ############################################
                       
            # For T<num>
            case tag if tag[0] == 'T' and tag[1].isdigit():

                # Getting vibhakti
                vibhakti = tag[1]

                if tag[1] == '7':
                    x1 = generator.generate_x_root_T7(x,lifgam, 7)

                    print(f"{x1} {y}")
                    
                else:
                    x1 = generator.generate_x_root(x,lifgam, vibhakti)

                    # For T2 to T6: <x-y>T(2:6) => x{(2:6)} y 
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

            # For Tds: <x-y>Tds => x{6;ba} y{6;ba}
            # <paFcan-gavam>Tds          
            case tag if tag == 'Tds':

                x1 = generator.generate_x_root_A4(x,lifgam, 6)

                y_list = generator.generate_y_root_Tds(y, 6)

                for y1 in list(set(y_list)):
                    print(f"{x1} {y1} samAhAraH")

            ############################################

            # For K<num>
            case tag if tag[0] == 'K' and tag[1].isdigit():
                match tag:

                    # For K1: <x-y>K1 => x{1} तत ् y{1} च
                    case tag if tag == 'K1':

                        x1 = generator.generate_x_root(x,lifgam, 1)

                        y_list = generator.generate_y_root_B(y, 1)

                        for y1, y_lifgam in y_list.items():
                            if lifgam == 'napuM' and y_lifgam == 'napuM':
                                print(f"{x1} ca waw {y1} ca")
                            elif lifgam == 'swrI' and y_lifgam == 'swrI':
                                print(f"{x1} ca asO {y1} ca")
                            elif lifgam == 'puM' and y_lifgam == 'puM':
                                print(f"{x1} ca asO {y1} ca")
        
                    
                    # For K2: <x-y>K2 => x{1} च y{1} च
                    case tag if tag == 'K2':
                        x1 = generator.generate_x_root(x,lifgam, 1)

                        y_list = generator.generate_y_root_B(y, 1)

                        for y1, y_lifgam in y_list.items():
                            if lifgam == 'napuM' and y_lifgam == 'napuM':
                                print(f"{x1} ca axaH {y1} ca")
                            elif lifgam == 'swrI' and y_lifgam == 'swrI':
                                print(f"{x1} ca asO {y1} ca")
                            elif lifgam == 'puM' and y_lifgam == 'puM':
                                print(f"{x1} ca asO {y1} ca")
                            

                    # For K3: <x-y>K3 => x{1}च असौ y{1} च
                    case tag if tag == 'K3':
                        x1 = generator.generate_x_root(x,lifgam, 1)

                        y_list = generator.generate_y_root_B(y, 1)

                        for y1, y_lifgam in y_list.items():
                            if lifgam == 'napuM' and y_lifgam == 'napuM':
                                print(f"{x1} ca asO {y1} ca")
                            elif lifgam == 'swrI' and y_lifgam == 'swrI':
                                print(f"{x1} ca asO {y1} ca")
                            elif lifgam == 'puM' and y_lifgam == 'puM':
                                print(f"{x1} ca asO {y1} ca")
                                

                    # For K4: <x-y>K4 => x{1} इव y{1}
                    case tag if tag == 'K4':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                                
                        y_list = generator.generate_y_root_B(y, 1)

                        for y1, y_lifgam in y_list.items():
                            if lifgam == 'napuM' and y_lifgam == 'napuM':
                                print(f"{x1} iva {y1}")
                            elif lifgam == 'swrI' and y_lifgam == 'swrI':
                                print(f"{x1} iva {y1}")
                            elif lifgam == 'puM' and y_lifgam == 'puM':
                                print(f"{x1} iva {y1}")
                             
                    
                    # For K5: <x-y>K5 => x{1} y{1} इव
                    case tag if tag == 'K5':
                        x1 = generator.generate_x_root(x,lifgam, 1)

                        y_list = generator.generate_y_root_B(y, 1)

                        for y1, y_lifgam in y_list.items():
                            if lifgam == 'napuM' and y_lifgam == 'napuM':
                                print(f"{x1} {y1} iva ")
                            elif lifgam == 'swrI' and y_lifgam == 'swrI':
                                print(f"{x1} {y1} iva ")
                            elif lifgam == 'puM' and y_lifgam == 'puM':
                                print(f"{x1} {y1} iva ")
                             

                    # For K6: <x-y>K6 => x{1} एव y{1}
                    case tag if tag == 'K6':
                        x1 = generator.generate_x_root(x,lifgam, 1)

                        y_list = generator.generate_y_root_B(y, 1)

                        for y1, y_lifgam in y_list.items():
                            if lifgam == 'napuM' and y_lifgam == 'napuM':
                                print(f"{x1} eva {y1}")
                            elif lifgam == 'swrI' and y_lifgam == 'swrI':
                                print(f"{x1} eva {y1}")
                            elif lifgam == 'puM' and y_lifgam == 'puM':
                                print(f"{x1} eva {y1}")
                             

                    # For K7: <x-y>K7 => x{1} इित y{1}
                    case tag if tag == 'K7':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                        y_list = generator.generate_y_root_B(y, 1)

                        for y1, y_lifgam in y_list.items():
                            if lifgam == 'napuM' and y_lifgam == 'napuM':
                                print(f"{x1} iwi {y1}")
                            elif lifgam == 'swrI' and y_lifgam == 'swrI':
                                print(f"{x1} iwi {y1}")
                            elif lifgam == 'puM' and y_lifgam == 'puM':
                                print(f"{x1} iwi {y1}")
                             

            ############################################## 
            case tag if tag[0] == 'B':

                match tag:

                    # <prApwa-uxakaH>Bs2
                    # For Bs2: <x-y>Bs2 => x{1} y{1} यत ्{g}{2}
                    case tag if tag[-2:] == 's2':
                        x1 = generator.generate_x_root_Bs3(x,lifgam, 1)
                        
                        #print(x1, y, 'in')
                        y_list = generator.generate_y_root_Bs2(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        #temp = {val: key for key, val in y_list.items()}
                        #y_list = {val: key for key, val in temp.items()}
                        for y1, y_lifgam in y_list.items():
                            #for y1, y_lifgam in y_list.items():
                                #print(x1, lifgam)
                                #print(y_lifgam[0])
                                if lifgam == y_lifgam[0]:
                                    if y_lifgam[1] == 'puM':
                                        z1 = 'yaM'
                                    elif y_lifgam[1] == 'swrI':
                                        z1 = 'yAM'
                                    elif y_lifgam[1] == 'napuM':
                                        z1 = 'yaw'
                                    print(f"{x1} {y1} {z1}")

                    # For Bs3: <x-y>Bs3 => x{1} y{1} येन/यया/येन
                    # <UDa-raWaH>Bs3
                    case tag if tag[-2:] == 's3':
                        x1 = generator.generate_x_root_Bs3(x,lifgam, 1)
                        #print(x1, lifgam)
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, y_lifgam in y_list.items():
                            #for y1, y_lifgam in y_list.items():
                                if lifgam == y_lifgam:
                                   
                                    if y_lifgam == 'puM':
                                        z1 = 'yena'
                                    elif y_lifgam == 'swrI':
                                        z1 = 'yayA'
                                    else:
                                        z1 = 'yena'
                                    print(f"{x1} {y1} {z1}")

                    # For Bs4: <x-y>Bs4 => x{1} y{1} यस्मै/यस्यै/यस्मै
                    # <xawwa-vaswrA>Bs4
                    case tag if tag[-2:] == 's4':
                        x1 = generator.generate_x_root_Bs4(x,lifgam, 1)
                        #print(x1,lifgam)
                        y_list = generator.generate_y_root_Bs2(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        #temp = {val: key for key, val in y_list.items()}
                        #y_list = {val: key for key, val in temp.items()}
                        for y1, y_lifgam in y_list.items():
                            #for y1, lifgam in y_list.items():
                                if lifgam == y_lifgam[0]:
                                    if y_lifgam[1] == 'puM':
                                        z1 = 'yasmE'
                                    elif y_lifgam[1] == 'swrI':
                                        z1 = 'yasyE'
                                    else:
                                        z1 = 'yasmE'
                                    print(f"{x1} {y1} {z1}")

                    # For Bs5: <x-y>Bs5 => x{1} y{1} यस्मात्/यस्याः/यस्मात्
                    # <apagawa-jIvaH>Bs5
                    case tag if tag[-2:] == 's5':
                        x1 = generator.generate_x_root_Bs3(x,lifgam, 1)
                        y_list = generator.generate_y_root_Bs2(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        #temp = {val: key for key, val in y_list.items()}
                        #y_list = {val: key for key, val in temp.items()}

                        for y1, y_lifgam in y_list.items():
                            #for y1, lifgam in y_list.items():
                                    if lifgam == y_lifgam[0]:
                                        if y_lifgam[1] == 'puM':
                                            z1 = 'yasmAw'
                                        elif y_lifgam[1] == 'swrI':
                                            z1 = 'yasyAH'
                                        else:
                                            z1 = 'yasmAw'
                                        print(f"{x1} {y1} {z1}")

                    # For Bs6: <x-y>Bs6 => x{1} y{1} यस्य/यस्याः/यस्य
                    # <pIwa-ambaraH>Bs6
                    case tag if tag[-2:] == 's6':
                        x1 = generator.generate_x_root_Bs3(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root_Bs2(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        #temp = {val: key for key, val in y_list.items()}
                        #y_list = {val: key for key, val in temp.items()}
                        for y1, y_lifgam in y_list.items():
                            #for y1, lifgam in y_list.items():
                                    if y_lifgam[0] == lifgam:
                                        if y_lifgam[1] == 'puM':
                                            z1 = 'yasya'
                                        elif y_lifgam[1] == 'swrI':
                                            z1 = 'yasyAH' 
                                        else:
                                            z1 = 'yasya'

                                        print(f"{x1} {y1} {z1}")
                             

                    # For Bs7: <x-y>Bs7 => x{1} y{1} यस्मिन्/यस्याम्/यस्मिन्
                    # <nikRipwa-viSvAsaH>Bs7
                    case tag if tag[-2:] == 's7':
                        x1 = generator.generate_x_root_Bs3(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, y_lifgam in y_list.items():
                                if lifgam == y_lifgam:
                                    if y_lifgam == 'puM':
                                        z1 = 'yasmin'
                                    elif y_lifgam == 'swrI':
                                        z1 = 'yasyAm'
                                    else:
                                        z1 = 'yasmin'
                                    print(f"{x1} {y1} {z1}") 

                    # For Bsd: <x-y>Bsd => x{6} च y{6} च यदन्तरालम्
                    # <pUrva-uwwarA>Bsd
                    case tag if tag[-2:] == 'sd':
                        x1 = generator.generate_x_root(x,lifgam, 6)
                            
                        y_list = generator.generate_y_root_Bs4(y, 6)

                        for y1 in list(set(y_list)):
                            print(f"{x1} ca {y1} ca yaxanwarAlam")

                    # For Bsp: <x-y>Bsp => x{3} च y{3} च प्रहृत्य इदम् युद्धम् प्रवृत्तम्
                    # <xaNdA-xaNdI>Bsp
                    case tag if tag[-2:] == 'sp':
                        x1 = generator.generate_x_root(x,lifgam, 3)
                            
                        y_list = generator.generate_y_root_B(y, 3)

                        for y1 in list(set(y_list)):
                            print(f"{x1} ca {y1} ca prahqwya ixam yuxXam pravqwwam")
                        

                    # For Bsg: <x-y>Bsg => x{7}-y{7} गृहित्वा इदम् युद्धम् प्रवृत्तम्
                    # <keSA-keSi>Bsg
                    case tag if tag[-2:] == 'sg':
                        x1 = generator.generate_x_root(x,lifgam, 7)
                            
                        y_list = generator.generate_y_root(y, 7)

                        for y1 in list(set(y_list)):
                            print(f"{x1} {y1} gqhiwvA ixam yuxXam pravqwwam")

                    # For Bsmn: <x-y>Bsmn => न विद्यते y{1} यस्य/यस्याः/यस्य
                    # <a-puwraH>Bsmn
                    case tag if tag[-3:] == 'smn':
                        x1 = generator.generate_x_root_Bs4(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root_Bs2(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, y_lifgam in y_list.items():
                                if lifgam == y_lifgam:
                                    if y_lifgam == 'puM':
                                        z1 = 'yasya'
                                    elif y_lifgam == 'swrI':
                                        z1 = 'yasyAH'
                                    else:
                                        z1 = 'yasya'
                                    print(f"na vixyawe {y1} {z1}") 

                    # For Bss: <x-y>Bss = > x{1} वा y{1} यस्य/यस्याः/यस्य
                    # <wri-cawuraH>Bss
                    # A6
                    case tag if tag[-2:] == 'ss':
                        x1 = generator.generate_x_root_A6(x,lifgam, 1)
                        y_list = generator.generate_y_root_Bs2(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        #temp = {val: key for key, val in y_list.items()}
                        #y_list = {val: key for key, val in temp.items()}
                        for y1, y_lifgam in y_list.items():
                                    if y_lifgam[0] == lifgam: 
                                        if y_lifgam[1] == 'puM':
                                            z1 = 'yasya'
                                        elif y_lifgam[1] == 'swrI':
                                            z1 = 'yasyAH'
                                        else:
                                            z1 = 'yasya'
                                        print(f"{x1} vA {y1} {z1}") 

                    # For Bsu: <x-y>Bsu => x{1} इव y{1} यस्य/यस्याः/यस्य
                    # <canxra-muKI>Bsu
                    case tag if tag[-2:] == 'su':
                        x1 = generator.generate_x_root(x,lifgam, 1)
                            
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, y_lifgam in y_list.items():
                                if lifgam == y_lifgam:
                                    if y_lifgam == 'puM':
                                        z1 = 'yasya'
                                    elif y_lifgam == 'swrI':
                                        z1 = 'yasyAH'
                                    else:
                                        z1 = 'yasya'
                                    print(f"{x1} iva {y1} {z1}")

                    # For Bv: <x-y>Bv => x y{1} यस्य/यस्याः/यस्य
                    # <kaNTe-kAlaH>Bv
                    # <canxra-SeKaraH>Bv
                    case tag if tag[-1:] == 'v':

                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, y_lifgam in y_list.items():
                                if lifgam == y_lifgam:
                                    if y_lifgam == 'puM':
                                        z1 = 'yasya'
                                    elif y_lifgam == 'swrI':
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
                    # <sa-puwraH>BvS
                    case tag if tag[-2:] == 'vS':
                        y_list = generator.generate_y_root(y, 3)

                        for y1 in list(set(y_list)):
                            print(f"{y1} saha")

                    # For BvU: <x-y>BvU => x{6} इव y यस्य/यस्याः/यस्य
                    # <uRtra-muKaH>BvU
                    case tag if tag[-2:] == 'vU':
                        x1 = generator.generate_x_root(x,lifgam, 6)
                            
                        y_list = generator.generate_y_root_B(y, 1)
                        # Remove duplicate values in dictionary
                        # Using dictionary comprehension
                        temp = {val: key for key, val in y_list.items()}
                        y_list = {val: key for key, val in temp.items()}
                        for y1, y_lifgam in y_list.items():
                                if lifgam == y_lifgam:
                                    if y_lifgam == 'puM':
                                        z1 = 'yasya'
                                    elif y_lifgam == 'swrI':
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
                            y_roots = generator.generate_y_root_Ds(y_part, 1)
                            y_roots = list(set(y_roots))  # deduplication
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
