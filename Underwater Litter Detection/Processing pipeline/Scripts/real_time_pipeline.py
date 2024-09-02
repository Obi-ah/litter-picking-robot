import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO

model = YOLO('Object_detection_and_pose_estimation_pipeline/yolo/litterModel.pt')



class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(
            Image,
            '/blurov/rgb_camera',  # Change this to your image topic
            self.listener_callback1,
            100)       
         
        self.subscription = self.create_subscription(
            Image,
            '/blurov/sonar',  # Change this to your image topic
            self.listener_callback2,
            10)
        # self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()
        self.counter= 1
        self.capturemode = False



    def listener_callback1(self, msg):
        # Convert ROS Image message to OpenCV format
        self.rgb_frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')



         # Run YOLOv8 on the frame
        results = model.predict(self.rgb_frame, conf=0.65, verbose = False)


        if results[0].boxes.xyxy.tolist():
            boxes = results[0].boxes.xyxy.tolist()[0]

            # print(boxes)
            self.x_center = (boxes[0] + boxes[2]) / 2
            self.y_center = (boxes[1] + boxes[3]) / 2

        # Display the results on the frame
        self.annotated_frame = results[0].plot()

        if self.counter <= 5 and self.capturemode:
            print('hii')
            cv2.imwrite(f'sonar_frame_{self.counter}.jpg', self.sonar_frame)
            cv2.imwrite(f'camera_frame_{self.counter}.jpg', self.annotated_frame)
            self.counter +=1

        # Show the annotated frame in a window
        cv2.imshow('Camera Stream', self.annotated_frame)

        cv2.waitKey(1)


    def listener_callback2(self, msg):


        # Convert ROS Image message to OpenCV format
        self.sonar_frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                self.counter = 1
                self.capturemode = True

                self.sonar_distance = compute_sonar_distance(x, y, self.sonar_frame.shape[0:2])

                self.position_3d = compute_3d_position(self.x_center, self.y_center, self.rgb_frame.shape[0:2], self.sonar_distance)

                print('sonar distance: ', self.sonar_distance)
                print('position: ', self.position_3d)


        cv2.namedWindow("sonar stream")
        cv2.imshow('sonar stream', self.sonar_frame)
        cv2.setMouseCallback('sonar stream', click_event)
        cv2.waitKey(1)



def compute_3d_position(x_centre, y_centre, image_shape, sonar_distance):
    image_width = image_shape[0]
    image_height = image_shape[1]

    sensor_width = 24

    cx = image_width/2
    cy = image_height/2


    f_mm = 31.17691
    f_pixel = (f_mm*image_width)/sensor_width
    print(f_pixel)


    s_x = cx - x_centre
    s_y = cy - y_centre

    a = (f_pixel**2 + s_x**2)**0.5
    f_o = (a**2 + s_y**2)**0.5

    X = sonar_distance * (s_x/f_o)
    Y = sonar_distance * (s_y/f_o)
    Z = sonar_distance * (f_pixel/f_o)

    return (X,Y,Z)



def compute_sonar_distance(x_centre, y_centre, image_shape):
    max_distance = 30  

    # Get the dimensions of the image
    height, width = image_shape

    origin_y = height -1 # y-coordinate of the vertex (bottom of the image)

    # Calculate the distance as a proportion of the total height
    distance = ((origin_y - y_centre) / height * max_distance)+1

    return distance




def main(args=None):
    rclpy.init(args=args)

    image_subscriber = ImageSubscriber()

    try:
        rclpy.spin(image_subscriber)
    except KeyboardInterrupt:
        pass

    # Destroy the node explicitly (optional)
    image_subscriber.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()



