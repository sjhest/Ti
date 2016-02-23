from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import models
from models import Comment, Issue
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@login_required
def index(request):
    issue_list = models.Issue.objects.all()
    return render_to_response('Tiapp/index.html', {'issue_list': issue_list})

@login_required
def issue(request, issue_id):
    issue = models.Issue.objects.get(id=issue_id)
    comments = models.Comment.objects.filter(issue_id=issue_id).order_by('-created_time')
    return render_to_response('Tiapp/issue.html', {'issue': issue, 'comments':comments},context_instance = RequestContext(request))

@login_required
def post_comment(request):
    issue_id = request.POST.get('issue_id')
    #print issue_id
    content = request.POST.get('content')
    comment_user = models.Ti_user.objects.get(id=request.user.id)
    issue = models.Issue.objects.get(id=issue_id)
    comment = Comment(content=content, issue=issue, comment_user=comment_user)
    comment.save()
    return HttpResponseRedirect('/issue/%s' %issue_id)

@login_required
def new_issue(request):
    all_Department = models.Department.objects.all()
    print all_Department
    return render_to_response('Tiapp/new_issue.html', {'all_Department': all_Department}, context_instance = RequestContext(request))

@login_required
@csrf_protect
def save_issue(request):
    requester = models.Ti_user.objects.get(id=request.user.id)
    title = request.POST.get('title')
    description = request.POST.get('description')
    severity = request.POST.get('severity')
    department = models.Department.objects.get(department_name=request.POST.get('department'))
    issue = Issue(title = title, description = description, requester = requester, assigned_group = department, Severity = severity)
    issue.save()
    print issue.id
    comments = models.Comment.objects.filter(issue_id=issue.id).order_by('-created_time')
    return HttpResponseRedirect('/issue/%s' %issue.id)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')