from django.shortcuts import render
from calculator import modul


def calculator(request):
    error_msg = None
    result = None
    if request.method == "POST":
        try:
            float(request.POST["a"])
            float(request.POST["b"])
        except Exception:
            error_msg = "A or B isn't a number!"
            return render(request, "calculator/calculator.html", dict(error_msg=error_msg, result=result))

        if (float(request.POST["b"]) == 0) and (request.POST["operator"] == "/"):
            error_msg = "You can't divide by zero!"
            return render(request, "calculator/calculator.html", dict(error_msg=error_msg, result=result))
        if request.POST["operator"] == "+":
            result = modul.summary(request.POST["a"], request.POST["b"])
        elif request.POST["operator"] == "-":
            result = modul.subtraction(request.POST["a"], request.POST["b"])
        elif request.POST["operator"] == "*":
            result = modul.multiplication(request.POST["a"], request.POST["b"])
        elif request.POST["operator"] == "/":
            result = modul.division(request.POST["a"], request.POST["b"])
        else:
            error_msg = "Something went wrong. :("
            return render(request, "calculator/calculator.html", dict(error_msg=error_msg, result=result))
    return render(request, "calculator/calculator.html", dict(error_msg=error_msg, result=result))
