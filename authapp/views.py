from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from authapp.models import ShopUser
from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserRegisterForm
from django.contrib import auth

def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])    

    title = f'Подтверждение учетной записи {user.username}'

    message = f'Для подтверждения учетной записи {user.username} на портале \ {settings.DOMAIN_NAME} перейдите по ссылке:\n{settings.DOMAIN_NAME}{verify_link}'
    
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def register(request):
    title = 'регистрация'
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('сообщение подтверждения отправлено')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('auth:login'))
        else:
            register_form = ShopUserRegisterForm()
            content = {'title': title, 'register_form': register_form}
            return render(request, 'authapp/register.html', content)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'error activation user : {e.args}')
        return HttpResponseRedirect(reverse('main'))
