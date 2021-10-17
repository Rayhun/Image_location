from exif import Image

img_path = '/home/rayhan/Downloads/IMG20211018022202.jpg'
with open(img_path, 'rb') as src:
    img = Image(src)

    if img.has_exif:
        info = f"has the EXIF {img.exif_version}"
    else:
        info = "does not contain any EXIF information"
    print(img.gps_longitude, img.list_all())
