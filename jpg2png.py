import os
import sys
from PIL import Image, PngImagePlugin

def jpg2png(directory, width, height):
    png_text = 'Imagen convertida y redimensionada con codigo obtenido de github.com/JuanMX/jpg2png'

    for img_name in os.listdir(directory):
        im = Image.open('./'+directory+'/'+img_name)
        exif = im.getexif()
        for k, v in exif.items():
            #print("Tag", k, "Value", v)
            del exif[k]

        im_resized = im.resize((width, height))

        png_metadata = PngImagePlugin.PngInfo()
        png_metadata.add_text('text', png_text)

        im_resized.save('./'+directory + output_directory_ends_with + '/' + img_name[:-4] + ".png", pnginfo=png_metadata)
        im.close()
        print("Converted:   " + img_name + "   Saved as:   " + img_name[:-4] + ".png")


def main():
    arg_directory = '-directory'
    arg_resize = '-resize'
    work_directory = ""
    resize_width = 0
    resize_height = 0

    args = sys.argv[1:]


    # [supported] example: jpg2png.py -directory directory_name -resize 1024 768 -> convert photos in directory name and resize the output
    # [unsupported] example: jpg2png.py -directory folder_name -> convert photos in directory name without resizing
    # [unsupported] example: jpg2png.py -directory folder_name -resize 1024 768 -> convert and resize photos in the current directory
    # [unsupported] example: jpg2png.py -> convert without resizing photos in the current directory
    
    if len(args) == 5 and args[0] == arg_directory and args[2] == arg_resize:
        work_directory = args[1]
        resize_width   = int(args[3])
        resize_height  = int(args[4])
    else:
        print("Source file needs to be executed like this: ")
        print("   > python jpg2png.py -directory directory_name -resize 1024 768")
        print("The directory_name and this source code need to be in the same place")
        exit(1)
    if (os.path.isdir(work_directory) == False):
        print("Directory does not exists")
        exit(1)

    return work_directory, resize_width, resize_height
    
if __name__ == "__main__":

    output_directory_ends_with = '_PNG-output'

    directory, width, height = main()
    
    try:
        os.mkdir('./'+directory + output_directory_ends_with)
    except FileExistsError as e:
        print(e, ' trying to continue')
    
    jpg2png(directory, width, height)

    done_message = "DONE, please check " + './'+directory + output_directory_ends_with
    
    print('\n\n')
    print("="*len(done_message))
    print(done_message)
    print("="*len(done_message))