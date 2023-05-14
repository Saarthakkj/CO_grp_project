def calling_other_functions(data,no_of_lines,label_name_dictionary,var_dic):
    for i in data:
        print(i)
        if(i[0]=="add"):
            print(addition(i[1], i[2], i[3]))
        elif(i[0]=="sub"):
            print(subtraction(i[1], i[2], i[3]))
        elif(i[0]=="mov" and (i[2])[0]=="$"):
            print(move_immediate(i[1], i[2]))
        elif(i[0]=="mov" and (i[2])[:1]=="R"):
            print(move_register(i[1], i[2]))
        elif(i[0]=="ld"):
            print(load(i,var_dic))
        elif(i[0]=="st"):
            print(store(i,var_dic))
        elif(i[0]=="mul"):
            print(multiply(i))
        elif(i[0]=="div"):
            print(divide(i))
        elif(i[0]=="rs"):
            print(right_shift(i))
        elif(i[0]=="ls"):
            print(left_shift(i))
        elif(i[0]=="xor"):
            print(exclusive_OR(i[1], i[2], i[3]))
        elif(i[0]=="or"):
            print(Or(i[1], i[2], i[3]))
        elif(i[0]=="and"):
            print(And(i[1], i[2], i[3]))
        elif(i[0]=="not"):
            print(invert(i[1], i[2]))
        elif(i[0]=="cmp"):
            print(compare(i[1], i[2]))
        elif(i[0]=="jmp"):
            print(unconditional_jump(i,label_name_dictionary,data))
        elif(i[0]=="jlt"):
            print(jump_if_less_than(i,label_name_dictionary,data))
        elif(i[0]=="jgt"):
            print(jump_if_greater_than(i,label_name_dictionary,data))
        elif(i[0]=="je"):
            print(jump_if_equal(i,label_name_dictionary,data))
        elif(i[0]=="hlt"):
            print(halt())
        else: 
            if(i[1]=="add"):
                print(addition(i[2], i[3], i[4]))
            elif(i[1]=="sub"):
                print(subtraction(i[2], i[3], i[4]))
            elif(i[1]=="mov" and (i[2])[0]=="$"):
                print(move_immediate(i[1], str(bin(int(i[2][1:])))[2:]))
            elif(i[1]=="mov" and (i[2])[:1]=="R"):
                print(move_register(i[2], i[3]))
            elif(i[1]=="ld"):
                print(load(i,var_dic))
            elif(i[1]=="st"):
                print(store(i,var_dic))
            elif(i[1]=="mul"):
                print(multiply(i))
            elif(i[1]=="div"):
                print(divide(i))
            elif(i[1]=="rs"):
                print(right_shift(i))
            elif(i[1]=="ls"):
                print(left_shift(i))
            elif(i[1]=="xor"):
                print(exclusive_OR(i[2], i[3], i[4]))
            elif(i[1]=="or"):
                print(Or(i[2], i[3], i[4]))
            elif(i[1]=="and"):
                print(And(i[2], i[3], i[4]))
            elif(i[1]=="not"):
                print(invert(i[2], i[3]))
            elif(i[1]=="cmp"):
                print(compare(i[2], i[3]))
            elif(i[1]=="jmp"):
                print(unconditional_jump(i,label_name_dictionary,data))
            elif(i[1]=="jlt"):
                print(jump_if_less_than(i,label_name_dictionary,data))
            elif(i[1]=="jgt"):
                print(jump_if_greater_than(i,label_name_dictionary,data))
            elif(i[1]=="je"):
                print(jump_if_equal(i,label_name_dictionary,data))
            elif(i[1]=="hlt"):
                print(halt())

       
        


# ---------------------------------------------------------------main---------------------------------------------------------
def main():
    label_name_dictionary={}
    data , no_of_lines,var_dic,data_for_error_function_dic,data_for_error_function_list=input()#here data doesn't contain "var" list
    print("data    ",data)
    print()
    print("data for error dic   ",data_for_error_function_dic)
    print()
    print("data for error list   ",data_for_error_function_list)
    error(data_for_error_function_dic,data_for_error_function_list)
    calling_other_functions(data,no_of_lines,label_name_dictionary,var_dic)
    print(label_name_dictionary)
    print(var_dic)
    # print("var ",variable("var1",var_dic))
if __name__ == "__main__":
    main()
