from django.shortcuts import render
from .forms import ChatForm
from .nlp_utils import process_user_input

def chat_view(request):
    response = ""
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data["user_message"]
            response = process_user_input(user_message)
    else:
        form = ChatForm()

    return render(request, "chatbot/chat.html", {"form": form, "response": response})
