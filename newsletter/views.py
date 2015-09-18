from django.shortcuts import render

from .forms import ContactForm, SignUpForm

# Create your views here.


def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)
    # if request.user.is_authenticated():
    #     title = "My Title %s" % request.user

    # add a form
    # if request.method == "POST":
    #     print(request.POST)
    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():
        # form.save()
        # print(request.POST['email']  NOT recommended as no cleaning is done.
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name

        # if not instance.full_name:
        #   instance.full_name = "Justin"
        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key, value in form.cleaned_data.items():
            # in Python3 .iteritems() has been changed to .items()
            print(key, value)
            # print(form.cleaned_data.get(key))
        # email = form.cleaned_data.get("email")
        # message = form.cleaned_data.get("message")
        # full_name = form.cleaned_data.get("full_name")
        # print(email, message, full_name)
    context = {
        "form": form,
    }

    return render(request, "forms.html", context)
