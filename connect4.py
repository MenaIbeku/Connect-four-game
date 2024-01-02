# Author   : Mena Ibeku
# Email    : cibeku@umass.edu
# Spire ID : 34151261
def make_empty_board(nrows,ncols):
    empty_list=[]
    for i in range(nrows):
        dots='.'*ncols
        empty_list.append(dots)
    return empty_list

    

def print_board(list_of_strings):
    for i in range(len(list_of_strings)):
        new_str=""
        for string1 in range(len(list_of_strings[i])):
            one_charact=list_of_strings[i][string1]
            if one_charact=='X':
                new_str+=' X '
            elif one_charact=='O':
                new_str+=' O '
            else:
                new_str+='   '
            
            if string1<((len(list_of_strings[i]))-1):
                new_str+='|'
        print(new_str)
        if i < len(list_of_strings)-1:
            print("---+" * (len(list_of_strings[i])-1)+"---")



def verify_board(list_strings):
    x_string=0
    o_string=0
    for i in range(len(list_strings)):
        for strings in range(len(list_strings[i])):
            if list_strings[i][strings]=="X":
                x_string+=1
                if i<len(list_strings)-1:
                    if (list_strings[i+1][strings]=='.') and (i!=-1) :
                        return False
            elif list_strings[i][strings]=='O':
                o_string+=1
                if i<len(list_strings)-1:
                    if(list_strings[i+1][strings]=='.') and (i!=-1) :
                        return False
    if ((x_string - o_string)<2) or ((o_string-x_string)<2):
        return True
    else:
        return False


def verify_move(list_strings,int_index):
    for i in range(len(list_strings)):
        count=0
        for strings in range(len(list_strings[i])):
            count+=1
            if (strings==int_index):
                if (list_strings[i][strings]=='.'):
                    return True
                elif (list_strings[i][strings]=='X' or list_strings[i][strings]=='O'):
                    return False
    if (int_index<0) or (int_index>=count):
        return False

               



def update_board(list_string,int_index,player_disc):
    for i in range(len(list_string)-1,-1,-1):
        for string1 in range(len(list_string[i])):
            if string1==int_index:
                if list_string[i][string1]==".":
                    new_list=list(list_string[i])
                    new_list[string1]=player_disc
                    list_string[i]="".join(new_list)
                    return list_string 

                
def has_won(list_string,int_index):
    
    row_top=0
    rows=len(list_string)
    disc=0
    
    for i in range(len(list_string)):
        if list_string[i][int_index]=='X' or list_string[i][int_index]=='O':
               disc=list_string[i][int_index]
               row_top=i
               break
        
    if rows-row_top>=4:
        if list_string[row_top+1][int_index]==disc and list_string[row_top+2][int_index]==disc and list_string[row_top+3][int_index]==disc:
            return True
    count_left=0
    count_right=0
    for ind1 in range(int_index+1,len(list_string[row_top])):
        if list_string[row_top][ind1]==disc:
            count_right+=1
        else:
            break
    for ind2 in range(int_index-1,-1,-1):
        if list_string[row_top][ind2]==disc:
            count_left+=1
        else:
            break
    if count_left+count_right>=3:
        return True
    num_cols1=int_index-1
    count1=0
    for mean1 in range((row_top)-1,-1,-1):
        if num_cols1>=0 and list_string[mean1][num_cols1]==disc:
            count1+=1
            num_cols1-=1
        else:
           break
    num_cols2=int_index+1
    count2=0
    for clex in range(row_top+1,len(list_string)):
        if num_cols2<=(len(list_string[clex])-1) and list_string[clex][num_cols2]==disc:
            count2+=1
            num_cols2+=1
        else:
            break
    count3=0
    num_cols3=int_index-1
    for mean2 in range(row_top+1,len(list_string)):
        if num_cols3>=0 and list_string[mean2][num_cols3]==disc:
            count3+=1
            num_cols3-=1
        else:
            break
    count4=0
    num_cols4=int_index+1
    for clex in range(row_top-1,-1,-1):
        if num_cols4<=(len(list_string[clex])-1) and list_string[clex][num_cols4]==disc:
            count4+=1
            num_cols4+=1
        else:
            break
    if  (count1+count2>=3) or (count3 +count4>=3):
        return True
    return False

print(has_won(['X....O...', 'O....OO..', 'O.XOOOXOX', 'XXXOXXOXX', 'OXOXXXOOO'], 4))
              
               
              
                   
              
                   

                   
                    
                    
                    
                    
                    
                    
                           
                       
                       
                       
               
               


            
                    
                
            




        
            
               


        




           




