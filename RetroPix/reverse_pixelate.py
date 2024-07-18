from PIL import Image, ImageDraw
from os.path import join
from glob import glob

def reverse_pixelate_image_black(input_path, output_folder, filename, pixel_size=5, space_size=2):
    
    # Load the background image
    background_image_path = join(input_path, filename)
    background = Image.open(background_image_path).convert('RGBA')
    background = background.resize((1920, 1080))

    # Dimensions of the final image
    width, height = background.size

    # Create a new image with a transparent background
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Draw the pixels with transparency
    for y in range(0, height, pixel_size + space_size):
        for x in range(0, width, pixel_size + space_size):
            # Draw the transparent pixels
            if x + pixel_size <= width and y + pixel_size <= height:
                draw.rectangle([x, y, x + pixel_size, y + pixel_size], fill=(0, 0, 0, 255))
                # Fill the spaces around the pixels with a color (black in this case)
                if x + pixel_size + space_size <= width:
                    draw.rectangle([x + pixel_size, y, x + pixel_size + space_size, y + pixel_size], fill=(0, 0, 0, 0))
                if y + pixel_size + space_size <= height:
                    draw.rectangle([x, y + pixel_size, x + pixel_size, y + pixel_size + space_size], fill=(0, 0, 0, 0))
                if x + pixel_size + space_size <= width and y + pixel_size + space_size <= height:
                    draw.rectangle([x + pixel_size, y + pixel_size, x + pixel_size + space_size, y + pixel_size + space_size], fill=(0, 0, 0, 0))

    # Combine the background with the overlay
    combined = Image.alpha_composite(background, overlay)
    combined_data = combined.getdata()

    # Replace black pixels by transparent ones
    final = []
    for pixel in combined_data:
        if pixel[:3] == (0, 0, 0):
            final.append((0, 0, 0, 0))
        else : final.append(pixel)
    combined.putdata(final)

    # Save the final image
    output_path = join(output_folder, "overlay_pixel.png")
    combined.save(output_path, format="PNG")

    print(f"Overlay image saved to {output_path}")



if __name__ == "__main__":    
    input_path = join("Retropix", "Input")
    output_folder = join("Retropix", "Output")

    # 5, 2 is best for this format

    reverse_pixelate_image_black(input_path, output_folder, filename="ruins_resclaed.png", 
                                 pixel_size=5, space_size=2)
    
