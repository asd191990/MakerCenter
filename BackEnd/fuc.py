from .models import News,Course,Group,DownLoadFiles,ClassroomIntroducts,Equipment,Space
def DBprocess(dbtype):
    switch_db = {
        "classroom":Course,
        "ClassroomIntroducts":ClassroomIntroducts,
        "DownLoadFiles":DownLoadFiles,
        "News":News,
        "Equipment":Equipment,
        "Space":Space
    }
    return switch_db.get(dbtype)
