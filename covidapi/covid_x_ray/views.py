from django.shortcuts import render,HttpResponse
import cv2
from keras.models import load_model


# Create your views here.
def index(request):
    if request.method == 'POST':
        return result(request)
    return render(request,'index.html')

def result(request):
    Answer = ''
    ig = request.POST.get('img')
    if not ig:
        Answer = 'Invalid Image'
    else:
        a = []
        lmodel = load_model("static/Covid_model_CNN.h5")
        IMG_W = 224
        IMG_H = 244
        img_array = cv2.imread(ig, cv2.IMREAD_GRAYSCALE)
        if img_array.ndim == 3:
            img_array = cv2.resize(img_array,(IMG_W,IMG_H))/255.0
            a.append(img_array)
            r = lmodel.predict_classes(a[:1])
            if r[0][0]==0:
                Answer = 'NEGATIVE'
            else:
                Answer = 'POSITIVE'
        else :
            Answer = 'Image must be 3 dimension x-ray'

    context = {
        'Answer' : Answer
    }
    return render(request,'result.html',context)
