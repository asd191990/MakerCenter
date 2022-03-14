from .models import News,Course,Group,DownLoadFiles,ClassroomIntroducts
def DBprocess(dbtype):
    switch_db = {"classroom":Course,"ClassroomIntroducts":ClassroomIntroducts,"DownLoadFiles":DownLoadFiles}
    return switch_db.get(dbtype)
