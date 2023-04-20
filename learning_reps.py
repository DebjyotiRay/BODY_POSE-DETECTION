from installations import *
from angle_calculator import *
from cvzone.PoseModule import PoseDetector
cap = cv2.capture(0)

cnt=0
stage = None


detector = PoseDetector(detectionCon=0.69)
while True:
    ret, frame = cap.read()
    image = detector.findPose(frame)

    llmst, bbox = detector.findPosition(image, draw=False)

    if llmst:
        print(llmst)

    cv2.imshow("BICEPS CURLS",image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break



# while mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
#     while cap.isOpened():
#         ret, frame = cap.read()


        image = cv2.cvtColor(frame, )


