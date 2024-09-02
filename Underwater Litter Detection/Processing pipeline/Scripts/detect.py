import cv2 as cv
from ultralytics import YOLO

model = YOLO('Object_detection_and_pose_estimation_pipeline/yolo/sodacanModel.pt')

# results = model(frame, conf=0.5)
image_path = '/home/mscrobotics2324laptop5/Course/Dissertation/Underwater Litter detector/Assets/DatasetGenerator/Dataset/sodacan/image_0012.png'
results = model.predict(image_path, conf = 0.4, save=True)


boxes = results[0].boxes.xyxy.tolist()[0]
# print(boxes)
x_center = (boxes[0] + boxes[2]) / 2
y_center = (boxes[1] + boxes[3]) / 2

print(x_center, y_center)

# annotated_frame = results[0].plot()

image = cv.imread(image_path)
cv.imshow('image', image)

cv.waitKey(0)
cv.destroyAllWindows()
