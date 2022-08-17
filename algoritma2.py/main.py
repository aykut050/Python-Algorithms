import re

pattern = '[\W_]+'
replacement = ''

def invert_string(string):
    accurate_string = ""
    string_length = len(string)

    while string_length > 0:
        accurate_string += string[string_length-1]
        string_length -= 1

    return accurate_string

def fix_text(input):
    result = ""
    input_splitted_array = input.split(" ")
    
    for input_splitted_item in input_splitted_array:
        if input_splitted_item[0] == "(":
            result += input_splitted_item + " "
        else:
            result += invert_string(input_splitted_item) + " "

    return result

input = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon " 
        ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc " 
        "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif " 
        "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec " 
        "(and) nrae a egral enutrof (from) ).gnitirw")

print(fix_text(input))