from PIL import Image
import os

input_folder = "imagesToConvert"
output_folder = "imagesConverted"

jpg_quality = 100  # 100 = massima qualità, 75 = predefinito

os.makedirs(output_folder, exist_ok=True)

supported_extensions = (".webp", ".png")

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(supported_extensions):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name.rsplit('.', 1)[0] + ".jpg")

        try:
            with Image.open(input_path) as img:
                img = img.convert("RGB")
                img.save(output_path, "JPEG", quality=jpg_quality)
                print(f"Convertito: {file_name} -> {output_path} con qualità {jpg_quality}")
        except Exception as e:
            print(f"Errore durante la conversione di {file_name}: {e}")

print("Conversione completata!")
