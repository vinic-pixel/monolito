from django.shortcuts import render


def indexView(request):

    return render(request, 'home.html')

def buildView(request):
    print("Build view called!")

    return render(request, 'build.html')

def cartView(request):
    print("Cart view called!")

    if request.method == 'POST':
        print("Your name is: ", request.POST['name'])
    return render(request, 'cart.html')
