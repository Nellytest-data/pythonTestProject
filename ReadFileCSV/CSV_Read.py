import pandas as pd
from IPython.display import display
from numba.np.arraymath import return_false
from numpy.ma.core import multiply
from pandas.core.interchange.dataframe_protocol import DataFrame


def File_transactions():
    try:
        df = pd.read_csv('transactions_example.csv')
        parse_dates = ['Date']
        print("parse_dates :", df)
        print("df['Date'].dtype : ", df['Date'].dtype)
        df['Date'] = pd.to_datetime(df['Date'])
        print("df['Date'] = pd.to_datetime(df['Date']):"'\n', df['Date'])
        print("df['Date'].dtype : ", df['Date'].dtype)
        print("df.isnull() :", df.isnull().any(axis=1))

        # print(df)
        # print(df.shape)
        # print(df.describe())
        # print(df.values)

        # max rows' index
        max_row = df.shape[0]
        print("Max Row : ", max_row)

        # max columns' index
        max_col = df.shape[1]
        print("Max Columns : ", max_col)

        df.head()
        df_to_str = df.to_string()
        # print(df.to_string())

        # examining missing values
        print("Missing values distribution: ")
        print(df.isnull().mean())
        print("")

        # check datatype in each column
        print("Column datatypes: ")
        print(df.dtypes)

        print(df.values[0])

        display(df.head(5))

        return df
    except Exception as e:
        print(f"Error in extraction : {e}")
        return None


#end File_transactions()


#Calculate expense-to-income ratio and check if the user maintains budget balance.
def Calculate_expense_income():
 try:
    i = 0
    exp_res = 0
    inc_res = 0

    df = File_transactions()

    Date_Value = df['Date']
    print("Date_Value = df['Date'] : '\n' ", Date_Value)
    print("Date_Value.dtype) : '\n' ", Date_Value.dtype)

    Date_Value_Str = str(Date_Value)
    print("Date_Value_Str = str(Date_Value) : '\n' ", Date_Value_Str)
    print("type(Date_Value_Str) : '\n' ", type(Date_Value_Str))

    Amount_mean = df["Amount"].mean()
    print("df Amount mean : \n ", Amount_mean)

    # Create monthly summary: total income and expenses.
    Amount_sum = df["Amount"].sum()
    print("df Amount sum : \n ", Amount_sum)

    Amount_value = df["Amount"].values
    print("Amount's value[0] : \n ", Amount_value[0])

    Categ_Amount_Describe = df[["Category", "Amount"]].describe()
    print("Categ_Amount_Describe = df[[Category, Amount]].describe()", Categ_Amount_Describe)

    while i < len(Amount_value):

        if Amount_value[i] < 0:
            exp_res += Amount_value[i]  #Amount_value.sum()
            i += 1

        elif Amount_value[i] > 0:
            inc_res += Amount_value[i]  # Amount_value.sum()
            i += 1

        else:
            print("Error")

    mean_exp = exp_res / i

    print("Mean : \n", mean_exp)
    print("count = i : \n", i)
    print("exp_res : \n", exp_res)
    print("inc_res : \n", inc_res)

    return exp_res, inc_res, mean_exp
 except Exception as e:
    return None

#end Calculate_expense_income()


# Sort data by expense categories.
def Sorted_File():
 try:
    df = File_transactions()

    sorted_df = df.sort_values(by=['Category']).values
    print("Sorted File by Category : \n", sorted_df)
    print("type of sorted_df by Category : \n", sorted_df.dtype)  # object type
    df_cat = pd.DataFrame(sorted_df)
    df_cat.to_csv('Sorted Categories.csv', index=False)

    return df_cat
 except Exception as e:
    return None

#end Sorted_File()


def Percentages_Calculation(income, expense):
    try:
        percent = ((expense * (-1)) * 100) / income
        return percent
    except Exception as e:
        print(f"Error in calculation : {e}")
        return None


#Percentages_Calculation


#Balance
def Balance():
 try:
    res = Calculate_expense_income()
    print("res  : \n ", res[0], res[1], res[2])
    print("exp_res : \n ", res[0])
    print("inc_res : \n ", res[1])
    print("mean : \n", res[2])

    if res[0] < 0 and res[1] > 0:
        expense = res[0]
        income = res[1]
        mean_exp = res[2]

    if (expense * (-1)) > (mean_exp * (-1)):
        print("Reduce your expenses : \n")
    else:
        print("You don't need reduce your expenses")

        print("Exspenses = \n", expense)
        print("Expenses' mean = \n", mean_exp)

    balance = expense + income
    print("balance : \n :", balance)

    if balance > 0:
        print("Good Balance : \n ", balance)
    else:
        print("Increase Your income : \n ", balance)

    return balance, mean_exp
 except Exception as e:
    return None

#end Balance()

def Expenses_Mean(var1,var2):
    try:
        exp_mean = var1/var2
    except ZeroDivisionError:
        exp_mean = None
    else:
        return exp_mean
#end Expenses_Mean(var1,var2)


#Write a function that identifies categories with expenses higher than desired average.
def Categories_Expenses():
 try:
    res = Balance()
    balance_for_all = res[0]
    mean_exp = res[1]
    print("Balance  & Expenses' Mean : ", balance_for_all, mean_exp)

    sum_exsp_res = []
    sum_inc_res = []
    percents_res = []
    categories = []
    dic_cat_dep = []

    df = File_transactions()

    count_entr = 0
    count_dng = 0
    count_groc = 0
    count_hl = 0
    count_rnt = 0
    count_trnsp = 0
    count_utl = 0

    cat_val_set = set(df['Category'].values)

    if 'Entertainment' in cat_val_set:
        count_entr = df['Category'].str.contains('Entertainment').sum()

    if 'Dining' in cat_val_set:
        count_dng = df['Category'].str.contains('Dining').sum()

    if 'Groceries' in cat_val_set:
        count_groc = df['Category'].str.contains('Groceries').sum()

    if 'Healthcare' in cat_val_set:
        count_hl = df['Category'].str.contains('Healthcare').sum()

    if 'Rent' in cat_val_set:
        count_rnt = df['Category'].str.contains('Rent').sum()

    if 'Transport' in cat_val_set:
        count_trnsp = df['Category'].str.contains('Transport').sum()

    if 'Utilities' in cat_val_set:
        count_utl = df['Category'].str.contains('Utilities').sum()



        print("count for Entertainment : \n", count_entr)
        print("count for Dinig : \n", count_dng)
        print("count for Groceries : \n", count_groc)
        print("count for Healthcare : \n", count_hl)
        print("count for Rent : \n", count_rnt)
        print("count for Transport : \n", count_trnsp)
        print("count for Utilities : \n", count_utl)

        len_unq = len(df['Category'].unique())
        print("Categories' Numbers : \n", len_unq)

        #Entertainment
        categ_etnrt = df.loc[df['Category'].isin(['Entertainment'])]
        print("df.loc[df[Category].isin([Entertainment])] : \n", categ_etnrt, type(categ_etnrt))
        sub_df_entr = categ_etnrt[['Category', 'Amount']]  #sub df
        print("sub_df for Entertainment : \n", sub_df_entr)
        print(type(sub_df_entr))  #pandas.core.frame.DataFrame
        print(sub_df_entr['Category'].values[7], sub_df_entr['Amount'].values[7])
        sum_entr = sub_df_entr['Amount'].sum()



        mean_entr = Expenses_Mean(sum_entr,count_entr)
        print("mean for Entertainment = \n", mean_entr)

        if (sum_entr * (-1)) > (mean_entr * (-1)):
            print(
                "Your Entertainment expenses   > than average value of the Entertainment expenses.Keep attention for it and try to spend less money on Entertainment. \n")
        else:
            print("Your Entertainment expenses  < = than average value of the Entertainment expenses \n ")
            print("Sum for Entertainment = \n", sum_entr)
        sum_exsp_res.append(sum_entr)

        #Dining
        categ_dng = df.loc[df['Category'].isin(['Dining'])]
        print("df.loc[df[Category].isin([Dining])] : \n", categ_dng, type(categ_dng))
        sub_df_dng = categ_dng[['Category', 'Amount']]  # sub df
        print("sub_df for Dining : \n", sub_df_dng)
        sum_dng = sub_df_dng['Amount'].sum()

        mean_dng = Expenses_Mean(sum_dng, count_dng)
        print("mean for Dining : \n", mean_dng)

        if (sum_dng * (-1)) > (mean_dng * (-1)):
            print("Your Dining expenses   > than average value of the Dining expenses.Keep attention for it and try to spend less money on Dining. \n")
        else:
            print("Your Dining expenses > = than average value of the Dining expenses \n")
            print("Sum for Dining = \n", sum_dng)
        sum_exsp_res.append(sum_dng)

        #Groceries
        categ_groc = df.loc[df['Category'].isin(['Groceries'])]
        print("df.loc[df[Category].isin([Groceries])] : \n", categ_groc, type(categ_groc))
        sub_df_groc = categ_groc[['Category', 'Amount']]  # sub df
        print("sub_df for Groceries : \n", sub_df_groc)
        sum_groc = sub_df_groc['Amount'].sum()

        mean_groc = Expenses_Mean(sum_groc,count_groc)
        print("mean for Groceries : \n", mean_groc)

        if (sum_groc * (-1)) > (mean_groc * (-1)):
            print("Your Groceries' expenses   > than average value of the Groceries' expenses.Keep attention for it and try to spend less money on Groceries. \n")
        else:
            print("Your Groceries' expenses < = than average value of the Groceries' expenses")
            print("Sum for Groceries = \n", sum_groc)
        sum_exsp_res.append(sum_groc)

        #Healthcare
        categ_hl = df.loc[df['Category'].isin(['Healthcare'])]
        print("df.loc[df[Category].isin([Healthcare])] : \n", categ_hl, type(categ_hl))
        sub_df_hl = categ_hl[['Category', 'Amount']]  # sub df
        print("sub_df for Healthcare : \n", sub_df_hl)
        sum_hl = sub_df_hl['Amount'].sum()
        print("Sum for Healthcare = \n", sum_hl)

        mean_hl = Expenses_Mean(sum_hl,count_hl)
        print("mean for Healthcare : \n", mean_hl)

        if (sum_hl * (-1)) > (mean_hl * (-1)):
            print("Your Healthcare expenses   > than average value of the Healthcare expenses.Keep attention for it and try to spend less money on Healthcare. \n")
        else:
            print("Your Healthcare expenses < = than average value of the Healthcare expenses")
            print("Sum for Healthcare = \n", sum_hl)
        sum_exsp_res.append(sum_hl)

        #Rent
        categ_rnt = df.loc[df['Category'].isin(['Rent'])]
        print("df.loc[df[Category].isin([Rent])] : \n", categ_rnt, type(categ_rnt))
        sub_df_rnt = categ_rnt[['Category', 'Amount']]  # sub df
        print("sub_df for Rent : \n", sub_df_rnt)
        sum_rnt = sub_df_rnt['Amount'].sum()

        mean_rnt = Expenses_Mean(sum_rnt,count_rnt)
        print("mean for Rent : \n", mean_rnt)

        if (sum_rnt * (-1)) > (mean_rnt * (-1)):
            print("Your Rent expenses   > than average value of the Rent expenses.Keep attention for it and try to spend less money on Rent. \n")
        else:
            print("Your Rent expenses < = than average value of the Rent expenses")
            print("Sum for Rent = \n", sum_rnt)
        sum_exsp_res.append(sum_rnt)

        #Salary
        categ_slr = df.loc[df['Category'].isin(['Salary'])]
        print("df.loc[df[Category].isin([Salary])] : \n", categ_slr, type(categ_slr))
        sub_df_slr = categ_slr[['Category', 'Amount']]  # sub df
        print("sub_df for Salary : \n", sub_df_slr)
        sum_slr = sub_df_slr['Amount'].sum()
        print("Sum for Salary = \n", sum_slr)

        #Transport
        categ_trnsp = df.loc[df['Category'].isin(['Transport'])]
        print("df.loc[df[Category].isin([Transport])] : \n", categ_trnsp, type(categ_trnsp))
        sub_df_trnsp = categ_trnsp[['Category', 'Amount']]  # sub df
        print("sub_df for Transport : \n", sub_df_trnsp)
        sum_trnsp = sub_df_trnsp['Amount'].sum()

        mean_trnsp = Expenses_Mean(sum_trnsp,count_trnsp)
        print("mean for Transport : \n", mean_trnsp)

        if (sum_trnsp * (-1)) > (mean_trnsp * (-1)):
            print("Your Transport expenses   > than average value of the Transport expenses.Keep attention for it and try to spend less money on Transport. \n")
        else:
            print("Your Transport expenses < = than average value of the Transport expenses")
            print("Sum for Transport = \n", sum_trnsp)
        sum_exsp_res.append(sum_trnsp)

        #Utilities
        categ_utl = df.loc[df['Category'].isin(['Utilities'])]
        print("df.loc[df[Category].isin([Utilities])] : \n", categ_utl, type(categ_utl))
        sub_df_utl = categ_utl[['Category', 'Amount']]  # sub df
        print("sub_df for Utilities : \n", sub_df_utl)
        sum_utl = sub_df_utl['Amount'].sum()
        print("Sum for Utilities = \n", sum_utl)

        mean_utl = Expenses_Mean(sum_utl,count_utl)
        print("mean for Utilities : \n", mean_utl)

        if (sum_utl * (-1)) > (mean_utl * (-1)):
            print("Your Utilities expenses   > than average value of the Utilities expenses.Keep attention for it and try to spend less money on Utilities. \n")
        else:
            print("Your Utilities expenses < = than average value of the Utilities expenses")
            print("Sum for Utilities = \n", sum_utl)
        sum_exsp_res.append(sum_utl)
        sum_inc_res.append(sum_slr)

       #Expenses' Percentages' calculation
        percent_entr = Percentages_Calculation(sum_slr, sum_entr)
        print("Entertainment's percentage = \n", percent_entr)
        percents_res.append(percent_entr)

        if percent_entr > 10.0:
            print(f"Please,reduce your Entertainment expenses by {percent_entr : 0.2f} / 2 = {percent_entr / 2 : 0.2f} %, to reach saving goals\n")
        else:
            print("Well done,your Entertainment expenses are less than 10% of monthly income : \n",percent_entr)
        categories.append('Entertainment')

        percent_dng = Percentages_Calculation(sum_slr, sum_dng)
        print("Dining percentage = \n", percent_dng)
        percents_res.append(percent_dng)

        if percent_dng > 10.0:
            print(f"Please,reduce your Dining expenses by {percent_dng : 0.2f} / 2 = {percent_dng / 2 : 0.2f} %, to reach saving goals\n")
        else:
            print("Well done,your Dining expenses are less than 10% of monthly income : \n",percent_dng)
        categories.append('Dining')

        percent_groc = Percentages_Calculation(sum_slr, sum_groc)
        print("Groceries percentage = \n", percent_groc)
        percents_res.append(percent_groc)

        if percent_groc > 10.0:
            print(f"Please,reduce your Groceries expenses by {percent_groc : 0.2f} / 2 = {percent_groc / 2 : 0.2f} %, to reach saving goals\n")
        else:
            print("Well done,your Groceries expenses are less than 10% of monthly income : \n",percent_groc)
        categories.append('Groceries')

        percent_hl = Percentages_Calculation(sum_slr, sum_hl)
        print("Healthcare percentage = \n", percent_hl)
        percents_res.append(percent_hl)

        if percent_hl > 10.0:
            print(f"Please,reduce your Healthcare expenses by {percent_hl : 0.2f} / 2 = {percent_hl / 2 : 0.2f} %, to reach saving goals\n")
        else:
            print("Well done,your Healthcare expenses are less than 10% of monthly income : \n",percent_hl)
        categories.append('Healthcare')

        percent_rnt = Percentages_Calculation(sum_slr, sum_rnt)
        print("Rent percentage = \n", percent_rnt)
        percents_res.append(percent_rnt)

        if percent_rnt > 10.0:
            print(f"Please,reduce your Rent expenses by {percent_rnt : 0.2f} / 2 = {percent_rnt / 2 : 0.2f} %, to reach saving goals\n")
        else:
            print("Well done,your Rent expenses are less than 10% of monthly income : \n",percent_rnt)
        categories.append('Rent')

        percent_trnsp = Percentages_Calculation(sum_slr, sum_trnsp)
        print("Transport percentage = \n", percent_trnsp)
        percents_res.append(percent_trnsp)

        if percent_trnsp > 10.0:
            print(f"Please,reduce your Transport expenses by {percent_trnsp : 0.2f} / 2 = {percent_trnsp / 2 : 0.2f} %, to reach saving goals\n")
        else:
            print("Well done,your Transport expenses are less than 10% of monthly income : \n",percent_trnsp)
        categories.append('Transport')

        percent_utl = Percentages_Calculation(sum_slr, sum_utl)
        print("Utilities percentage = \n", percent_utl)
        percents_res.append(percent_utl)

        if percent_utl > 10.0:
            print(f"Please,reduce your Utilities expenses by {percent_utl : 0.2f} / 2 = {percent_utl / 2 : 0.2f} %, to reach saving goals\n")
        else:
            print("Well done,your Utilities expenses are less than 10% of monthly income : \n",percent_utl)
        categories.append('Utilities')

    return sum_inc_res, sum_exsp_res, percents_res, categories
 except Exception as e:
    return  None

#end Categories_Expenses()


#To Create a Monthly Deposit by Expenses' Percentages' Comparison
def Monthly_Deposit():
 try:
    user_input = 0
    while True:
        try:
            user_input = float(input("Please, enter an amount to deposit. : "))
            print("Your entered : ", user_input)
        except ValueError:
            print("%s" % (user_input), "Not an number!Try again.")
            continue
        else:
            print("Yes,it is  a number !")
            break

    res = Categories_Expenses()

    monthly_dep = []

    tp_lst = list(res)

    sum_inc_res = tp_lst[0]
    sum_exsp_res = tp_lst[1]
    percents_res = tp_lst[2]
    categories = tp_lst[3]

    print("categories : \n", categories)

    percents_total = percents_res

    for exp_percent in percents_total:
        print(f"expenses percentage = {exp_percent} \n and total percentages for expenses = {percents_total} \n")
        if exp_percent >= 15.0:
            print(f"Please,reduce your expenses by {exp_percent} / 2 = {exp_percent / 2} %, to reach saving goals\n")
        else:
            mult = multiply(sum_inc_res, exp_percent)
            val = mult / 100
            print("val = \n", val)
            #Increase in the amount of expenses after making a deposit amount from monthly income
            val_dep = val + user_input
            print("val_dep = \n", val_dep)
            monthly_dep.append(val_dep)

            print("Monthly Saving Value = \n", monthly_dep)

    return monthly_dep
 except Exception as e:
    return None

#end Monthly_Deposit()


#Save a List of expenses after user's deposit
def Save_Deposit():

 try:

    deposit = Monthly_Deposit()
    print("DEPOSIT : \n", deposit)

    Category_Names = ["Entertainment", "Dining", "Groceries", "Healthcare", "Transport", "Utilities"]
    monthly_dep = deposit[0], deposit[1], deposit[2], deposit[3], deposit[4], deposit[5]
    dic_cat_dep = {'Category Names': Category_Names, 'Monthly Deposit': monthly_dep}
    df_dep = pd.DataFrame(dic_cat_dep)
    df_dep.to_csv('Monthly Expenses include Deposit.csv')

    with open('monthly_expenses_include_deposit.txt', 'w+') as f:

        for item in deposit:
            f.write('%0.2f\n' % item)

        print("File written successfully")
    f.close()
    return f
 except Exception as e:
    print(f"Error creating file : {e}")
    return None

  #end Save_Deposit(deposit)


