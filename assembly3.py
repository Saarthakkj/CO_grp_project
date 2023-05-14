
def multiply(i):
    ans="00110_00_"
    ans+=register(i[1])
    ans+="_"
    ans+=register(i[2])
    ans+="_"
    ans+=register(i[3])
    return ans

def divide(i):
    ans="00111_00000"
    ans+=register(i[1])
    ans+="_"
    ans+=register(i[2])
    return ans

def right_shift(i):
    ans="01000_0_"
    ans+=register(i[1])
    ans+="_"
    imm=i[2][1:]
    #print("imm: ",imm)
    ans+=integer_to_binary_with_padding(imm)
    return ans

def left_shift(i):
    ans="01001_0_"
    ans+=register(i[1])
    ans+="_"
    imm=i[2][1:]
    #print("imm: ",imm)
    ans+=integer_to_binary_with_padding(imm)
    return ans

def exclusive_OR(r1,r2,r3):
    if r1 in reg_lst and r2 in reg_lst and r3 in reg_lst:
        return "01010_00_"+register(r1)+register(r2)+register(r3)

def Or(r1,r2,r3):
    if r1 in reg_lst and r2 in reg_lst and r3 in reg_lst:
        return "01011_00_"+register(r1)+register(r2)+register(r3)

def And(r1,r2,r3):
     if r1 in reg_lst and r2 in reg_lst and r3 in reg_lst:
        return "01100_00_"+register(r1)+register(r2)+register(r3)

def invert(r1,r2):
    if r1 in reg_lst and r2 in reg_lst:
        return "01101_00000_"+register(r1)+register(r2)

def compare(r1,r2):
    if r1 in reg_lst and r2 in reg_lst:
        return "01110_00000_"+register(r1)+register(r2)

def unconditional_jump(instruction,label_name_dictionary,data):
    k=key(instruction)
    taking_input_in_label_dictionary(instruction[k],label_name_dictionary,data)
    return "01111_0000_"+label_name_dictionary[instruction[k]]

def jump_if_less_than(instruction,label_name_dictionary,data):
    k=key(instruction)
    taking_input_in_label_dictionary(instruction[k],label_name_dictionary,data)
    return "11100_0000_"+label_name_dictionary[instruction[k]]

def jump_if_greater_than(instruction,label_name_dictionary,data):
    k=key(instruction)
    taking_input_in_label_dictionary(instruction[k],label_name_dictionary,data)
    return "11101_0000_"+label_name_dictionary[instruction[k]]

def jump_if_equal(instruction,label_name_dictionary,data):
    k=key(instruction)
    taking_input_in_label_dictionary(instruction[k],label_name_dictionary,data)
    return "11111_0000_"+label_name_dictionary[instruction[k]]

def halt():
    return "11010_00000000000"



# -------------------------calling all the different functions-----------
