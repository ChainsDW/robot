from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe
import json
import base64
import os
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main(request):
    return render(request, 'video.html')


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


i = 0


def video(request):
    if request.method == 'POST':
        obj = request.POST.get('img')
        date = obj.split(',')[1]
        img = base64.b64decode(date)
        global i
        # with open('{0}/static/img/{1}.jpg'.format(BASE_DIR, i), 'wb') as f:
        #     f.write(img)
        i = i + 1
        return HttpResponse(json.dumps('ok'))
    return render(request, 'video&audio.html')


def index(req):
    return render(req, 'index.html')


def to_video():
    import cv2
    import glob as gb
    img_root = gb.glob('{0}/static/img/*.jpg'.format(BASE_DIR))
    videoWriter = cv2.VideoWriter('{0}/static/video/test.mp4'.format(BASE_DIR), cv2.VideoWriter_fourcc(*'MJPG'), 25, (640, 480))
    for path in img_root:
        img = cv2.imread(path)
        img = cv2.resize(img, (640, 480))
        videoWriter.write(img)


def recorder(request):
    return render(request, 'recorderview.html')

if __name__ == '__main__':
    to_video()