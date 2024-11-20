# This is a sample Python script.
from ReadFileCSV import CSV_Read
from Graphical_Visualization import Expenses_Income_Graphical_Visualization as gr


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    df = CSV_Read.File_transactions()

    df_srt = CSV_Read.Sorted_File()

    file = CSV_Read.Save_Deposit()

    gr.Graph_Vis()

