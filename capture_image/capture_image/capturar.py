import rclpy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from rclpy.node import Node
import imutils
from rclpy.qos import ReliabilityPolicy, QoSProfile
import pytesseract
import time
import requests
import json
import cv2
import numpy as np
import imutils
import pytesseract
import time
import requests
import json
class Ros2OpenCVImageConverter(Node):   

    def __init__(self):

        super().__init__('Ros2OpenCVImageConverter')
        
        self.bridge_object = CvBridge()
        self.image_sub = self.create_subscription(Image,'/image',self.camera_callback,QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT))
        
    def camera_callback(self,data):

        try:
            # Seleccionamos bgr8 porque es la codificacion de OpenCV por defecto

            pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
            # Cargar la imagen de la matrícula
            cv_img = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")

            print(len(cv_img))
            cv_img = cv2.resize(cv_img, (600, 400))

            gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
            gray = cv2.bilateralFilter(gray, 13, 15, 15)

            edged = cv2.Canny(gray, 30, 200)
            contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
            screenCnt = None

            for c in contours:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.018 * peri, True)

                if len(approx) == 4:
                    screenCnt = approx
                    break

            if screenCnt is None:
                detected = 0
                print("No contour detected")
            else:
                detected = 1
                cv2.drawContours(cv_img, [screenCnt], -1, (0, 0, 255), 3)

                mask = np.zeros(gray.shape, np.uint8)

        
                new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1)
                new_image = cv2.bitwise_and(cv_img, cv_img, mask=mask)
                (x, y) = np.where(mask == 255)
                (topx, topy) = (np.min(x), np.min(y))
                (bottomx, bottomy) = (np.max(x), np.max(y))
                Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]
                text = pytesseract.image_to_string(Cropped, config='--psm 11')
                print("programming_fever's License Plate Recognition\n")
                print("Detected license plate Number is:", text)
                img = cv2.resize(cv_img, (500, 300))
                Cropped = cv2.resize(Cropped, (400, 200))
                cv2.imshow('car', img)
                #cv2.imshow('Cropped', Cropped)
                cv2.imshow("Imagen capturada por el robot", cv_img)
                time.sleep(3)            #if detected == 1:
                # URL de destino
                url = 'http://localhost:3000/insertar_matricula'  # Reemplaza con la URL correcta de la API
                # Datos del post a enviar
                datos = {
                'matricula': text,
    
                }
                respuesta = requests.post(url, json=datos)
                                
                # Verificar la respuesta
                if respuesta.status_code == 200:
                    print("¡El post se ha creado exitosamente!")
                else:
                    print("Error al crear el post. Código de estado:", respuesta.status_code)



            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            
        except CvBridgeError as e:
            print(e)

                
        cv2.waitKey(1)    

def main(args=None):

    rclpy.init(args=args)    
    img_converter_object = Ros2OpenCVImageConverter()    
       
    try:
        rclpy.spin(img_converter_object)
    except KeyboardInterrupt:
        img_converter_object.destroy_node()
        print("Fin del programa!")
    
    cv2.destroyAllWindows() 
    

if __name__ == '__main__':
    main()

