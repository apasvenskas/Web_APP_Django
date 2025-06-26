# views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # This block handles the form submission (the POST request)
    if request.method == 'POST':
        # Retrieve the submitted data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        # ... get other form fields ...

        # Process the data (e.g., save to database)
        print(f"Processing application for {first_name} {last_name}...")

        # Return a success message
        return HttpResponse("<h1>Thank you! Your application has been submitted.</h1>")

    # This line handles initially displaying the page (the GET request)
    return render(request, "index.html")