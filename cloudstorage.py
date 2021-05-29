import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)


    f = open(file_from, 'rb')
    dbx.files_upload(f.read(),file_to)

    def main():
        access_token = 'sl.Axv64UwTA83nrvgkfV9VaMyV3JhJjWiJH-Y3-rLSIY9-ow6hZuQfypmvXqW0okO4AKsdXp3m9pd0cr2azGtmJCbziwZe4fxHR2elE1QimKD3kty71Ku6fc8IL9vibyN2Tx5L6r8'
        transferData = TransferData(access_token)

        file_from = input("Enter the file path to transfer : -")
        file_to = input("Enter the fullpath to upload to dropbox:-") #This is the full path to up

        #API v2
        transferData.upload_file(file_from,file_to)
        print("File has been moved !!!")