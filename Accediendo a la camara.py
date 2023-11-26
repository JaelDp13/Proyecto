import cv2

class Camara:
    def __init__(self, camara_index=0):
        self.camara = cv2.VideoCapture(camara_index)

    def _del_(self):
        self.camara.release()

    def show_camara(self):
        while True:
            ret, frame = self.camara.read()
            cv2.imshow('Camara', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()

if __name__ == "__main__":
    my_camara = Camara()
    my_camara.show_camara()
