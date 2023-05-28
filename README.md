# Detecção de Rachaduras usando YOLO

Este projeto demonstra a implementação de um modelo YOLO (You Only Look Once) para localizar rachaduras em imagens de vídeo em tempo real usando a biblioteca OpenCV e o pacote ultralytics.

Pré-requisitos
Certifique-se de ter os seguintes requisitos instalados em seu ambiente:

- Python 3.x
- OpenCV (cv2)
- Ultralytics

# Configuração
1. Baixe o arquivo de pesos pré-treinados (.pt) do modelo YOLO específico para detecção de rachaduras.
2. Salve o arquivo de pesos na mesma pasta do código-fonte.

# Utilização
1. Importe os módulos necessários:
```
import cv2 as cv
from ultralytics import YOLO
```
2. Inicialize a câmera para capturar o vídeo:
```
cam = cv.VideoCapture(0)
```
3. Carregue o modelo YOLO treinado para detecção de rachaduras:
```
model = YOLO("./best.pt")
```
4. Execute um loop contínuo para capturar frames de vídeo, fazer a previsão do modelo e exibir os resultados:
```
while True:
    ret, frame = cam.read()
    result = model.predict(frame, conf=0.6) 
    cv.imshow("Resultados", result[0].plot())
    if cv.waitKey(1) == ord('q'):
        break 
```
5. Libere os recursos da câmera e feche as janelas:
```
cam.release()
cv.destroyAllWindows()
```

# Parâmetros

- "cam": o objeto VideoCapture que representa a câmera a ser utilizada.
- "model": o objeto YOLO carregado com os pesos pré-treinados para detecção de rachaduras.
- "conf": o limite de confiança para considerar uma detecção válida. Pode ser ajustado conforme necessário.

# Considerações Finais

Este projeto serve como uma base para a detecção de rachaduras em tempo real usando YOLO. Você pode ajustar os parâmetros, treinar seu próprio modelo ou modificar o código para atender às suas necessidades específicas.
