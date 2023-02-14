from django.shortcuts import render,redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .forms import AddarticlesForm
from django.contrib import messages
from .models import Articles,Comment



def index(request):
    return render(request,'index.html')

def about(request):
    return render (request,'about.html')


@login_required(login_url='user:login')
def dashboard(request):
    articles=Articles.objects.filter(author=request.user)
    context={
        'articles': articles
    }
    return render(request,"dashboard.html",context)


@login_required(login_url='user:login')
def addarticles(request):
    form=AddarticlesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False) # commit=False yazdigimizda,django save etmir,ve biz author fieldimizi ora elave ede bilirik
        article.author=request.user # request.user - bize mekale elave etmek isteyen userin(giris yapmis) adini verir
        article=form.save()
        messages.success(request,'Mekaleniz basariyla eklendi...')
        return redirect('index')


    return render (request, "Addarticles.html",{'form':form}) # -bu bize Get request zamani template return edir,dict daxilindeki form ise bize sadece bow fieldleri  template-de cixarir

def detail(request,id):
    # article=Articles.objects.filter(id=id).first()
    article=get_object_or_404(Articles,id=id)  # get_object_or_404 -u eger bu id-li article varsa cixarsin,yoxsa 404 erroru versin deye istifade edirik
    comments=article.comments.all()# biz modelimizde related_name='comments' kodundan bu cur istifade ederek,butun commentlerimize cata bilerik
   
    return render(request,'detail.html',{'article':article,'comments':comments})

@login_required(login_url='user:login')
def update(request,id):
    article=get_object_or_404(Articles,id=id)
    form=AddarticlesForm(request.POST or None, request.FILES or None,instance=article)
    if form.is_valid():
        article=form.save(commit=False) # commit=False yazdigimizda,django save etmir,ve biz author fieldimizi ora elave ede bilirik
        article.author=request.user # request.user - bize mekale elave etmek isteyen userin(giris yapmis) adini verir
        article=form.save()
        messages.success(request,'Mekaleniz basariyla guncellendi...')
        return redirect('articles:dashboard')

        
    return render (request, "update.html",{'form':form}) 



@login_required(login_url='user:login')
def delete(request,id):
    article=get_object_or_404(Articles,id=id)
    article.delete()
    messages.success(request,'Makaleniz bawariyla silindi...')
    return redirect('articles:dashboard')

def articles(request):
    keyword=request.GET.get('keyword')
    if keyword: #  eger hansisa bir melumat search edilibse,o cixsin tempatede
        articles=Articles.objects.filter(title__contains=keyword) # burda title__contains -bize formdaki keywordun title-in daxilinde olub olmadigini yoxlayir
        return render(request,'articles.html',{'articles':articles})
    articles=Articles.objects.all()# eger search olunmayibsa,butun melumatlar gosterilsin
    return render(request,'articles.html',{'articles': articles})

def comment(request,id):
    article=get_object_or_404(Articles,id=id)

    if request.method=='POST':
        comment_author=request.POST.get('comment_author') #formlarda name-lere gore melumati gotururuk
        comment_content=request.POST.get('comment_content')
        new_comment=Comment(comment_author=comment_author,comment_content=comment_content,article=article) #ve yeni object yaradiriq
        new_comment.save()
    return redirect(reverse("articles:detail",kwargs={'id': id})) # bu cur yaziliw dinamic url sayilir