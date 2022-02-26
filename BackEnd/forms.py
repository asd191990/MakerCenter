from django import forms
from .models import News, Course, ClassroomIntroducts, DownLoadFiles, Memebers, Group, Space

# 新增最新消息填寫表單

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        
        fields = ('title', 'content', 'type')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': '標題',
            'content': '內容',
            'type': '類型',
        }

# 新增課程表單

class CouresForm(forms.ModelForm):

    class Meta:
        model = Course
        
        fields = ('title', 'content', 'type')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'title': '課程名稱',
            'content': '課程內容',
            'type': '課程類型',
        }

# 新增校級共用實驗室

class ClassroomForm(forms.ModelForm):

    class Meta:
        model = ClassroomIntroducts
        
        fields = ('title', 'content', 'imageone')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }

        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'title': '教室名稱',
            'content': '教室描述',
            'imageone': '教室照片',
        }

# 新增各類申請及說明 / 相關辦法

class DownLoadFilesForm(forms.ModelForm):

    class Meta:
        model = DownLoadFiles
        
        fields = ('title', 'content', 'type')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'title': '標題',
            'content': '申請內容',
            'type': '申請類型',
        }

# 新增成員

class MemebersForm(forms.ModelForm):

    class Meta:
        model = Memebers
        
        fields = ('name', 'extension', 'email', 'work', 'location')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'extension': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'work': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'name': '姓名',
            'extension': '分機',
            'email': '電子信箱',
            'work': '業務職掌',
            'location': '位置',
        }

# 新增專業領域小組

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        
        fields = ('title', 'content', 'type')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'title': '標題',
            'content': '內容',
            'type': '類型',
        }

# 新增空間介紹及設備

class SpaceForm(forms.ModelForm):

    class Meta:
        model = Space
        
        fields = ('code', 'name', 'space_description', 'number', 'equipment_description')

        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'space_description': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'equipment_description': forms.TextInput(attrs={'class': 'form-control'}),
        }

        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'code': '教室代碼',
            'name': '教室名稱',
            'space_description': '空間介紹',
            'number': '容納人數',
            'equipment_description': '設備資訊',
        }