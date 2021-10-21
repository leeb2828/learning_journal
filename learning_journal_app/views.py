from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required # login required
from .models import Post 


@login_required
def index(request):
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'learning_journal_app/index.html', context)


def new(request):
    if request.method == 'POST':
        data = request.POST

        title = data['title']
        date = data['date']
        timespent = data['timeSpent']
        what_i_learned = data['whatILearned']
        author = request.user
        

        exists = Post.objects.filter(title=title, date=date)
        if exists:
            print('Already exists')
        else:
            print('Does not exist')
            new_post = Post(title=title, date=date, timespent=timespent, what_i_learned=what_i_learned, author=author)
            check_if_exists = Post.objects.filter(title=title, date=date)
            new_post.save()
            
        return redirect('index')

        
    return render(request, 'learning_journal_app/new.html')


def detail(request, title, date):
    current_post = Post.objects.filter(title=title, date=date)
    
    if current_post:
        current_post_dict = {
            'id': str(current_post[0].author),
            'title': str(current_post[0].title),
            'date': current_post[0].date, 
            'timespent': str(current_post[0].timespent),
            'what_i_learned': str(current_post[0].what_i_learned),
            'author_id': current_post[0].author_id,
            'author': str(current_post[0].author)
        }
        
        context = {
            'post': current_post_dict,
        }
       
        return render(request, 'learning_journal_app/detail.html', context)
    else:
        return redirect('index')




def check_author(post_author, current_user):
    if post_author == current_user:
        return True 
    return False
    


def edit(request, title, date):
    if request.method == 'POST':
        data = request.POST
        edit_post = {}

        edit_title = data['title']
        edit_date = data['date']
        edit_timespent = data['timeSpent']
        edit_what_i_learned = data['whatILearned']

        
        # Retrieve all post objects
        all_objects = Post.objects.all()
        # Locate the correct post object and make modifications
        for obj in all_objects:
            if obj.get_title() == title and obj.get_date() == date and check_author(obj.author, request.user):
                if edit_title:
                    obj.title = edit_title
                elif edit_date:
                    obj.date = edit_date
                elif edit_timespent:
                    obj.timespent = edit_timespent
                elif edit_what_i_learned:
                    obj.what_i_learned = edit_what_i_learned
                obj.save()
                break
        return redirect('index')
        
    context = {
        'title': title,
        'date': date
    }
    return render(request, 'learning_journal_app/edit.html', context)


def delete(request, title, date):
    post_to_delete = Post.objects.get(title=title, date=date)
    post_to_delete.delete()

    return redirect('index')


