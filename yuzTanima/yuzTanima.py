from concurrent.futures import process
from operator import iadd
import cv2
import os
import mediapipe as mp



"""
	Adım Adım Neler Eklediklerimi farklı dosyalarda yazdım
	Burda sadece yüzü belirleyip dosyaya kaydediyor
"""



mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

camera = cv2.VideoCapture(0)

try:
	
	# data klasörünü oluşturuyor yoksa ---> fotoları oraya kaydediyor
	if not os.path.exists('data'):
		os.makedirs('data')


except OSError:
	print ('data oluşturulamadı')

# foto numara sayısı
sayi = 0

while(True):
	
	# kamerayı açıyor burda
	
	with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
		while camera.isOpened():
			success, image =camera.read()
			if not success:
				continue

			#fotoğrafın renkli ve çizgilerin olmasına yarıyor
			image.flags.writeable=False
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			results= face_detection.process(image)
			print(results)
			image.flags.writeable=True
			image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
			if results.detections:
				for detection in results.detections:
					mp_drawing.draw_detection(image,detection)
					
        			
					name = './data/image' + str(sayi) + '.jpg'
					print ('Oluşturuluyor...' + name)
					# foto kaydedilior
					
					cv2.imwrite(name, image)
					sayi += 1
			if cv2.waitKey(2500) & 0xFF == 27:
				break	
	
	camera.release()
	cv2.destroyAllWindows()
