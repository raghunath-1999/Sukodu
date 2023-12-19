# import csv
# import math

# import copy

import csv
import math
import time
import numpy as np
import copy
print("1 – brute force search")
print("2 – Constraint Satisfaction Problem back-tracking search,")
print("3 – CSP with forward-checking and MRV heuristics,")
print("4 – test if the completed puzzle is correct.")

# getting inputs and verifying conditions

user_ip=input("enter the mode and the filename with a space in between")
ip_arr=user_ip.split(" ")

if(((ip_arr[1].split('.')[0][8:9]) not in ['1','2','3','4','5','6','7'] )):
    print("wrong input")
    exit()
if(((ip_arr[1].split('.')[0][0:8])!="testcase") ):
    print("wrong input")
    exit()
if(ip_arr[1].split('.')[1]!="csv"):
    print("wrong input add csv")
    exit()
if((len(ip_arr)!=2) and (int(ip_arr[1].split('.')[0][8:9])<0 and int(ip_arr[1].split('.')[0][8:9])>7) and (ip_arr[1].split('.')[1]!="csv") ):
    print("wrong input")
    exit()
print(ip_arr)


#------------------------check_completeness----------------
# ----------------------------------------
# a overall function to check the completeness
def Cond_sudf(sud_bd):
        
        const_row={}
        const_col={}
        const_sq={}
        # global X_val_idx
        ps=[]
        for y in range(len(sud_bd)):
            for x in range(len(sud_bd[y])):
                if(sud_bd[y][x]!='X'):
                    if(y in const_row.keys()):
                        const_row[y].add(sud_bd[y][x])
                    else:
                        const_row[y]=set(sud_bd[y][x])
                    if(x in const_col.keys()):
                        const_col[x].add(sud_bd[y][x])
                    else:
                        const_col[x]=set(sud_bd[y][x])
                    if(y in const_row.keys()):
                        const_row[y].add(sud_bd[y][x])
                    else:
                        const_row[y]=set(sud_bd[y][x])
                    box_x=math.floor(x/3)
                    box_y=math.floor(y/3)
                    box_sq=box_x+box_y*3
                    if(box_sq in const_sq.keys()):
                        const_sq[box_sq].add(sud_bd[y][x])
                    else:
                        const_sq[box_sq]=set(sud_bd[y][x])
                # else:
                    # X_val_idx.append((x,y))
                        
        rw=0
        cl=0
        sq=0
        #checking row wise
        arr_check=[1,2,3,4,5,6,7,8,9]
        for rr in const_row:
            tp=list(const_row[rr])
            tp1=[]
            for v1 in tp:
                tp1.append(int(v1))
            tp1.sort()
            if(tp1==arr_check):
                rw=rw+1
        #checking column wise
        for cc in const_col:
            tp=list(const_col[cc])
            tp1=[]
            for v1 in tp:
                tp1.append(int(v1))
            tp1.sort()
            if(tp1==arr_check):
                cl=cl+1
        #checking sub square wise
        for cc in const_sq:
            tp=list(const_sq[cc])
            tp1=[]
            for v1 in tp:
                tp1.append(int(v1))
            tp1.sort()
            if(tp1==arr_check):
                sq=sq+1
        if(rw==9 and cl==9 and sq==9):
            return True
        else:
            return False

#-----------------check completeness over--

#----------------------------------------brute force--------
if(ip_arr[0]=='1'):
    csv_file_path = ip_arr[1] #3


    with open(csv_file_path, 'r',encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]



    data = [[str(cell) if cell.isdigit() else cell for cell in row] for row in data]

    sud_bd=data
    def print_sudoku():
        for i in sud_bd:
            print(i)
    const_row={}
    const_col={}
    const_sq={}
    X_val_idx=[]
    ps=[]
    x_ran=np.arange(1,10)
    for i in x_ran:
        ps.append(str(i))
    
    #brute force recursion
    def brute_frce(X_val_idx,sud_bd):
        global ps
        global count_nodes
        count_nodes=count_nodes+1
        #idea is to get info about the missing values ie Xs in the array and checking possiblities untill all gets filled up
        if(len(X_val_idx)==0 ):
            # at each bottom most root of the tree, a full condition is checked and stopped if it is true
            if(Cond_sud(sud_bd)):
                return True,sud_bd
            else:
                return False,sud_bd
        
        
        # print(X_val_idx)
        x,y=X_val_idx[0]
        
        box_x=math.floor(x/3)
        box_y=math.floor(y/3)
        box_sq=box_x+box_y*3
        # checking all possible numbers from 1 to 9
        for ele in ps:
            sud_bd_for_search = copy.deepcopy(sud_bd)
            
            
            
            sud_bd_for_search[y][x] = ele
            X_val_idx.pop(0)
            res,sol_bd=brute_frce(X_val_idx,sud_bd_for_search)
            if(res):
                return True,sol_bd
            else: 
                sud_bd_for_search[y][x] = 'X'

                X_val_idx.insert(0, (x, y))
        return False,sud_bd
            
            
    #constrain checking as mentioned above,. included this to prevent the unwanted output
    def Cond_sud(sud_bd):
        
        const_row={}
        const_col={}
        const_sq={}
        global X_val_idx
        ps=[]
        for y in range(len(sud_bd)):
            for x in range(len(sud_bd[y])):
                if(sud_bd[y][x]!='X'):
                    if(y in const_row.keys()):
                        const_row[y].add(sud_bd[y][x])
                    else:
                        const_row[y]=set(sud_bd[y][x])
                    if(x in const_col.keys()):
                        const_col[x].add(sud_bd[y][x])
                    else:
                        const_col[x]=set(sud_bd[y][x])
                    if(y in const_row.keys()):
                        const_row[y].add(sud_bd[y][x])
                    else:
                        const_row[y]=set(sud_bd[y][x])
                    box_x=math.floor(x/3)
                    box_y=math.floor(y/3)
                    box_sq=box_x+box_y*3
                    if(box_sq in const_sq.keys()):
                        const_sq[box_sq].add(sud_bd[y][x])
                    else:
                        const_sq[box_sq]=set(sud_bd[y][x])
                else:
                    X_val_idx.append((x,y))
                        
        rw=0
        cl=0
        sq=0
        arr_check=[1,2,3,4,5,6,7,8,9]
        for rr in const_row:
            tp=list(const_row[rr])
            tp1=[]
            for v1 in tp:
                tp1.append(int(v1))
            tp1.sort()
            if(tp1==arr_check):
                rw=rw+1
        for cc in const_col:
            tp=list(const_col[cc])
            tp1=[]
            for v1 in tp:
                tp1.append(int(v1))
            tp1.sort()
            if(tp1==arr_check):
                cl=cl+1
        for cc in const_sq:
            tp=list(const_sq[cc])
            tp1=[]
            for v1 in tp:
                tp1.append(int(v1))
            tp1.sort()
            if(tp1==arr_check):
                sq=sq+1
        if(rw==9 and cl==9 and sq==9):
            return True
        else:
            return False
            
                
            
    # taking information about the vaccant spots in the sudoku board         
    X_val_idx=[]   
    for y in range(len(sud_bd)):
        for x in range(len(sud_bd[y])):
            if(sud_bd[y][x]=='X'):     
                X_val_idx.append((x,y))  
    # print(X_val_idx)
    # res11=Cond_sud(sud_bd)
    # print(res11)
    # brute_frce(sud_bd)
    count_nodes=0
    time_start=time.time()
    res1,soll_bd=brute_frce(X_val_idx,sud_bd)
    time_stop=time.time()
    print("total time taken",time_stop-time_start)
    print("nodes explored",count_nodes)
    if(Cond_sudf(soll_bd)):
        for i in soll_bd:
            print(i)
    else:
        print("ERROR: This is NOT a solved Sudoku puzzle")
        
        
        


# ----------------------- *****---------brute completed------


#------constrain satisfaction probelm mode back tracking 2 ---------------------

if(ip_arr[0]=='2'):
    const_row={}
    const_col={}
    const_sq={}
    X_val_idx=[]
    ps=[]


    x_ran=np.arange(1,10)
    for i in x_ran:
        ps.append(str(i))
    # recursive building of the tree with taking aacount of all possible constraints of the cell
    def build_tree(X_val_idx,ps,const_row,const_col,const_sq,sud_bd):
        global count_node
        count_node=count_node+1
        if(len(X_val_idx)==0):
            return True,sud_bd
        #sub box coordinates
        x,y=X_val_idx[0]
        box_x=math.floor(x/3)
        box_y=math.floor(y/3)
        box_sq=box_x+box_y*3
        #checking all possible elements from 1 to 9
        for ele in ps:
            if (ele not in const_row.setdefault(y, set())) and (ele not in const_col.setdefault(x, set())) and (ele not in const_sq.setdefault(box_sq, set())):
                sud_bd_for_search = copy.deepcopy(sud_bd)

                
                sud_bd_for_search[y][x] = ele
                #checking if a element is already in the constraint dictionary 
                # row wise
                const_row_for_search= copy.deepcopy(const_row)
                if(y in const_row_for_search.keys()):
                    const_row_for_search[y].add(ele)
                else:
                    const_row_for_search[y]=set(ele)
                const_col_for_search = copy.deepcopy(const_col)
                #checking if a element is already in the constraint dictionary 
                # columns wise
                if(x in const_col_for_search.keys()):
                    const_col_for_search[x].add(ele)
                else:
                    const_col_for_search[x]=set(ele)
                    
                const_sq_for_search = copy.deepcopy(const_sq)
                #checking if a element is already in the constraint dictionary 
                # sub square wise
                if(box_sq in const_sq_for_search.keys()):
                    const_sq_for_search[box_sq].add(ele)
                else:
                    const_sq_for_search[box_sq]=set(ele)
                X_val_idx.pop(0)
                res,sol_bd=build_tree(X_val_idx,ps,const_row_for_search,const_col_for_search,const_sq_for_search,sud_bd_for_search)
                if(res):
                    return True,sol_bd
                else: 
                    sud_bd_for_search[y][x] = 'X'
                    const_row_for_search[y]=const_row_for_search[y]-set(ele)
                    const_col_for_search[x]=const_col_for_search[x]-set(ele)
                    const_sq_for_search[box_sq]=const_sq_for_search[box_sq]-set(ele)
                    X_val_idx.insert(0, (x, y))
                    
                
                
        return False,sud_bd

    #initializing vaccant set and starting the game
    def csp_bt_game():
        global sud_bd
        global count_node
        global const_row,const_col,const_sq,X_val_idx,ps
        for y in range(len(sud_bd)):
            for x in range(len(sud_bd[y])):
                if(sud_bd[y][x]!='X'):
                    # vals_in_rows[y] = vals_in_rows.get(y, set()) | {sudo_board[y][x]}
                    if(y in const_row.keys()):
                        const_row[y].add(sud_bd[y][x])
                    else:
                        const_row[y]=set(sud_bd[y][x])
                    if(x in const_col.keys()):
                        const_col[x].add(sud_bd[y][x])
                    else:
                        const_col[x]=set(sud_bd[y][x])
                    if(y in const_row.keys()):
                        const_row[y].add(sud_bd[y][x])
                    else:
                        const_row[y]=set(sud_bd[y][x])
                    box_x=math.floor(x/3)
                    box_y=math.floor(y/3)
                    box_sq=box_x+box_y*3
                    if(box_sq in const_sq.keys()):
                        const_sq[box_sq].add(sud_bd[y][x])
                    else:
                        const_sq[box_sq]=set(sud_bd[y][x])
                else:
                    X_val_idx.append((x,y))
        
        
        val,bd= build_tree(X_val_idx,ps,const_row,const_col,const_sq,sud_bd)
        return val,bd



        



    csv_file_path = ip_arr[1]


    with open(csv_file_path, 'r',encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]



    data = [[int(cell) if cell.isdigit() else cell for cell in row] for row in data]

    print("Board")
    print(np.array(data))
    print("\n")
    import time


    sud_bd=np.array(data)
    count_node=0
    time_start=time.time()
    val,bd=csp_bt_game()
    time_stop=time.time()
    print("nodes explored",count_node)
    print("time_taken",time_stop-time_start)

    print("solution")
    if(Cond_sudf(bd)):
        for q in bd:
            print(q)
    else:
        print("ERROR: This is NOT a solved Sudoku puzzle")



# --------------------csp backtracking completed-----------------------

#-------------csp minimum value heuristics----------------------

if(ip_arr[0]=='3'):
    
    csv_file_path = ip_arr[1]


    with open(csv_file_path, 'r',encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]



    data = [[str(cell) for cell in row] for row in data]
    sud_bd=np.array(data)

    #this function gives the possible values for a vaccant spot
    def possibilities(i,j):
            global sud_bd
            if(sud_bd[i][j]!='X'):
                return False
            all_num=[]
            #rows
            for k in range(1,10):
                all_num.append(str(k))
            
            all_num=set(all_num)
                
            
            temp_dis=set(sud_bd[i])
            all_num=all_num-temp_dis
            #columns
            temp_col=[]
            for ele in range(0,9):
                temp_col.append(sud_bd[ele][j])
            all_num=all_num-set(temp_col)
            
            box_i=math.floor(i/3)
            box_j=math.floor(j/3)
            box_i=box_i*3
            box_j=box_j*3
            #sub square
            square_bd=[]
            for ia in range(box_i,box_i+3):
                xps=[]
                for ja in range(box_j,box_j+3):
                    xps.append(sud_bd[ia][ja])
                square_bd.append(xps)
            
                    
            temp_box=[]
            for r in square_bd:
                for c in r:
                    temp_box.append(c)
            temp_box=set(temp_box)
            all_num=all_num-temp_box
            return list(all_num) 
    # getting constrints based on the possibilities function above

    def check_broad(sud_bd,vac_cell,csp_val):
        search_csp_val_n=copy.deepcopy(csp_val)
        for ele in vac_cell:
            x=ele[0]
            y=ele[1]

            val_ele=search_csp_val_n[(x,y)]
            
            for k in range(0,len(sud_bd)):
                if(sud_bd[x][k] in val_ele):
                    val_ele.remove(sud_bd[x][k])
                if(sud_bd[k][y] in val_ele):
                    val_ele.remove(sud_bd[k][y])
            box_x=math.floor(x/3)*3
            box_y=math.floor(y/3)*3
            
            for i in range(box_x, box_x + 3):
                for j in range(box_y, box_y + 3):
                    if sud_bd[i][j] in val_ele:
                        val_ele_temp=set(val_ele)
                        val_ele_temp=val_ele_temp-set(sud_bd[i][j])
                        val_ele=copy.deepcopy(list(val_ele_temp))
                        # val_ele=copy.deepcopy(val_ele_temp)
                        # val_ele.remove(sud_bd[i][j])
            
            search_csp_val_n[(x,y)]=set(val_ele)
        return search_csp_val_n


    #after getting the constraints checking the mrv
    def csp_assign(s_bd,vac_cell,csp_val):
        global count_node
        global zeroArray
        count_node=count_node+1
        if(vac_cell==[]):
            return s_bd
        
        lest_cnt_val=vac_cell[0]
        min_len=len(csp_val[lest_cnt_val])

        for i in vac_cell:
            val_i=csp_val[i]
            
            if(len(val_i)<min_len):
                lest_cnt_val=i
                min_len=len(val_i)
    
        possible_val=csp_val[lest_cnt_val]

        possible_val1=tuple(possible_val)
        for j in possible_val1:
            search_board=copy.deepcopy(s_bd)
            cor_x,cor_y=lest_cnt_val[0],lest_cnt_val[1]
            search_board[cor_x][cor_y]=j
            search_vac_cell=copy.deepcopy(vac_cell)
            search_vac_cell.remove(lest_cnt_val)
            # search_vac_cell_tp=set(search_vac_cell)-set(lest_cnt_val)
            # search_vac_cell=copy.deepcopy(list(search_vac_cell_tp))
            csp_val[(lest_cnt_val)].remove(j)
            search_csp_val_n=check_broad(search_board,search_vac_cell,csp_val)
            #checking for the least mrv
            # print("pls ignore the warning, arises because of comparing 2 diff multi dimensional array")
            cntr=0
            for ele in search_vac_cell:
                temp_ele_val=search_csp_val_n[ele]
                if(len(temp_ele_val)>0):
                    cntr=cntr+1
            if(cntr==len(search_vac_cell)):
                ans_bd=csp_assign(search_board,search_vac_cell,search_csp_val_n)
                if ans_bd is not zeroArray:
                    return ans_bd

            
        return zeroArray
            
            
        
                
        





    def csp_mrv_fc():
        global sud_bd
        global count_node
        
        unknown=[]
        for i,row in enumerate(sud_bd):
            for j,col in enumerate(row):
                if(col=='X'):
                    unknown.append((i,j))
        csp_val={}

        for i in unknown:
            
            csp_val[i]=possibilities(i[0],i[1])
            if(csp_val[i]==False):
                print("stp")
                exit()
        time_start=time.time()
        sol_bd=csp_assign(sud_bd,unknown,csp_val)
        time_stop=time.time()
        print("time taken",time_stop-time_start)
        
        print("number of nodes explored",count_node)
        if(sol_bd==zeroArray):
            print("ERROR: This is NOT a solved Sudoku puzzle")
        else:    
            for row in sol_bd:
                print(row)

    zeroArray = [[0 for i in range(9)] for i in range(9)]
        
        
    count_node=0   

    csp_mrv_fc()

# ------------------------csp_mrv----------completed


#-------------------------------board check

if(ip_arr[0]=='4'):
    
    csv_file_path = ip_arr[1]


    with open(csv_file_path, 'r',encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]



    data = [[str(cell) for cell in row] for row in data]
    sud_bd=np.array(data)
    if(Cond_sudf(sud_bd)==True):
        print("solved")
    else:
        print("unsolved")