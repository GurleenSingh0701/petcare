import pyrebase
from django.http import HttpResponse


firebaseConfig = {

    " apiKey": "AIzaSyDOv_8gQB-zXAtQFNChjhd3Sd7_CFL1pow",

    "authDomain": "pythonproject-f841d.firebaseapp.com",

    "projectId": "pythonproject-f841d",

    "storageBucket": "pythonproject-f841d.appspot.com",

    "messagingSenderId": "534856973705",

    "appId": "1:534856973705:web:55ad2d3b75148b39eeb558"

}
firbase = pyrebase.initialize_app(firebaseConfig)
auth = firbase.auth()


def index(request):
    return HttpResponse("Hello, worlds.")
