from dependency import os,path,re,string
available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

def searchfile(file_name):
    pass
