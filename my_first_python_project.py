import os,shutil
# NOTE: You can write every single extensions inside tuples 
dict_extensions = {
    'audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac'),
    'video_extensions' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'document_extensions' : ('.ZIP','.zip', '.rar', '.RAR''.doc', '.pdf', 'sql', 'SQL', '.txt','py','php','.xlsx'),
    'image_extesntions':('PNG', 'png', 'JPG' ,'svg','jpg','jpeg'),
}

folderpath=input("enter folder path")

def files_finder(folderpath, file_extensions):
    files=[]
    for file in os.listdir(folderpath):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)

    return files
# returned=files_finder(os.getcwd(), dict_extensions['document_extensions'])
#print(files_finder(os.getcwd(), dict_extensions['document_extensions']))


for extension_type, extension_tuple in dict_extensions.items():
    folder_name = extension_type.split('_')[0] + 'Files'
    folder_path = os.path.join(folderpath, folder_name)
    if os.path.exists(folder_path):
        pass
    else:
        os.mkdir(folder_path)
    for item in files_finder(folderpath, extension_tuple):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)
 