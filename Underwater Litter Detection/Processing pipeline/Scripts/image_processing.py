import cv2
import os
print(int(float('4.9')))
def draw_bounding_boxes(image_folder, bbox_folder, output_folder):
    counter = 0
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for image_name in os.listdir(image_folder):
        if image_name.endswith('.png'):
            image_path = os.path.join(image_folder, image_name)
            bbox_path = os.path.join(bbox_folder, image_name.replace('.png', '.txt'))
            output_path = os.path.join(output_folder, image_name)

            # Load image
            image = cv2.imread(image_path)
            print('shape', image.shape)

            # Load bounding box
            with open(bbox_path, 'r') as f:
                bbox_data = f.read().strip().split(',')
                # print(bbox_data)4
                x, y, width, height = map(int, map(float, bbox_data))
                # print('params: ', x,y,width,height)


            # Draw bounding box
            top_left = (x, y)
            bottom_right = (x + width, y + height)
            image = cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

            # Save the image with bounding box
            # cv2.imwrite(output_path, image)
            # print(f"Processed and saved: {output_path}")
            counter+=1
    


if __name__ == "__main__":
    image_folder = 'Assets/DatasetGenerator/Dataset/mug'
    bbox_folder = 'Assets/DatasetGenerator/Dataset/mug'
    output_folder = 'Assets/DatasetGenerator/Annotated/sodacan'

    draw_bounding_boxes(image_folder, bbox_folder, output_folder)
