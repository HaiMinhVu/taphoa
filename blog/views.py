from django.shortcuts import render

posts = [
	{
		'author' : 'hai',
		'title' : 'blog post 1',
		'content' : 'content 1',
		'date_posted': '06/04/2020'
	},
	{
		'author' : 'vu',
		'title' : 'blog post 2',
		'content' : 'content 2',
		'date_posted': '06/03/2020'
	}
]

def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})


