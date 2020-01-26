from PIL import Image
import math


def escagris(img):
    arr = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            arr[x,y] = img.getpixel((x,y))
    return arr
huella=Image.open("imagesInput/dedoscan.png").convert("L")
convirtiendo = escagris(huella)
huella.save("imagesOuput/escalagrisu.tif")
huella.show()


def binarizacion (img,umbral):
    arr = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            p = img.getpixel((x,y))
            if p>umbral:
                arr[x,y] = 255
            else:
                arr[x,y] = 0
    return arr   

huella=Image.open("imagesOuput/escalagrisu.tif").convert("L")
convirtiendo=binarizacion(huella,128)
huella.save("imagesOuput/binarizacion.tif")
huella.show()

def adelgazamiento(img,mascaraH,mascaraV):
    arr = img.load()        
    
    Ha = mascaraH[0][0]
    Hb = mascaraH[0][1]
    Hc = mascaraH[0][2]
    Hd = mascaraH[1][0]
    He = mascaraH[1][1]
    Hf = mascaraH[1][2]
    Hg = mascaraH[2][0]
    Hh = mascaraH[2][1]
    Hi = mascaraH[2][2]

    Va = mascaraV[0][0]
    Vb = mascaraV[0][1]
    Vc = mascaraV[0][2]
    Vd = mascaraV[1][0]
    Ve = mascaraV[1][1]
    Vf = mascaraV[1][2]
    Vg = mascaraV[2][0]
    Vh = mascaraV[2][1]
    Vi = mascaraV[2][2]
    
    for x in range(1,img.size[0]-1):
        for y in range(1,img.size[1]-1):
            Ia = img.getpixel((x-1,y-1))
            Ib = img.getpixel((x-1,y))
            Ic = img.getpixel((x-1,y+1))
            Id = img.getpixel((x,y-1))
            Ie = img.getpixel((x,y))
            If = img.getpixel((x,y+1))
            Ig = img.getpixel((x+1,y-1))
            Ih = img.getpixel((x+1,y))
            Ii = img.getpixel((x+1,y+1))
            Gx = Ha*Ia+Hb*Ib+Hc*Ic+Hd*Id+He*Ie+Hf*If+Hg*Ig+Hh*Ih+Hi*Ii
            Gy = Va*Ia+Vb*Ib+Vc*Ic+Vd*Id+Ve*Ie+Vf*If+Vg*Ig+Vh*Ih+Vi*Ii
##            Gx = math.fabs(-Ia-Id-Ig+Ic+If+Ii)
##            Gy = math.fabs(-Ia-Ib-Ic+Ig+Ih+Ii)
            valor = math.sqrt(Gx*Gx+Gy*Gy)
            if valor>255.0:
                valor=255.0
            arr[x-1,y-1] = int(valor)
    return arr

img = Image.open("imagesOuput/binarizacion.tif").convert("L")
thiningX = [[0.0 ,0.0, 0.0],
            [0.0 ,1.0, 0.0],
            [1.0 ,1.0, 1.0],
            
            [1.0 ,0.0, 0.0],
            [1.0 ,1.0, 0.0],
            [1.0 ,0.0, 0.0],
            
            [1.0 ,1.0, 1.0],
            [0.0 ,1.0, 0.0],
            [0.0 ,0.0, 0.0],
                       
            [0.0 ,0.0, 1.0],
            [0.0 ,1.0, 1.0],
            [0.0 ,0.0, 1.0]]
          

thiningY = [[0.0,  0.0,  0.0],
            [1.0,  1.0,  0.0],
            [0.0,  1.0,  0.0],
            
            [0.0 ,1.0, 0.0],
            [1.0 ,1.0, 0.0],
            [0.0 ,0.0, 0.0],
            
            [0.0 ,1.0, 0.0],
            [0.0 ,1.0, 1.0],
            [0.0 ,0.0, 0.0],
                       
            [0.0 ,0.0, 0.0],
            [0.0 ,1.0, 1.0],
            [0.0 ,1.0, 0.0]]


I =  adelgazamiento(img,thiningX,thiningY)
img.save("imagesOuput/imgAdelgazada.tif")
img.show()


def poda(img,mascaraH,mascaraV):
    arr = img.load()        
    
    Ha = mascaraH[0][0]
    Hb = mascaraH[0][1]
    Hc = mascaraH[0][2]
    Hd = mascaraH[1][0]
    He = mascaraH[1][1]
    Hf = mascaraH[1][2]
    Hg = mascaraH[2][0]
    Hh = mascaraH[2][1]
    Hi = mascaraH[2][2]

    Va = mascaraV[0][0]
    Vb = mascaraV[0][1]
    Vc = mascaraV[0][2]
    Vd = mascaraV[1][0]
    Ve = mascaraV[1][1]
    Vf = mascaraV[1][2]
    Vg = mascaraV[2][0]
    Vh = mascaraV[2][1]
    Vi = mascaraV[2][2]
    
    for x in range(1,img.size[0]-1):
        for y in range(1,img.size[1]-1):
            Ia = img.getpixel((x-1,y-1))
            Ib = img.getpixel((x-1,y))
            Ic = img.getpixel((x-1,y+1))
            Id = img.getpixel((x,y-1))
            Ie = img.getpixel((x,y))
            If = img.getpixel((x,y+1))
            Ig = img.getpixel((x+1,y-1))
            Ih = img.getpixel((x+1,y))
            Ii = img.getpixel((x+1,y+1))
            Gx = Ha*Ia+Hb*Ib+Hc*Ic+Hd*Id+He*Ie+Hf*If+Hg*Ig+Hh*Ih+Hi*Ii
            Gy = Va*Ia+Vb*Ib+Vc*Ic+Vd*Id+Ve*Ie+Vf*If+Vg*Ig+Vh*Ih+Vi*Ii
##            Gx = math.fabs(-Ia-Id-Ig+Ic+If+Ii)
##            Gy = math.fabs(-Ia-Ib-Ic+Ig+Ih+Ii)
            valor = math.sqrt(Gx*Gx+Gy*Gy)
            if valor>255.0:
                valor=255.0
            arr[x-1,y-1] = int(valor)
    return arr

img = Image.open("imagesOuput/imgAdelgazada.tif").convert("L")
pruningX = [[0.0 ,0.0, 0.0],
            [0.0 ,1.0, 0.0],
            [0.0 ,0.0, 0.0]]
          

pruningY = [[0.0,  0.0,  0.0],
            [0.0,  1.0,  0.0],
            [0.0,  0.0,  0.0]]


I =  poda(img,thiningX,thiningY)
img.save("imagesOuput/imgpoda.tif")
img.show()















