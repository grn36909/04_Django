from django.shortcuts import render

# Create your views here.

def home_text(request):
    key = u'text'
    string = u"我在自强学堂学习Django，用它来建网站"
    info = u'Wellcome to my learn.'
    return render(request, 'home.html', {'key': key, 'string': string, 'info': info})
# 在视图中我们传递了一个字符串(string) 到模板(home.html)

def home_for(request):
    key = u'for'
    TutorialInfo = u'教程列表: '
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'key': key, 'TutorialInfo': TutorialInfo, 'TutorialList': TutorialList})

def home_dict(request):
    key = u'dict'
    info_dict = {'site': u'《自强学堂》', 'content': u'【各种IT技术教程】'}
    return render(request, 'home.html', {'key': key, 'info_dict': info_dict})

def home_list(request):
    key = u'list'
    List = map(str, range(100))         # 一个长度为100的 List
    return render(request, 'home.html', {'key': key, 'List': List})