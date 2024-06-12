from PIL import Image, ImageDraw
from os.path import join

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

input_name = "SolarSquare.png"
input_path = join("Retropix\\Input", input_name)
output_name = input_name[:-4] + '_pixelisee.png'
output_path = join("Retropix\\Output", output_name)
pixel_size = 10  
spacing = 6    
# pixel_size to 10 and spacing to 6 gives a good render

pixelate_image(input_path, output_path, pixel_size, spacing)
