from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm


@login_required
def message_list(request):
    messages = Message.objects.filter(user=request.user)
    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect("messanger:message_list")

    context = {
        "messages": messages,
        "form": form,
    }
    return render(request, "messanger/message_list.html", context)


@login_required
def delete_message(request, message_id):
    message = Message.objects.get(id=message_id, user=request.user)
    message.delete()
    return redirect("messanger:message_list")
