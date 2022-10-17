import qrcode


qr_icerik = input("qr'ın içeriğini giriniz : ")
text = input("isim :")


qr = qrcode.QRCode(

    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 20 ,
    border = 5
)
qr.add_data(qr_icerik)
qr.make(fit=True)
img = qr.make_image()
img.save("xd.png")

