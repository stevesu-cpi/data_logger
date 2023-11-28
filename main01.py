

import sys
import tempRise
import pandas as pd
import matplotlib.pyplot as plt

def main(input_csv_file, data_path):
    
    input_df = pd.read_csv(input_csv_file)
    print('\n')
    inp = input('Choose filter type: r = row, c = cable, n = none, e = exit or any other key: ')        
    if inp == 'r':
        inp_list = input('enter row numbers i.e. [1,3,4,6] or [1-4]: ')
        inp_list = convert_to_intlist(inp_list)
        idx_col = list(input_df['index'])
    elif inp == 'c':
        inp_list = input('enter cable ids i.e. [1,3,4,6] or [1-4]: ')
        inp_list = convert_to_intlist(inp_list)
        idx_col = list(input_df['cable_id'])
    elif inp == 'n':
        inp_list = None    
    else:
        return
    
    if inp_list != None:
        iloc_idx_list = []                
        for idx in inp_list:
            while True:  
                try:
                    row_num = idx_col.index(idx)
                    idx_col[row_num] = None
                    iloc_idx_list.append(row_num)
                except ValueError:
                    break    
        input_df = input_df.iloc[iloc_idx_list, : ]
        input_df = input_df.reset_index(drop=True)        
    print('input_df: \n', input_df, '\n') 
    newclass = tempRise.dataGroup(input_df, data_path)
    new_dict_df = newclass.dict_df
    newclass.make_temprise_table()

    while True:

        inp = input('Choose output: p = plot, d = derate, t = temprise, e = exit or any other key: ') 
 
        if inp == 'p':
            fig, ax = newclass.plotchart2('title', new_dict_df)
            plt.show()

            while True:
                replot = input('do you want to replot? y/n: ')
                if replot == 'y' or replot == 'Y':
                    xdata_str = input('enter "[xmin, xmax]" include brackets ')
                    ydata_str = input('enter ["ymin, ymax]" include brackets ')
                    xdata_list = convert_to_floatlist(xdata_str)
                    ydata_list = convert_to_floatlist(ydata_str)
                    xdata_tup = (xdata_list[0], xdata_list[1])
                    ydata_tup = (ydata_list[0], ydata_list[1])
                    plt.close()
                    fig, ax = newclass.plotchart2('title', new_dict_df)
                    fig, ax = newclass.resize(fig, ax, xdata_tup, ydata_tup)
                    plt.show()
                else:
                    plt.close()
                    break
                    

        elif inp == 'd':
            derate_dict = newclass.make_derate_table()
            for k in derate_dict.keys():
                print('\n')
                print(derate_dict[k])
                
        else:
            break        
    return


def convert_to_floatlist(list_str):
    list_str = list_str[1:]
    new_list = []
    temp_str = ''
    for ch in list_str:
        if ch != ',' and ch != ' ' and ch != ']':
            temp_str += ch
        if ch == ',' or ch == ']':
            new_list.append(float(temp_str))
            temp_str = ''
    return new_list

def convert_to_intlist(list_str):
    list_str = list_str[1:]
    new_list = []
    temp_str = ''
    for i, ch in enumerate(list_str):
        if ch != ',' and ch != ' ' and ch != ']' and ch != '-':
            temp_str += ch
        elif ch == ',' or ch == ']':
            new_list.append(int(temp_str))
            temp_str = ''
        elif ch == '-':
            new_list.append(int(temp_str))
            temp_str = ''
            for k in range(i+1,len(list_str) - 1):
                temp_str += list_str[k]
            new_list = list(range(new_list[0],int(temp_str)+1))
            return new_list  
    return new_list

if __name__ == '__main__':
    input_csv = sys.argv[1]
    path = sys.argv[2] + '/'

    main(input_csv, path)   
    

    '''    index_str = sys.argv[3]
    if index_str == 'None':
        index_list = None
    else:
        index_str = index_str[1:]  #convert string to list of integers  ... make into a function?
        index_list = []
        temp_str = ''
        for ch in index_str:
            if ch != ',' and ch != ' ' and ch != ']':
                temp_str += ch
            if ch == ',' or ch == ']':
                index_list.append(int(temp_str))
                temp_str = ''
        print(index_list)'''