#coding: utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.db.models import Count
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, RequestContext
from django.template.loader import get_template, render_to_string
from blog.models import Chapter, Article, Commentary
from blog.forms import FeedbackForm, RegistrationForm
from django.contrib.auth.models import User, UserManager

def chapter_index(request):
    chapters = Chapter.objects.annotate(Count('actual'))
    return render(request, 'chapters.html', locals())


def title(request, OTETO_S_URLA):
    article = Article.objects.get(id=OTETO_S_URLA)
    form1111 = FeedbackForm()
    if request.method == "POST":
        #q=1
        form1111 = FeedbackForm(request.POST)
        if form1111.is_valid():
            obj = Commentary(
                comment_text=form1111.data['new_comment'],
                user=request.user,
                #user_id=request.user.id,
                article_id=OTETO_S_URLA
                #article=article
            )
            obj.article_id = OTETO_S_URLA
            obj.article=article
            obj.save()
            form1111 = FeedbackForm()
        ##raise ValueError(request.POST['new_comment'])
        #    if request.method == "POST":
        #    #q=1
        #    obj = Commentary(
        #        comment_text=request.POST['new_comment'],
        #        user=request.user,
        #        #user_id=request.user.id,
        #        article_id=OTETO_S_URLA
        #        #article=article
        #    )
        #    obj.article_id = OTETO_S_URLA
        #    obj.article=article
        #    obj.save()
        #    #raise ValueError(request.POST['new_comment'])

    comments = article.commentary_set.all()
    comments = Commentary.objects.filter(article_id=article.id)
    return render(request, 'article.html', locals())


def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            print 'user active'
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)
            # Перенаправление на "правильную" страницу
            return render(request, 'chapters.html', locals())
        else:
            # Отображение страницы с ошибкой
            return render(request, "registration/login.html", locals())

    return render(request, 'registration/login.html', locals())


def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return render(request, 'registration/login.html', locals())


def registration(request):
    form2 = RegistrationForm()
    if request.method == "POST":
        print 11111
        form2 = RegistrationForm(request.POST)
        print form2.errors
        if form2.is_valid():
            user = User.objects.create_user(
                username = request.POST['login'],
                first_name = request.POST['name'],
                last_name = request.POST['surname'],
                email = request.POST['sender'],
                password = request.POST['password']
            )
            user.save()
    #            print 1111111111
    #            print User.objects.filter(user=user).exists()
            return render(request, 'chapters.html', locals())
    return render(request, "registration/registration.html", locals())