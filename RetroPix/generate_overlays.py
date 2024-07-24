from PIL import Image, ImageDraw
from os.path import join
from glob import glob

from pixelate import pixelate_image
from reverse_pixelate import reverse_pixelate_image

input_path = join("Retropix", "feed_for_stream")
output_folder = "C:\\Users\\arthu\\Pictures\\stream\\overlays"
input_folder = glob(input_path + "\\*")

for input_filepath in input_folder:
    input_filename = input_filepath.split('\\')[-1]
    print("Processing : " + input_filename)

    # 7, 4 good for graphical effect against full color background
    # 8, 3 good for laying over games
    # 8, 2 good for pausing overlay
    output_name_pixelate = input_filename[:-4] + '_pixelate_4stream.png'
    output_path_pixelate = join(output_folder, output_name_pixelate)
    pixelate_image(input_filepath, output_path_pixelate, 
                   pixel_size=7, spacing=4)

    output_name_reverse_pixelate = input_filename[:-4] + '_reverse_pixelate_4stream.png'
    output_path_reverse_pixelate = join(output_folder, output_name_reverse_pixelate)
    reverse_pixelate_image(input_filepath, output_path_reverse_pixelate, 
                            pixel_size=5, space_size=4)
