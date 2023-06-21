import cv2
from PIL import ImageFilter

from run import process


def main():
    # Read input image
    input_image = cv2.imread("input.png")

    # Process to mask
    mask = process(input_image).filter(ImageFilter.BLUR)

    prompt = "naked girl with huge breast, intricate"
    negative_prompt = "deformed, bad anatomy, disfigured, poorly drawn face, mutation, mutated, extra limb, ugly, poorly drawn hands, missing limb, floating limbs, disconnected limbs, malformed hands, out of focus, long neck, long body, monochrome, feet out of view, head out of view, lowres, ((bad anatomy)), bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, jpeg artifacts, signature, watermark, username, blurry, artist name, extra limb, poorly drawn eyes, (out of frame), black and white, obese, censored, bad legs, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, (extra legs), (poorly drawn eyes), without hands, bad knees, multiple shoulders, bad neck, ((no head))"

    input_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2BGR)


if __name__ == "__main__":
    main()