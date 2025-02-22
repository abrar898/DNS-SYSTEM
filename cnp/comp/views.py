# views.py
from django.shortcuts import  get_object_or_404
from django.shortcuts import render, redirect
from .models import React

def react_form(request):
    if request.method == 'POST':
        # Get data from the form
        domain_name = request.POST.get('DomainName')
        ip_address = request.POST.get('IPAddress')
        react_class = request.POST.get('Class')
        # Save the data to the database
        React.objects.create(DomainName=domain_name, IPAddress=ip_address, Class=react_class)
        # Redirect to the table view after saving data
        return redirect('react-table')

    return render(request, 'react_form.html')

def react_table(request):
    # Fetch all React objects from the database
    react_objects = React.objects.all()
    # Render the data as a table in an HTML template
    return render(request, 'react_table.html', {'react_objects': react_objects})


def home(request):
    react_objects = React.objects.all()
    return render(request, 'homepage.html', {'react_objects': react_objects})
# def search(request):
#     react_objects = React.objects.all()
#     return render(request, 'search_form.html', {'react_objects': react_objects})

# Delete view to remove a React object
def react_delete(request, react_id):
    # Get the React object to delete
    react = get_object_or_404(React, id=react_id)

    # Check if the request method is POST to confirm the deletion
    if request.method == "POST":
        react.delete()  # Delete the React object
        return redirect('react-table')  # Redirect to the list of React objects (or any other page)

    return render(request, 'react_delete.html', {'react': react})



def search_results(request):
    search_query = request.POST.get('search_query', '')  # Get search query from the form
    results = []

    if search_query:
        # Filter results based on the search query
        results = React.objects.filter(
            DomainName__icontains=search_query) | React.objects.filter(
            IPAddress__icontains=search_query)

    return render(request, 'search-result.html', {'results': results, 'search_query': search_query})



def search(request):
    message = ""
    if request.method == 'POST':
        # Get and clean input values
        domain_name = request.POST.get('DomainName', '').strip()
        ip_address = request.POST.get('IPAddress', '').strip()

        # Case 1: Both Domain Name and IP Address provided
        if domain_name and ip_address:
            try:
                # Update IP Address for the given Domain Name
                record = React.objects.get(DomainName=domain_name)
                record.IPAddress = ip_address
                record.save()
                message = f"IP Address updated for Domain Name: {domain_name}"
            except React.DoesNotExist:
                message = f"Domain Name '{domain_name}' not found."

        # Case 2: Only IP Address provided, updating Domain Name
        elif ip_address:
            try:
                # Ensure Domain Name is provided for update
                # if not domain_name:
                #     message = "Domain Name cannot be empty when updating for an IP Address."
                # else:
                    # Update Domain Name for the given IP Address
                    record = React.objects.get(IPAddress=ip_address)
                    record.DomainName = domain_name
                    record.save()
                    message = f"Domain Name updated for IP Address: {ip_address}"
            except React.DoesNotExist:
                message = f"IP Address '{ip_address}' not found."

        # Case 3: Neither field provided
        else:
            message = "Please provide both Domain Name and IP Address."

    # Render the form and message
    return render(request, 'search_form.html', {'message': message})
