import cv2
# Membaca gambar
image = cv2.imread('env/WhatsApp Image 2025-01-25 at 09.13.36.jpeg')
# Menampilkan gambar
cv2.imshow('Display Window', image)
# Menunggu hingga ada input dari keyboard
cv2.waitKey(0)
# Menutup semua jendela
cv2.destroyAllWindows()