from PIL import Image, ImageDraw, ImageFont

# Kreiraj 256x256 ikonu
size = 256
img = Image.new('RGB', (size, size), color='white')
draw = ImageDraw.Draw(img)

# Pozadina - gradijent plavi
for i in range(size):
    color = (30, 60 + i//2, 120 + i//3)
    draw.rectangle([0, i, size, i+1], fill=color)

# Nacrtaj štampač outline
printer_color = (255, 255, 255)
# Glavni pravougaonik štampača
draw.rectangle([60, 80, 196, 180], fill=printer_color, outline=(200, 200, 200), width=3)
# Gornji deo (paper tray)
draw.rectangle([70, 50, 186, 80], fill=(220, 220, 255), outline=(150, 150, 200), width=2)
# Papir koji izlazi
draw.rectangle([90, 40, 166, 50], fill=(255, 255, 255), outline=(100, 100, 100), width=2)

# Toner kartridž (centralno)
toner_x = 128 - 30
toner_y = 100
draw.rectangle([toner_x, toner_y, toner_x+60, toner_y+40], 
               fill=(34, 139, 34), outline=(20, 80, 20), width=3)

# Tekst "T" za Toner
try:
    # Pokušaj sa system fontom
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
except:
    font = ImageFont.load_default()

draw.text((toner_x+18, toner_y+5), "T", fill='white', font=font)

# Donji deo - progress bar (prikaz nivoa)
draw.rectangle([60, 185, 196, 195], fill=(220, 220, 220), outline=(100, 100, 100), width=2)
draw.rectangle([62, 187, 150, 193], fill=(34, 139, 34))

# Sačuvaj u različitim veličinama
img.save('/tmp/toner_final/icon_256.png')
img_128 = img.resize((128, 128), Image.Resampling.LANCZOS)
img_128.save('/tmp/toner_final/icon_128.png')
img_64 = img.resize((64, 64), Image.Resampling.LANCZOS)
img_64.save('/tmp/toner_final/icon_64.png')
img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
img_32.save('/tmp/toner_final/icon_32.png')

print("✅ Ikone kreirane: icon_256.png, icon_128.png, icon_64.png, icon_32.png")

