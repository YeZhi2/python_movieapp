from django.http import JsonResponse
from django.shortcuts import render, redirect
from moviesapp.models import Movie
# Create your views here.

# 获取movie
def getbyid(request):
    if 'usertype' not in request.session or request.session['usertype'] != 'mgr':
        return render(request,"signin.html")
    id= int(request.GET.get('id'))
    movie=Movie.objects.get(mid=id)
    print(movie)
    return render(request,"movie.html",{'movie':movie})

def getall(request):
    if 'usertype' not in request.session or request.session['usertype'] != 'mgr':
        return render(request,"signin.html")
    movies=Movie.objects.all()
    return render(request,"movie.html",{'movies':movies})

# 新增movie
def newmovie(request):
    # 根据session判断用户是否是登录的管理员用户
    if 'usertype' not in request.session or request.session['usertype'] != 'mgr':
        return render(request,"signin.html")

    return render(request,"newmovie.html")

# 更新movie
def updatemovie(request):
    # 根据session判断用户是否是登录的管理员用户
    if 'usertype' not in request.session or request.session['usertype'] != 'mgr':
        return render(request,"signin.html")

    return render(request,"updatemovie.html")

def update(request):
    if 'usertype' not in request.session or request.session['usertype'] != 'mgr':
        return render(request,"signin.html")
    tit = request.POST.get('title')
    try:
        movie = Movie.objects.get(title=tit)
    except Movie.DoesNotExist:
        return render(request, "error.html")
    movie.movie_img = request.POST.get('movie_img')
    movie.director = request.POST.get('director')
    movie.actors = request.POST.get('actors')
    movie.content = request.POST.get('content')
    movie.grade = request.POST.get('grade')
    movie.link = request.POST.get('link')
    movie.save()
    return redirect('/main')


def save(request):
    # ptitle = request.POST.get('title')
    # pimg = request.POST.get('movie_img')
    # pdir = request.POST.get('director')
    # pact = request.POST.get('actors')
    # pcontent = request.POST.get('content')
    # pgrade = request.POST.get('grade')
    # prelease_date = request.POST.get('release_date')

    movie=Movie(
        title=request.POST.get('title'),
        movie_img=request.POST.get('movie_img'),
        director=request.POST.get('director'),
        actors=request.POST.get('actors'),
        content=request.POST.get('content'),
        grade=request.POST.get('grade'),
        release_date=request.POST.get('release_date'),
        link=request.POST.get('link'),
    )
    print('进入')
    movie.save()
    return redirect('/main')

# 删除
def deletebyid(request):

    if 'usertype' not in request.session or request.session['usertype'] != 'mgr':
        return render(request,"signin.html")
    id=int(request.GET.get('id'))
    movie=Movie()
    if id!=None:
        movie=Movie.objects.get(mid=id)
        movie.delete()
        msg = 'succeed'
    else:
        msg= 'failed'
        print("删除失败")

    return JsonResponse({'movie': movie,'msg':msg})

# 更新
def updatebyid(request):
    pmid=request.POST.get('id')
    ptitle = request.POST.get('title')
    pimg = request.POST.get('movie_img')
    pdir = request.POST.get('director')
    pact = request.POST.get('actors')
    pcontent = request.POST.get('content')
    pgrade = request.POST.get('grade')
    prelease_date = request.POST.get('release_date')



# API传值
# 前后端分离，传json
def get_json(request):
    movies=Movie.objects.all()
    data=list(movies.values())
    print(data)
    return JsonResponse({'data':data,'code':200,'msg':'获取数据'})

def search(request):
    name=request.GET.get('value')
    print(name)
    movies=Movie.objects.filter(title=name).values()
    data=[]
    data = list(movies)
    print(movies)
    if data != []:
        print(data)
        msg = 'succeed'
    else:
        msg = 'failed'
        print("还没有这个资源")

    # print(data)
    return JsonResponse({'data':data, 'code': 200, 'msg': msg})

# 删除movie
def delete(request):
    if 'usertype' not in request.session or request.session['usertype'] != 'mgr':
        return render(request,"signin.html")
    return render(request,"delmovie.html")

#删除函数
def do_del(request):
    if 'usertype' not in request.session or request.session['usertype'] != 'mgr':
        return render(request,"signin.html")
    tit=request.POST.get('title')
    try:
        movie = Movie.objects.get(title=tit)
    except Movie.DoesNotExist:
        return render(request,"error.html")
    movie.delete()
    return render(request,"main.html")