from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import BookOrd
from .form import BookOrdForm


def tbord(request):
    # tbords = BookOrd.objects.all().order_by('-id')
    if request.method == 'POST':
        stulevel = request.POST.get('stulevel')
        coursetitle = request.POST.get('coursetitle')
        tbname = request.POST.get('tbname')
        tbversion = request.POST.get('tbversion')
        tbpublish = request.POST.get('tbpublish')
        tbauthor = request.POST.get('tbauthor')
        tbisbn = request.POST.get('tbisbn')
        tbpurpose = request.POST.get('tbpurpose')
        tbfteach = request.POST.get('tbfteach')
        value = {'stulevel': stulevel, 'coursetitle': coursetitle, 'tbname': tbname, 'tbversion': tbversion,
                 'tbpublish': tbpublish, 'tbauthor': tbauthor, 'tbisbn': tbisbn, 'tbpurpose': tbpurpose,
                 'tbfteach': tbfteach,'teachingtask_id': 1}
        BookOrd.objects.create(**value)
        kwargs = {'id': 1}
        return redirect(request, 'index.html', locals())
    else:
        return render(request, 'tbord.html', locals())


def tblist(request):
    tblists = BookOrd.objects.all().order_by('-id')
    return render(request, 'tblist.html', locals())

def tbord(request):
    # tbords = BookOrd.objects.all().order_by('-id')
    if request.method == 'POST':
        tbform = BookOrdForm(request.POST)
        if tbform.is_valid():
            new_tbp = tbform.save(commit=False)
            new_tbp.stulevel = tbform.cleaned_data['stulevel']
            new_tbp.coursetitle = tbform.cleaned_data['coursetitle']
            new_tbp.tbname = tbform.cleaned_data['tbname']
            new_tbp.tbversion = tbform.cleaned_data['tbversion']
            new_tbp.tbpublish = tbform.cleaned_data['tbpublish']
            new_tbp.tbauthor = tbform.cleaned_data['tbauthor']
            new_tbp.tbisbn = tbform.cleaned_data['tbisbn']
            new_tbp.tbpurpose = tbform.cleaned_data['tbpurpose']
            new_tbp.tbfteach = tbform.cleaned_data['tbfteach']
            # new_tbp.teachingtask_id = tbform.cleaned_data['teachingtask']
            new_tbp.save()
            return redirect(request, 'index.html', locals())
        else:
            return HttpResponse("输入内容有误，请重新填写。")
    else:
        return render(request, 'tbord.html', locals())
