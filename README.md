
## COMO EJECUTAR EL PROYECTO:


python 3.10.0
entorno virtual venv - 

ejecutar => py 3.10 -m venv tf-env

y activar el entorno con tf-env/Scripts/activate
# Instalaciones

````
pip install tensorflow
````
````
pip install opencv-python
````
````
pip install cvlib
````


# PASOS QUE SE REALIZÓ PARA SOLUCIONAR EL PROGRAMA:

1: SE TRASLADÓ EL LA VERSION DE de archivos YOLO DE V3 A LA V4 , necesario en la carpeta yolo/

problema de archivos:


    Directorio: C:\Users\ETIA\.cvlib\object_detection\yolo

````

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        27/06/2025     20:20                yolov3
-a----        27/06/2025     21:04           8342 yolov3.cfg
-a----        27/06/2025     20:13            620 yolov3_classes.txt

````

````
nota: al ejecutar los el script inicial se generaba archivos v3 entonces se tuvo que hacer una "limpieza" y trasladar los siguientes archivos en su reemplazo:
````

yolov4.weights: Archivo de pesos del modelo

yolov4.cfg: Archivo de configuración de la arquitectura de la red neuronal

yolov3_classes.txt: Archivo de clases que contiene las etiquetas que el modelo puede detectar --- este archivo no necesita ser v4


enlaces:

yolov4.cfg

https://github.com/AlexeyAB/darknet/blob/master/cfg/yolov4.cfg


yolov4.weights

https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4.weights







````
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        27/06/2025     20:13            620 yolov3_classes.txt
-a----        27/06/2025     21:33         780725 yolov4.cfg
-a----        27/06/2025     21:34      257717640 yolov4.weights

````