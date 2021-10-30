import dropbox

class cloud_storage:
    def __init__(self,accessToken):
        self.at=accessToken
    
    def uploadFile(self,file,folder):
        access_token=self.at
        dbx=dropbox.Dropbox(access_token)

        folders='/'+folder+'/'+file
        files=open(file,'rb')
        files=files.read()

        dbx.files_upload(files,folders,dropbox.files.WriteMode.overwrite)
        
        print("Files have been uploaded succesfully !")
    
def main():
    while True:
        print("Welcome to dropbox cloud storage !")
        print("")

        user=cloud_storage('aaNBtIgUCzMAAAAAAAAAAW_J923vlOWMPS_RX8iU65vcg9blgg7l2RsrwtELW3qi')

        yn=input("Would you like to upload a file to cloud storage(y/n): ").lower()
        print("")

        if yn=='y':
            file=input("Enter the file you would like to upload: ")
            folder=input("Enter the folder where you would like to store your file in cloud storage: ")

            user.uploadFile(file,folder)
        elif yn=='n':
            print("Thanks for using our program !")

        print("")
        print("")

main()