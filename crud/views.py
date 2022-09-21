from django.shortcuts import render,redirect
from .models import Emp

def home(request):
    return render(request,'crud/home.html')


def add_emp(request):
    if request.method == "GET":
        get_emp = Emp.objects.all()
        return render(request, "crud/form.html", {"get_items": get_emp})

    if request.method=='POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact= request.POST.get("contact")
        age = request.POST.get("age")
        description = request.POST.get("desc")

        print("None value of req is : ", request.POST.get("abcd"))

        print(request.POST)

        Emp.objects.create(
            name = name,
            email= email,
            contact=contact,
            age=age,
            description = description,
        )

        return redirect('homepage')

def emp_list(request):
    if request.method=="GET":
        el=Emp.objects.all()
        return render(request,"crud/emplist.html",{'el':el})

def delete_emp(request):
    if request.method == "POST":

        get_data = request.POST['delete']
        Emp.objects.filter(id=get_data).delete()

        return redirect('employee_list')



def update_emp(request, id):

    if request.method == "GET":

        get_obj = Emp.objects.get(id=id)
        return render(request, "crud/update.html", {'emp': get_obj})

    if request.method == "POST":

        get_id = request.POST['update']
        get_obj = Emp.objects.get(id=get_id)

        get_obj.name = request.POST['name']    
        get_obj.email = request.POST['email']
        get_obj.contact = request.POST['contact']
        get_obj.age = request.POST['age']
        get_obj.description = request.POST['description']

        get_obj.save()

        return redirect('employee_list')

