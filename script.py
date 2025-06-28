import cv2
import numpy as np

#Problema: Las rutas a los archivos de pesos (.weights), configuración (.cfg) y clases (.txt)
#  no eran correctas o no estaban bien definidas.
weights_path = "C:/Users/ETIA/.cvlib/object_detection/yolo/yolov4.weights"
cfg_path = "C:/Users/ETIA/.cvlib/object_detection/yolo/yolov4.cfg"
labels_path = "C:/Users/ETIA/.cvlib/object_detection/yolo/yolov3_classes.txt"  # O tu archivo de clases correcto
#archivo de clases (labels_path) correspondiera con la 
# versión del modelo (en este caso, YOLOv4 y no YOLOv3) para evitar desajustes en las etiquetas.
# Cargar red
net = cv2.dnn.readNet(weights_path, cfg_path)

# Cargar nombres de clases
with open(labels_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Configurar cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]

    # Preparar blob y hacer forward pass
    blob = cv2.dnn.blobFromImage(frame, 1/255, (416,416), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Eliminar cajas superpuestas
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            conf = confidences[i]
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, f"{label}: {conf:.2f}", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.imshow("YOLOv4 Object Detection", frame)

    if cv2.waitKey(1) == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()