from .models import News,Course,Group,DownLoadFiles
def DBprocess(dbtype):
    switch_db = {"classroom":Course,"ClassroomIntroducts":ClassroomIntroducts}
    return switch_db.get(dbtype)
