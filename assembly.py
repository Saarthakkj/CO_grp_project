def input():
# ------------------------------------taking input from the file and storing it in final data-----------------------------------------
    f=open("example.txt",'r')
    data=f.readlines()
    l1=[]
    l2=[]
    no_of_lines=0
    data_for_error_function_dic={}
    data_for_error_function_list=[]
    key=0
    final_data=[]
    var_data=[]
    var_dic={}

    for i in data:
        l1.append(i.split())
# --------------------------------------data for error function-------------------------------------------------------------------
    for i in l1:
        if(i!=[]):
            
            data_for_error_function_list.append(i)    #dictionary of all the data with line number
            data_for_error_function_dic[key]=i    #list of all the data
            key+=1

# --------------------------------------------------data for all other funtions----------------------------------------------
    for i in l1:
        if((i!=[]) and i[0]!='var'):
            final_data.append(i)
            no_of_lines+=1

    for i in l1:
        if(i[0]=="var"):
            var_data.append(i[1])
    k=0
    for i in var_data:
        k=k+1
        var_dic[i]=str(format((no_of_lines+k-1),'b')).rjust(7,'0')

    f.close()
    return final_data,no_of_lines-1,var_dic,data_for_error_function_dic,data_for_error_function_list















# I have created all_ISA, register, variable, and label lists. Now u guys have to write the code for the errors.


def error(data_for_error_function_dic,data_for_error_function_list):
    # -------------------------------------------------------write the error code here------------------------------------------------------
    all_isa=["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
    reg_lst = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
    var_list=[]#list for variables
    label_list=[]#list for lables

    for i in data_for_error_function_list:
        if(i[0]=="var"):
            var_list.append(i[1])
    
    print()
    print("variable list",var_list)

    for i in data_for_error_function_list:
        if((i[0])[-1]==":"):
            label_list.append(i[0][:len(i)+1])
    print()
    print("label list",label_list)
    print()

















# --------------------------creating a list of all registers-------------------------
reg_lst = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
