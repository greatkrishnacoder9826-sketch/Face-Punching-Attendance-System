 # Face Image Detection

import pandas as pd

try:
    df = pd.read_csv(
        r"C:\MACHINE LEARNING PROJECTS\Face Puching - Open CV\Book1.csv"
    )
except:
    df = pd.DataFrame(columns=["id", "Name"])

import cv2

face_cascade = cv2.CascadeClassifier(
    r"C:\MACHINE LEARNING PROJECTS\Face Puching - Open CV\haarcascade_frontalface_default (1).xml"
)

cam = cv2.VideoCapture(0)

id = input("Enter your id: ")
name = input("Enter your name: ")

df2 = pd.DataFrame({
    "id": [id],
    "Name": [name]
})

df = pd.concat([df, df2]).drop_duplicates().reset_index(drop=True)

df.to_csv(
    r"C:\MACHINE LEARNING PROJECTS\Face Puching - Open CV\Book1.csv",
    index=False
)

sampleNum = 0

while True:
    ret, img = cam.read()

    faces = face_cascade.detectMultiScale(img, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (144, 1, 1), 3)

        sampleNum += 1

        cv2.imwrite(
            r"C:\MACHINE LEARNING PROJECTS\Face Puching - Open CV\faces\\"
            + str(id) + "." + str(sampleNum) + ".jpg",
            img[y:y+h, x:x+w]
        )

    cv2.imshow("Face", img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    elif sampleNum > 10:
        break

cam.release()
cv2.destroyAllWindows()