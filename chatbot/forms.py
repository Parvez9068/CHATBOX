from django import forms

class ChatForm(forms.Form):
    user_message = forms.CharField(
        label="Your Message",
        widget=forms.TextInput(attrs={"placeholder": "Type your message here...", "class": "form-control"})
    )
