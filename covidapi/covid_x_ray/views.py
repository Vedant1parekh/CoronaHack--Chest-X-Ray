from django.shortcuts import render, HttpResponse
import cv2
from keras.models import load_model
import base64
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from .forms import ImageUploadForm
# Create your views here.
def handle_upload(f):
    with open('img.jpg','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def index(request):
    if request.method == "POST":
        return result(request)
    return render(request,'index.html')

def result(request):
    Answer="invalid_image"
    form =ImageUploadForm(request.POST,request.FILES)
    if form.is_valid():
        a=[]
        handle_upload(request.FILES['image'])
        lmodel = load_model("C:/Users/Dell/Desktop/Covid/covidapi/Covid_X_ray/static/Covid_model_CNN.h5")
        img_path="img.jpg"
        IMG_W = 224
        IMG_H = 224
        img=np.array(cv2.imread(img_path))
        img_array = np.array(cv2.resize(img,(IMG_W,IMG_H))/255.0)
        a.append([img_array,0])
        plt.imshow(img_array)
        plt.show()
        x_test=[]
        for k,j in a:
            x_test.append(k)
        x_test=np.array(x_test)
        r = lmodel.predict_classes(x_test)
        print('------------------------')
        print(r)
        if r[0][0]==0:
            Answer = 'NEGATIVE'
        else:
            Answer = 'POSITIVE'
    
    context = {
        'Answer' : Answer
    }
    return render(request,'C:/Users/Dell\Desktop/Covid/covidapi/Covid_X_ray/templates/result.html',context)
