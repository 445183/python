import dropbox
import os

def uploadFile(at,file,folder):
    access_token=at
    dbx=dropbox.Dropbox(access_token)

    folders='/'+folder+'/'+file
    files=open(file,'rb')
    files=files.read()

    dbx.files_upload(files,folders,dropbox.files.WriteMode.overwrite)
        
    print("Files have been uploaded succesfully !")

class cloud_storage:
    def __init__(self,accessToken):
        self.at=accessToken

    def getFiles(self,folder):
        files=''
        while files=='':
            for files in os.walk(folder):
                if files:
                    for i in range(0,len(files[1])):
                        sub_folder=files[1][i]
                        sub_folder_path=folder+'/'+sub_folder

                        list=os.listdir(sub_folder_path)
                        for file in list:
                            file_path=sub_folder_path+'/'+file
                            uploadFile(self.at,file_path,file_path)
    
def main():
    while True:
        print("Welcome to dropbox cloud storage !")
        print("")

        user=cloud_storage('aaNBtIgUCzMAAAAAAAAAAW_J923vlOWMPS_RX8iU65vcg9blgg7l2RsrwtELW3qi')

        yn=input("Would you like to upload a file to cloud storage(y/n): ").lower()
        print("")

        if yn=='y':
            folder=input("Enter the folder which you would like to store in cloud storage along with its content: ")
            user.getFiles(folder)
        elif yn=='n':
            print("Thanks for using our program !")

        print("")
        print("")

main()