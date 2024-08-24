import cv2

# Load the Haar cascades
cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cascade_smile = cv2.CascadeClassifier('haarcascade_smile.xml')

# Check if the cascades are loaded correctly
if cascade_face.empty() or cascade_smile.empty():
    print("Error loading cascade classifiers")
    exit(0)

# Start video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

while True:
    ret, img = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert to grayscale
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    f = cascade_face.detectMultiScale(
        g,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in f:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        gray_r = g[y:y + h, x:x + w]

        # Detect smiles
        s = cascade_smile.detectMultiScale(
            gray_r,
            scaleFactor=1.5,
            minNeighbors=15,
            minSize=(25, 25)
        )

        if len(s) > 0:  # If a smile is detected
            cv2.putText(img, "SMILING", (x, y - 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                        2, cv2.LINE_AA)

    cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # Escape key to exit
        break

cap.release()
cv2.destroyAllWindows()
