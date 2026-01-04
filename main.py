from PIL import Image
import os

def create_pro_optimized_pdf(input_images, output_filename):
    image_list = []
    
    for file in input_images:
        if os.path.exists(file):
            img = Image.open(file)
            # Convert to RGB to ensure PDF compatibility and reduce size
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            image_list.append(img)
        else:
            print(f"Warning: {file} not found.")

    if image_list:
        # Saving with 300 DPI and 85 Quality for the best size/quality balance
        image_list[0].save(
            output_filename, 
            save_all=True, 
            append_images=image_list[1:], 
            resolution=300.0, 
            quality=85, 
            subsampling=0,
            optimize=True
        )
        print(f"Success! PDF saved as: {output_filename}")

if __name__ == "__main__":
    # You can change these filenames to match your images
    files = ["1.png", "2.png"]
    create_pro_optimized_pdf(files, "final_optimized.pdf")