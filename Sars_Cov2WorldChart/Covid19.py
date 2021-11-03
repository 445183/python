import pandas as pd
import plotly.express as pex

class data_visualiztion:
    def __init__(self,file_name):
        self.file_name=file_name
        file=pd.read_csv(file_name)

        self.CSV=file
    
    def draw_chart(self):
        data_frame=self.CSV
        x_val='country'
        z_val='cases'
        y_val='date'

        chart=pex.scatter_3d(data_frame,x_val,y_val,z_val,color='country')

        self.chart=chart

    def show_chart(self):
        fig=self.chart
        fig.show()

def main():
    a=input("Enter the covid 19 cases data (file name): ")
    print("Starting, reading csv file ....")
    print("")
    
    new_chart=data_visualiztion(a)

    print("Constructing the chart !")
    new_chart.draw_chart()
    print("Construction completed, trying to display...")
    print("")

    print("Showing the chart in a couple of seconds ...")
    new_chart.show_chart()
    print("Process completed !")

main()