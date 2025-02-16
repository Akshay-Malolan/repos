import qrcode
def generate_qrcode(txt):
    qr=qrcode.QRCode( # type: ignore
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(txt)
    qr.make(fit=True)
    img=qr.make_image(fill_color='black',back_color='white')
    img.save('qrimg.png')

url=input('Enter the url: ')
generate_qrcode(url)