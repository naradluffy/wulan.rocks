from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from django.core.mail import send_mail

from .forms import CommentForm, ContactForm

from .models import Project, Comment, Category, Picture, Contact

from .myscript import HelloWorld

def index(request):
	
	##latest_project_list = Project.objects.annotate(num_comment=Count('comment')).order_by('-pub_date')[:10]
	latest_project_list = Project.objects.all().order_by('-pub_date')
	paginator = Paginator(latest_project_list,10)
	
	page = request.GET.get('page')
	latest_projects = paginator.get_page(page)
		
	#categories
	cat_list = Category.objects.all().order_by('cat_name')
	
	context = { 'latest_project_list':latest_projects,'cat_list':cat_list,'mytest':HelloWorld}

	return render(request,'articles/index.html', context)
	
def detail(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	cat_list = Category.objects.all().order_by('cat_name')
	comment_list = Comment.objects.filter(project_id=project_id).order_by('pub_date')
	picture_list = Picture.objects.filter(project_id=project_id)
	
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = CommentForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			save_comment = Comment(	name=form.cleaned_data['name'], 
									email=form.cleaned_data['email'],
									message=form.cleaned_data['message'],
									project_id=project_id)
			save_comment.save()
			
			# reset form
			form = CommentForm()
			
			com_message = "Thank you for your comment!"
			# redirect to a new URL:
			# return HttpResponseRedirect('/thanks/')
		else:
			com_message = "Please edit your comment."

	# if a GET (or any other method) we'll create a blank form
	else:
		form = CommentForm()
		com_message = "Please tell us what do you think :)"
	
	category_list = Project.objects.get(id=project_id)
	
	context = {	'project': project,
				'num_comment': Comment.objects.filter(project_id=project_id).count(),
				'comment_list': comment_list,
				'category_list':category_list.categories.all(),
				'form': form, 
				'com_message':com_message,
				'cat_list':cat_list,
				'picture_list': picture_list,}
	
	return render(request, 'articles/detail.html', context)

def category(request, category_id):
	latest_project_list = Project.objects.filter(categories=category_id).order_by('-pub_date')
	paginator = Paginator(latest_project_list,10)
	
	page = request.GET.get('page')
	latest_projects = paginator.get_page(page)
		
	#categories
	cat_list = Category.objects.all().order_by('cat_name')
	what_cat = Category.objects.get(pk=category_id)
	
	context = { 'latest_project_list':latest_projects,'cat_list':cat_list,'what_cat':what_cat}

	return render(request,'articles/category.html', context)

def contact(request):
	cat_list = Category.objects.all().order_by('cat_name')
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			save_contact = Contact(	email=form.cleaned_data['email'],
									subject=form.cleaned_data['subject'],
									message=form.cleaned_data['message']
									)
			save_contact.save()
			new_string = "%s send you a message. This is the message: %s Reply him/her quickly!" %(form.cleaned_data['email'],form.cleaned_data['message'])
			send_mail(
				'Automatic Reply from Wulan.rocks',
				'Hi, \n\nThank you for sending us email. We will reply you soon!\n\nBest Regards,\nSri Ratna Wulan',
				form.cleaned_data['email'],
				[form.cleaned_data['email']],
				fail_silently=False,
			)
			
			send_mail(
				"You've got a message!",
				new_string,
				form.cleaned_data['email'],
				['naradluffy@gmail.com'],
				fail_silently=False,
			)
			
			
			# reset form
			form = ContactForm()
			
			com_message = "Thank you for contacting me!"
			# redirect to a new URL:
			# return HttpResponseRedirect('/thanks/')
		else:
			com_message = "Hm, something is wrong."

	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactForm()
		com_message = "Contacts"
	
	context = {	'form': form, 
				'com_message':com_message,
				'cat_list':cat_list,
				}
	
	return render(request, 'articles/contact.html', context)

def about(request):
	cat_list = Category.objects.all().order_by('cat_name')
	
	context = {	'cat_list':cat_list,
				}
				
	return render(request, 'articles/about.html', context)
