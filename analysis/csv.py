from os import path

def launch_analysis(data_file):
    directory = path.dirname(path.dirname(__file__))
    path_to_file = path.join(directory, "data", data_file)
    
    try:
        with open(path_to_file,"r") as f:
            preview = f.readline()
            print("Yeah! We managed to read the file. Here is a preview:")
            print(preview)
    except FileNotFoundError as e:
        print("Ow :( The file was not found. Here is the original message of the exception :", e)
    except:
        print('Destination unknown')


if __name__=="__main__":
    launch_analysis('current_mps.csv')