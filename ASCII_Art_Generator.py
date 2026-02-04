from PIL import Image
def load_image(image_path,new_width=100):
    img=Image.open(image_path)
    aspect_ratio=img.height/img.width
    new_height=int(new_width*aspect_ratio*0.55)
    img=img.resize((new_width,new_height))
    return img
def convert_to_greyscale(img):
    return img.convert("L")
def map_pixels_to_ascii(img):
    ascii_chars="@%#*+=-:. "
    pixels=img.getdata()
    ascii_str="".join([ascii_chars[pixel//25] for pixel in pixels])
    return ascii_str
def generate_ascii_art(image_path,new_width=100):
    img=load_image(image_path,new_width)
    grey_image=convert_to_greyscale(img)
    ascii_str=map_pixels_to_ascii(grey_image)
    ascii_art="\n".join([ascii_str[i:i+new_width] for i in range(0,len(ascii_str),new_width)])
    return ascii_art
def save_ascii_art(ascii_art,output_path):
    with open(output_path,"w") as file:
        file.write(ascii_art)
def main():
    print("welcome to the ascii art generator")
    image_path=input("enter the loaction of the image")
    output_path=input("enter path to be stored")
    new_width=int(input("enter the width of ascii art"))
    try:
        ascii_art=generate_ascii_art(image_path,new_width)
        save_ascii_art(ascii_art,output_path)
        print(f"ascii art generated and saved to {output_path}")
    except Exception as e:
        print(f"an error occured :{e}")
if __name__=="__main__":
    main()