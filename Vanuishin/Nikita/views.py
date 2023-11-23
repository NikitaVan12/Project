from django.shortcuts import render
from django.http import HttpResponse


def full_name(request, name, age, interesting):
    return HttpResponse(f"""
            <h1>{name}</h1>
            <h2>{age}</h2>
            <h3>{interesting}<h3>
""")


def about(request, resp, city):
    return HttpResponse(f"""
        <p>{resp}</p>
        <p1>{city}</p1>
""")

def Contacks(request, Contacks):
    return HttpResponse(f"""
        <h1>{Contacks}</h1>
""")
