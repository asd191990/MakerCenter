from django import forms
from .models import News, Coures, classroomintroducts

# 新增最新消息填寫表單

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        
        fields = ('title', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': '標題',
            'content': '內容',
        }

# 新增課程表單

class CouresForm(forms.ModelForm):

    class Meta:
        model = Coures
        
        fields = ('title', 'content', 'type')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }

        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'title': '課程名稱',
            'content': '課程內容',
            'type': '課程類型',
        }

# 新增校級共用實驗室

class CouresForm(forms.ModelForm):

    class Meta:
        model = classroomintroducts
        
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