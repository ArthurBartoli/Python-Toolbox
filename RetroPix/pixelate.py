from PIL import Image, ImageDraw
from os.path import join
from glob import glob

def pixelate_image(input_path, output_path, pixel_size, spacing, standard_size=1000):
    image = Image.open(input_path)
    original_size = image.size
    original_ratio = original_size[0] / original_size[1]
    new_size = [round(standard_size*original_ratio), standard_size]
    
    # Pixelate
    small_image = image.resize(
        (original_size[0] // pixel_size, original_size[1] // pixel_size),
        resample=Image.NEAREST
    )
    pixelated_image = small_image.resize(new_size, resample=Image.NEAREST)
    
    # RGBA for transparency
    output_image = Image.new('RGBA', new_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(output_image)
    
    # Redraw the picture with negative space between pixels
    for y in range(0, new_size[1], pixel_size):
        for x in range(0, new_size[0], pixel_size):
            pixel_color = pixelated_image.getpixel((x, y))
            draw.rectangle(
                [x, y, x + pixel_size - spacing, y + pixel_size - spacing],
                fill=pixel_color
            )
    
    # Save as .png for transparency
    output_image.save(output_path, format="PNG")

if __name__ == "__main__":    
    pixel_size = 7
    spacing = 4
    # pixel_size to 10 and spacing to 6 gives a good render
    # With standardised size, 7 pixel size and 4 spacing is a good render
    # With strandardised size, (3, 3) is pretty good too
    # With strandardised size, (4, 4) is good


    input_path = join("Retropix", "Input")
    output_folder = join("Retropix", "Output")
    input_folder = glob(input_path + "\\*.png")

    for input_filepath in input_folder:
        input_filename = input_filepath.split('\\')[-1]
        print("Processing : " + input_filename)
        output_name = input_filename[:-4] + '_retropix.png'
        output_path = join("Retropix\\Output", output_name)
        pixelate_image(input_filepath, output_path, pixel_size, spacing)
