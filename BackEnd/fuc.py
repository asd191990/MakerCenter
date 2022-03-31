from .models import News,Course,Group,DownLoadFiles,ClassroomIntroducts,Equipment,Space,Memebers,Group
def DBprocess(dbtype):
    switch_db = {
        "classroom":Course,
        "ClassroomIntroducts":ClassroomIntroducts,
        "DownLoadFiles":DownLoadFiles,
        "News":News,
        "Equipment":Equipment,
        "Space":Space,
        "Group":Group,
        "Memebers":Memebers
    }
    return switch_db.get(dbtype)
