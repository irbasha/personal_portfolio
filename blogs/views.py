from django.shortcuts import render
from .models import Post, Category, Comment
from .forms import CommentForm

def blog_index(request):
	blogs = Post.objects.all()
	return render(request, 'blog_index.html', {'blogs': blogs})

def blog_category(request, category):
	blogs = Post.objects.filter(categories__name__contains=category)
	return render(request, 'blog_category.html', {'blogs': blogs})

def blog_detail(request, bin):
	blog = Post.objects.get(id=bin)
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(
				author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=blog
            )
		comment.save()
	comments = Comment.objects.filter(post=blog)
	return render(request, 'blog_detail.html', {'blog': blog, 'comments':comments, 'form': form})

