
from ReadFileCSV import CSV_Read as rd

import matplotlib.pyplot as plt

from ReadFileCSV.CSV_Read import Categories_Expenses


def Graph_Vis():
 try:
    res = rd.Categories_Expenses()

    tp_lst = list(res)

    sum_inc_res = tp_lst[0]
    sum_exsp_res = tp_lst[1]
    percents_res = tp_lst[2]


    #Lists of Category_Names, Amount_For_Each_Expense, Total_Monthly_Income_Before_Expenses, Percentages_Expenses

    Category_Names = ["Entertainment","Dining","Groceries","Healthcare","Rent","Transport","Utilities"]
    Amount_For_Each_Expense = [sum_exsp_res[0],sum_exsp_res[1],sum_exsp_res[2],sum_exsp_res[3],sum_exsp_res[4],sum_exsp_res[5],sum_exsp_res[6]]
    Total_Monthly_Income_Before_Expenses = sum_inc_res[0]
    Percentages_Expenses = [percents_res[0],percents_res[1],percents_res[2],percents_res[3],percents_res[4],percents_res[5],percents_res[6]]

    # dictionary of lists
    dict_perc = {'Category Names' : Category_Names,'Percentages Expenses' : Percentages_Expenses, 'Amount For Each Expense' : Amount_For_Each_Expense,'Total Monthly Income Before Expenses' : Total_Monthly_Income_Before_Expenses}

    df_perc = rd.pd.DataFrame(dict_perc)

    # saving the dataframe
    df_perc.to_csv("Percentage of Expenses from Income.csv")



    #pie chart

    explode = (0, 0, 0, 0, 0.1, 0, 0) # only "explode" 5th slice expenses for 'Rent'

    fig_pie, ax = plt.subplots()
    ax.pie(Percentages_Expenses,explode=explode,labels=Category_Names,autopct='%1.2f%%',
                      shadow=True,  startangle=90, textprops={'fontsize' : 11})
    plt.title("Expenses' Percentage \n " + " October 2024 ", fontdict={"fontsize" : 14}, bbox={'facecolor' : '0.9', 'pad' : 16 } )


    plt.savefig('Pie_Chart_Expenses_Percentage.png')

    plt.show()
 except Exception as e:
    print(f"Error creating pie chart : {e}")

#end Graph_Vis()