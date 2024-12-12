import data_extractor
import db_writer
import data_visualization
import matplotlib.pyplot as plt
def main():

        file_path = 'logfiles.log'
       
        #Uncomment to following lines to insert data into the database,
        #log_data = data_extractor.parse_logs(file_path)
        #db_writer.insert_data_into_postgres(log_data)
        
        #Displaying graphs for data visualization
        plt.figure(1)
        data_visualization.violin_plot()
        plt.figure(2)
        data_visualization.line_plot()
        plt.figure(3)
        data_visualization.bar_plot()
        plt.show()
        
        
        

if __name__ == '__main__':
        try:
                main()
        except Exception as e:
                print(f"Error: {e}")        