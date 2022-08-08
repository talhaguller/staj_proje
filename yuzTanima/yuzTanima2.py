from operator import iadd
from turtle import color
import cv2
import os
import mediapipe as mp

import sys



"""
	Burda da yüzü belirleyip yüzü kesmeyi yarıyor
	ve kesilen yüzü kaydediyor
	Kullanıcıdan terminalden aldığı isim üzerine dosya açıp oaraya keydediyor
"""




mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

print("Lütfen bir isim Gİriniz:")
isim=input()
camera = cv2.VideoCapture(0)

try:
	
	# data+hangi kişi ise o klasörde isim açıyor ---> fotoları oraya kaydediyor
	if not os.path.exists('data/'+isim):
		os.makedirs('data/'+isim)


except OSError:
	print ('data oluşturulamadı')

# foto numara sayısı
sayi = 0

while(True):
	
	# kamerayı açıyor burda
	
	with mp_face_detection.FaceDetection(
		model_selection=0, min_detection_confidence=0.5) as face_detection:
		while camera.isOpened():
			success, image =camera.read()
			image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
					
					#fotoğrafın konumunu çıkartıyoruz
					#detection içinde box olarak geliyor
					mp_drawing.draw_detection(image,detection)
					xmin=detection.location_data.relative_bounding_box.xmin
					ymin=detection.location_data.relative_bounding_box.ymin
					width=detection.location_data.relative_bounding_box.width
					height=detection.location_data.relative_bounding_box.height
					print(xmin)
					print(ymin)
					print(width)
					print(height)

					#burda box türünde olan sayıları int e dönüştürüyoruz
					dh,dw,_=image.shape
					print(dh)
					print(dw)
					print("************************")

					

					nx = int(xmin*dw)
					ny = int(ymin*dh)
					nw = int(width*dw)
					nh = int(height*dh)

					print(nx)
					print(ny)
					print(nw)
					print(nh)
					print("---------------------")

					#dönüştürülen sayıları elde ettiğimiz fotoğraftan belirtilen konumları kesiyoruz
					kesik=image[ny:ny+nh,nx:nx+nw]
					
					#burda fotoprafın sahibi olan adamın adıla kaydediyor
					name = './data/'+isim+'/'+isim + str(sayi) + '.jpg'
					print ('Oluşturuluyor...' + name)
					
					#keilen fotoğrafı kaydediyor 
					cv2.imwrite(name, kesik)
					sayi += 1
					
					
					
			if cv2.waitKey(2500) & 0xFF == 27:
				break	


	camera.release()
	cv2.destroyAllWindows()





