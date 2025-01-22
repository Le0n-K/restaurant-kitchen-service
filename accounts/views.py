from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import (
    get_current_site_safely,
    generate_activation_data,
    send_activation_email
)
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import DetailView

from accounts.forms import RegisterForm
from accounts.services.token_service import account_activation_token
from messanger.forms import MessageForm
from messanger.models import Message
from restaurant.settings.base import ACCOUNT_EMAIL_VERIFICATION

User = get_user_model()


def create_inactive_user(form):
    """
    Create an inactive user from the form data.
    """
    user = form.save(commit=False)
    user.is_active = not ACCOUNT_EMAIL_VERIFICATION
    user.save()
    return user


def handle_user_activation(request, user):
    """
    Handle the user activation process if required.
    """
    if ACCOUNT_EMAIL_VERIFICATION:
        try:
            domain = get_current_site_safely(request).domain
            uid, token = generate_activation_data(user)
            send_activation_email(user, domain, uid, token)
            messages.info(request, "Please confirm your email to activate your account.")
        except Exception as e:
            messages.error(request, "There was an error sending the activation email. Please try again later.")
    else:
        messages.success(request, "Your account has been created successfully. You can now log in.")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = create_inactive_user(form)
            handle_user_activation(request, user)
            return redirect("accounts:login")
        else:
            form = RegisterForm()
        return render(
            request,
            "registration/register.html",
            {"form": form}
        )


def activate(request, uid, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if not ACCOUNT_EMAIL_VERIFICATION:
        return HttpResponse("Email verification is not required for this site.")

    if user is not None and not user.is_active:
        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse("Thank you for your email confirmation."
                                "Now you can login to your account.")
        else:
            return HttpResponse("Activation link is invalid!")
    elif user is not None and user.is_active:
        return HttpResponse("Your account is already activated.")
    else:
        return HttpResponse("Activation link is invalid!")


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = "registration/user_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = Message.objects.filter(user=self.object)
        context["message_form"] = MessageForm()
        return context
