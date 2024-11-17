from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
import logging

from .forms import LoginUserForm, RegisterUserForm, RegisterPosterForm, SubmitApplicationForm, SignForPosterForm
from .models import Poster, User, Application
from .personal_exceptions import InvalidException
from logger_handlers import logger_info_join_page


@logger_info_join_page
def index(request):
    data = {'posters': Poster.objects.all()}
    return render(request, 'index.html', context=data)


@logger_info_join_page
class Posters(ListView):
    # data = {'posters': Poster.objects.all()}
    # return render(request, 'posters.html', context=data)
    model = Poster
    template_name = 'posters.html'
    context_object_name = 'posters'
    all_posters = Poster.objects.all()
    if not len(all_posters):
        logging.warning("'Posters' doesn't have posts, 'Posters' is empty.")
    extra_context = {
        'posters': Poster.objects.all(),
    }


@logger_info_join_page
def poster(request, post_slug):
    post = get_object_or_404(Poster, slug=post_slug)
    if request.method == 'POST':
        form = SignForPosterForm(request.POST)
        if form.is_valid():
            user = User.objects.get(nickname=request.COOKIES['nickname'])
            post.subscribers.add(user)
            return redirect('personal_account')
    else:
        form = SignForPosterForm()
    context = {'post': post, 'form': form}
    return render(request, 'poster.html', context=context)


@logger_info_join_page
def personal_account(request):
    try:
        user = User.objects.get(nickname=request.COOKIES['nickname'])
        applications = [application for application in Application.objects.filter(sender=user)]
        user_data = {
            'user': user,
            'created_events': user.created_events.all(),
            'applications': applications,
            'poster_subscribers': Poster.objects.filter(subscribers__nickname=request.COOKIES['nickname']),
        }
    except:
        return redirect('login_page')
    return render(request, 'personal_account.html', context=user_data)


@logger_info_join_page
def poster_redactor(request):
    if request.method == 'POST':
        form = RegisterPosterForm(request.POST)
        try:
            user = User.objects.get(nickname=request.COOKIES['nickname'])
            if form.is_valid():
                user.created_events.create(title=form.cleaned_data['title'],
                                   place=form.cleaned_data['place'],
                                   price=form.cleaned_data['price'],
                                   creator=request.COOKIES['nickname'],
                                   short_description=form.cleaned_data['short_description'],
                                   full_description=form.cleaned_data['full_description'],
                                   time_event=form.cleaned_data['time_event'])

                user.save()
                return redirect('posters')
            else:
                logging.warning(f"User '{user}' tried create event with invalid params.")
                raise InvalidException
        except:
            form.add_error(None, 'Не удалось создать обьявление')

    else:
        form = RegisterPosterForm()
    data = {'form': form}
    return render(request, 'poster_redactor.html', context=data)


@logger_info_join_page
def submit_application(request):
    # todo - страница с отправлением заявки модераторам
    if request.method == 'POST':
        form = SubmitApplicationForm(request.POST)
        user = User.objects.get(nickname=request.COOKIES['nickname'])
        if form.is_valid():
                application = Application(
                    sender=user,
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    call_time=form.cleaned_data['call_time']
                )
                application.save()
                return redirect('personal_account')
        else:
            logging.warning(f"User '{user}' tried submit invalid application.")
    else:
        form = SubmitApplicationForm()
    data = {'form': form}
    return render(request, 'submit_application.html', context=data)


@logger_info_join_page
def registration_page(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            try:
                if User.objects.filter(nickname=form.cleaned_data['nickname']):
                    raise Exception
                user = User(nickname=form.cleaned_data['nickname'],
                            password=form.cleaned_data['password'],
                            name=form.cleaned_data['name'],
                            surname=form.cleaned_data['surname'],
                            age=form.cleaned_data['age'],
                            hobby=form.cleaned_data['hobby'])
                user.save()
                rsp = redirect('personal_account')
                rsp.set_cookie('nickname', form.cleaned_data['nickname'])
                return rsp
            except:
                form.add_error(None, 'Пользователь с таким ником уже существует')
        else:
            logging.warning("User tried to register with invalid parameters.")
    else:
        form = RegisterUserForm()
    data = {'form': form}
    return render(request, 'registration_page.html', context=data)


@logger_info_join_page
def login_page(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(nickname=form.cleaned_data['nickname']):
                return redirect('registration_page')
            elif User.objects.filter(nickname=form.cleaned_data['nickname'])[0].password \
                    != form.cleaned_data['password']:
                logging.warning("User tried to login with invalid password.")
                form.add_error(None, 'Неправильно указан пароль')
            else:
                try:
                    User.objects.get(nickname=request.COOKIES['nickname'])
                    return redirect('personal_account')
                except:
                    rsp = redirect('index')
                    rsp.set_cookie('nickname', form.cleaned_data['nickname'])
                    return rsp
        else:
            logging.warning("User tried to login with invalid parameters.")

    else:
        form = LoginUserForm()
    return render(request, 'login_page.html', context={'form': form})