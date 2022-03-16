from .models import News,Course,Group,DownLoadFiles,ClassroomIntroducts,Equipment,Space,Memebers
def DBprocess(dbtype):
    switch_db = {
        "classroom":Course,
        "ClassroomIntroducts":ClassroomIntroducts,
        "DownLoadFiles":DownLoadFiles,
        "News":News,
        "Equipment":Equipment,
        "Space":Space,
        "Memebers":Memebers
    }
    return switch_db.get(dbtype)
