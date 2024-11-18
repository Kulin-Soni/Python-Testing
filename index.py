# A program to rotate an image based on the pixels.
# Not actually an image rotater but it gives the idea of how images are rotated behind the scenes.

pixels = list(range(1, 11)) # 11 is (No. of pixels in the image + 1)
px = [5] # 5 is width, height will automatically be set
def sortPixels(array: list, dimensions: list): # This function creates an image dimension
    return [array[i:i+dimensions[0]] for i in range(0, len(array), dimensions[0])]

def rotatePixelsRight(array: list, dimensions: list): # This function rotates the image rightwards
    return [[i[x] for i in array][::-1] for x in range(dimensions[0])]

def rotatePixelsLeft(array: list, dimensions: list): # This function rotates the image leftwards
    return [[i[x] for i in array] for x in range(dimensions[0])][::-1]

# Original:
print(sortPixels(pixels, px))

# Right Rotated:
print(rotatePixelsRight(sortPixels(pixels, px), px))

# Left Rotated:
print(rotatePixelsLeft(sortPixels(pixels, px), px))