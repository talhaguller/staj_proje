import os
import time
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import *
import cv2
import mediapipe as mp
import sys

from yüzTanimaDesigner import Ui_Form
from PyQt5.QtGui import QPixmap

"""  
    Burda Pqyt5'i Ekleyerek Fonksiyonlaştırılmaya Çalışıldı
    Her Fonksiyonun Üstünde Ne İşe Yaradığına Dair Bilgilendirilme Yapılmıştır
"""

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
class MyApp(QtWidgets.QWidget):
    
    
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.get_files()
        self.file_name_comboBox()
        
        #burda listtede tıklanan değeri döndürüyor 
        self.ui.file_listWidget.itemClicked.connect(self.Clicked)
        
        #burda dosya oluştur butonuna tıklayınca yazılan isme göre dosya oluşturuyor
        self.ui.pushButton.clicked.connect(self.file_create)
        #burda basınca true dönüyor true olunca camera açılıyor
        self.ui.yon_degistir_btn.clicked['bool'].connect(self.state)

        #doyaları bulup açmaya yarıyor
        self.ui.file_open_btn.clicked.connect(self.find)
        #butona basınca buton textini değiştiriyor
        self.ui.file_open_btn.clicked['bool'].connect(self.find)
       
        
        
        self.show()

  
    #burda dosyaları döndürüyor
    def get_files(self):
        mainFile="C:\\Users\\Talha\\Desktop\\isYeri"
        mainFiles=os.listdir(mainFile)
        for i in mainFiles:
            if i!="data":
                try:
	
                    # data+hangi kişi ise o klasörde isim açıyor ---> fotoları oraya kaydediyor
                    if not os.path.exists('data'):
                        os.makedirs('data')


                except OSError:
                    print ('data oluşturulamadı')
            
    
    #yeni dosya açılınca dosyaları silip yeni açılanı da göstermek için yapıldı
    def remove(self):
        self.ui.data_listWidget.clear()
        

    #burda kullanıcıdan klasör ismi alıp klasör açmasına yarıyor    
    def file_create(self,isim):
        self.isim=isim
        enteredName=self.ui.lineEdit.text().upper()
        isim=enteredName
        try:
	
            # data+hangi kişi ise o klasörde isim açıyor ---> fotoları oraya kaydediyor
            if not os.path.exists('data/'+isim):
                os.makedirs('data/'+isim)
                returnValue=self.baslamaMessageBox()


        except OSError:
            print ('klasör oluşturulamadı')
            self.remove()
            self.get_files()

        print()
    
   
    
    def camera(self):
        returnValue1=self.bilgilendirmeMessageBox()
        sayi=0
        camera = cv2.VideoCapture(0)
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
                        strs=self.ui.lineEdit.text().upper()
                        taraf="on"
                        
                        
                        if sayi>=0 and sayi<5:
                            #burda fotoprafın sahibi olan adamın adıla kaydediyor
                            name = './data/'+strs +'/'+strs+'_'+taraf+'_'+ str(sayi) + '.jpg'
                            print ('Oluşturuluyor...' + name)
                                
                            #keilen fotoğrafı kaydediyor 
                            cv2.imwrite(name, kesik)
                            sayi += 1
                        else:
                            returnValue2=self.solYuzMessageBox()
                            if returnValue2 == QMessageBox.Ok:
                                print('OK clicked')
                                time.sleep(5)
                                if sayi>=5 and sayi<7:
                                    self.ui.yon_lbl.setText("Sol Yüzünüzü Dönün")
                                    taraf="sol"
                                    name = './data/'+strs +'/'+strs+'_'+taraf+'_'+ str(sayi) + '.jpg'
                                    print ('Oluşturuluyor...' + name)
                                        
                                    #kesilen fotoğrafı kaydediyor 
                                    cv2.imwrite(name, kesik)
                                    sayi += 1
                            returnValue3=self.sagYuzMessageBox()
                            if returnValue3 == QMessageBox.Ok: 
                                time.sleep(5)   
                                if sayi>=7 and sayi<12:
                                    self.ui.yon_lbl.setText("Sağ Yüzünüzü Dönün")
                                    taraf="sag"

                                    #burda fotoprafın sahibi olan adamın adıla kaydediyor
                                    name = './data/'+strs +'/'+strs+'_'+taraf+'_'+ str(sayi) + '.jpg'
                                    print ('Oluşturuluyor...' + name)
                                        
                                    #keilen fotoğrafı kaydediyor 
                                    cv2.imwrite(name, kesik)
                                    sayi += 1
                                elif sayi==12:
                                    camera.release()
                                    break      
                if cv2.waitKey(2500) & 0xFF == ord('q'):
                    break	

        print()
    
    #açılan dosyalardaki tekrar üstüne yazmasın diye silemeye yarıyor
    #combox da seçilen bir dosyanın içini açmaya yarıyor
    def find(self,bool):
        if bool: 
            self.ui.file_open_btn.setText("Dosya Kapat")
            # index
            index = self.ui.file_name_comboBox.currentIndex()
    
            # finding the content at index  in combo box
            fileName = self.ui.file_name_comboBox.itemText(index).strip()
            #print(type(fileName))
            fileUrl="C:\\Users\\Talha\\Desktop\\isYeri\\data\\"+fileName
            # showing content on the screen though label
            files=os.listdir(fileUrl)
            print(files)
            if len(files)==0:
                text="Dosya İçi Boştur"
                self.ui.file_listWidget.addItem(text)
            else:
                names=self.ui.file_listWidget.addItems(files)
                #print(files)
        else:
            self.ui.file_open_btn.setText("Dosya Aç")
            self.ui.file_listWidget.clear()
        
        
    #burda listWidgetta tıklanan dosyanın adını alıp dosya uzantısı oluşturuyoruz
    def Clicked(self,item):
        # index
        index = self.ui.file_name_comboBox.currentIndex()
    
        # finding the content at index  in combo box
        fileName = self.ui.file_name_comboBox.itemText(index).strip()
        #print(type(fileName))
        fileUrl="C:\\Users\\Talha\\Desktop\\isYeri\\data\\"+fileName
        print(fileUrl+"\\"+(item.text()))
        openFile=fileUrl+"\\"+(item.text())
        pixmap = QPixmap(openFile)

        self.ui.image_lbl.setPixmap(QtGui.QPixmap(pixmap))

    #Message Boxlarla kullanıcı ile iletişim kurularak yapıldı    
    def solYuzMessageBox(self):
        solmMsgBox = QMessageBox()
        solmMsgBox.setIcon(QMessageBox.Information)
        solmMsgBox.setText("Sol Yüzünüzü Dönün 5 sn Sonra Fotoğraf Çekime Başlayacak")
        solmMsgBox.setWindowTitle("İnformation")
        solmMsgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = solmMsgBox.exec()
        return returnValue  

    def sagYuzMessageBox(self):
        self.ui.msgBox = QMessageBox()
        self.ui.msgBox.setIcon(QMessageBox.Information)
        self.ui.msgBox.setText("Sağ Yüzünüzü Dönün 5 sn Sonra Fotoğraf Çekime Başlayacak")
        self.ui.msgBox.setWindowTitle("İnformation")
        self.ui.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        

        returnValue = self.ui.msgBox.exec()
        return returnValue         
    
    def baslamaMessageBox(self):
        baslaMsgBox = QMessageBox()
        baslaMsgBox.setIcon(QMessageBox.Information)
        baslaMsgBox.setText("Dosyanız Oluşturulmuştur. Fotoğraf Çekmek İçin Başlama Butonuna Tıklayınız")
        baslaMsgBox.setWindowTitle("İnformation")
        baslaMsgBox.setStandardButtons(QMessageBox.Ok)
        

        returnValue = baslaMsgBox.exec()
        return returnValue         
    
    def bilgilendirmeMessageBox(self):
        bilgiMsgBox = QMessageBox()
        bilgiMsgBox.setIcon(QMessageBox.Information)
        bilgiMsgBox.setText("Lütfen Kameranızın Önü Kapalıysa Açınız")
        bilgiMsgBox.setWindowTitle("İnformation")
        bilgiMsgBox.setStandardButtons(QMessageBox.Ok)
        

        returnValue = bilgiMsgBox.exec()
        return returnValue         

    def file_name_comboBox(self):
        file="C:\\Users\\Talha\\Desktop\\isYeri\\data"
        files=os.listdir(file)
        self.ui.file_name_comboBox.addItems(files)

        print()

    def state(self,bool):
        if bool==False:
            print(bool)
            
        else:
            print(bool)
            

        if bool==False:
            print(bool)
            self.camera()
        else:
            print("Çalışmadı")




        
def app():
    app=QtWidgets.QApplication(sys.argv)
    win=MyApp()
    win.show()
    sys.exit(app.exec_())


app()