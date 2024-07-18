from PIL import Image, ImageDraw
from os.path import join
from glob import glob

from pixelate import pixelate_image

pixel_size = 25
spacing = 10
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
