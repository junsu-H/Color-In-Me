from flask import request

def face_detection(f, fn):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('static/haarcascade_frontalface_default.xml')
    
    # Read the input image

    # windows \\

    if fn.split('\\')[-2:][0] == 'static':

        img = cv2.imread(fn.split('\\')[-2:][0] + "\\" + fn.split('\\')[-2:][1])
        # liunx / 
        # img = cv2.imread(fn.split('/')[-2:][0] + "/" + fn.split('/')[-2:][1])

        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        crop_face = 0
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            crop_face = img[y:y+h, x:x+w]
        
        # windows \\
        cv2.imwrite(fn.split('\\')[-2:][0] + "\\" + "face_" + fn.split('\\')[-2:][1], crop_face)
        
        # linux /
        # cv2.imwrite(fn.split('/')[-2:][0] + "/" + "face_" + fn.split('/')[-2:][1], crop_face)
    else:
        print("error")