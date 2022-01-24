import cv2
import os
from config import IMAGE_MEDICAL_DIR

def getResult(upload):
    upload_path = os.path.join(IMAGE_MEDICAL_DIR, upload)

    image = cv2.imread(upload_path, cv2.IMREAD_GRAYSCALE)

    result = 'result_' + upload
    result_path = os.path.join(IMAGE_MEDICAL_DIR, result)

    cv2.imwrite(result_path, image)
    
    return result