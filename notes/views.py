from django.shortcuts import render,redirect,HttpResponseRedirect
from notes.models import Notes
# Create your views here.
def homepage(request):
    if str(request.user) == 'AnonymousUser':
        return redirect('accounts/login')
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            main = request.POST.get('main')
            notes_obj = Notes(title=title,main=main,user=request.user.profile)
            notes_obj.save()
            return HttpResponseRedirect(request.path_info)
        
        except Exception as e:
            print(e)

    if request.POST.get('search'):
        search = request.POST.get("search")
        print(search)
        notes = Notes.objects.filter(user= request.user.profile,title__icontains = search)
        context = {
            'notes':notes
        }
        return render(request,'homepage.html',context)  



    notes = Notes.objects.filter(user= request.user.profile)
    context = {
        'notes':notes
    }
    return render(request,'homepage.html',context)  

def delete_note(request,uid):
    note_obj = Notes.objects.get(uid=uid)
    note_obj.delete()
    return redirect('/')