from PIL import Image

# 開啟本地圖片檔（1.jpg 必須放在同一資料夾中）
original = Image.open("1.png").convert("RGBA")

# 2. 裁切左側邊框（大約 80 像素）
width, height = original.size
cropped = original.crop((80, 0, width, height))

# 3. 羽化左邊緣邊界（漸層透明）
feather = Image.new("L", (20, height), color=0)
for x in range(20):
    alpha_value = int(255 * (x / 20))
    for y in range(height):
        feather.putpixel((x, y), alpha_value)

# 合併羽化邊界到透明通道
alpha = cropped.split()[-1]
alpha.paste(feather, (0, 0))
cropped.putalpha(alpha)

# 4. 儲存為透明 PNG
cropped.save("hero_right_image_cleaned.png", format="PNG")
print("✅ 已完成處理，儲存為 hero_right_image_cleaned.png")
