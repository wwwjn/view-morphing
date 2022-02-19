import cv2
import numpy as np

# print(img.shape)

def get_user_click(path): 
    points = []
    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            xy = "%d,%d" % (x, y)
            cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0, 0, 0), thickness=1)
            cv2.imshow("image", img)
            points.append([x, y])
    
    img = cv2.imread(path)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    cv2.imshow("image", img)

    # waiting for user to get points
    while (True):
        if cv2.waitKey(20) & 0xFF == ord('q'): 
            cv2.destroyAllWindows()
            break

    print(points)
    return points


# points1 = get_user_click("data/einstein1.jpg")
# print(points1)
# points2 = get_user_click("data/einstein3.jpg")
# print(points2)

def get_user_click_two_images(path1, path2): 
    points = []
    points1 = []  # points in image1
    points2 = []  # points in image2
    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            xy = "%d,%d" % (x, y)
            cv2.circle(Hori, (x, y), 1, (255, 0, 0), thickness=-1)
            cv2.putText(Hori, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0, 0, 0), thickness=1)
            cv2.imshow("image", Hori)
            points.append([x, y])
    
    img1 = cv2.imread(path1)
    width = img1.shape[1]
    img2 = cv2.imread(path2)
    
    # horizontal concate the image together
    Hori = np.concatenate((img1, img2), axis=1)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    cv2.imshow("image", Hori)
    
    # waiting for user to get points
    while (True):
        if cv2.waitKey(20) & 0xFF == ord('q'): 
            cv2.destroyAllWindows()
            break


    for i in range(0, len(points)):
        point = points[i]
        if point[0] >= width:
            points2.append([point[0]-width, point[1]])
        else:
            points1.append(point)
    return points1, points2

# points1, points2 = get_user_click_two_images(path1 = 'data/einstein1.jpg', path2='data/einstein3.jpg')
# print(points1)
# print(points2)