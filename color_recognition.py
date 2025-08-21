import cv2
import numpy as np

# افتح الفيديو 
cap = cv2.VideoCapture("855474-hd_1920_1080_24fps.mp4")

# تحديد نطاق اللون الأحمر بالـ HSV
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break  # يوقف إذا خلص الفيديو

    # تحويل من BGR إلى HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # نعمل Mask للون الأحمر
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # نطلع الأجزاء اللي فيها اللون الأحمر
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # نعرض الفريم الأصلي + الناتج
    cv2.imshow("Original", frame)
    cv2.imshow("Red Detection", result)

    # إذا ضغطت q يوقف
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

