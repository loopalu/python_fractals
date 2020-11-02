"""Written by Aivar Loopalu. Function draws fractals."""


from PIL import Image, ImageDraw
import math


class Fractal:
    """Class for drawing a fractal."""

    def __init__(self, size, scale, computation):
        """Constructor.

        Arguments:
        size -- the size of the image as a tuple (x, y)
        scale -- the scale of x and y as a list of 2-tuple [(minimum_x, minimum_y), (maximum_x, maximum_y)]
        computation -- the function used for computing pixel values as a function
        """
        self.size = size
        self.scale = scale
        self.computation = computation
        self.coordinates = []
        self.map_width = size[0]
        self.map_height = size[1]
        self.img = Image.new('RGB', (self.map_width, self.map_height), color='white')
        self.draw = ImageDraw.Draw(self.img)
        self.width_change = (self.scale[1][0] - self.scale[0][0]) / self.map_width
        self.height_change = (self.scale[0][1] - self.scale[1][1]) / self.map_height
        self.pixel_width = 1
        self.pixel_height = 1

    def compute(self):
        """
        Create the fractal by computing every pixel value.

        map_width - The width of picture.
        map_height - The height of picture.
        pixel_width - The width of pixel.
        pixel_height - The height of pixel.
        width_change - Variable that shows the change of pixel's value to right.
        height_change - Variable that shows the change of pixel's value to bottom.
        """
        count = 0
        for y in range(self.map_height + 1):
            for x in range(self.map_width + 1):
                pixel = (x, y)
                escape = self.pixel_value(pixel)
                self.draw.rectangle([x, y, (x + 1), (y + 1)], fill=(self.color(escape)))
                count += 1
                print(str(count / (self.map_width * self.map_height) * 100) + " %")
        return True

    def pixel_value(self, pixel):
        """
        Return the number of iterations it took for the pixel to go out of bounds.

        Arguments:
        pixel -- the pixel coordinate (x, y)
        Returns:
        the number of iterations of computation it took to go out of bounds as integer.
        """
        x = self.scale[0][0] + pixel[0] * self.width_change
        y = self.scale[1][1] + pixel[1] * self.height_change
        pixel = (x, y)
        iter = self.computation(pixel)
        return iter

    def save_image(self, filename):
        """
        Save the image to hard drive.

        Arguments:
        filename -- the file name to save the file to as a string.
        """
        self.img.save(filename)

    def color(self, escape):
        """Color set."""
        red = escape % 32 * 8
        green = escape % 16 * 16
        blue = escape % 8 * 32
        if escape == 200:
            return 255, 255, 255
        return red, green, blue

if __name__ == "__main__":
    def mandelbrot_computation(pixel):
        """Function for Mandelbrot fractals."""
        x = pixel[0]
        y = pixel[1]
        count = 0
        if x**2 + y**2 > 4:
            count += 1
        else:
            count += 1
            while x**2 + y**2 <= 4:
                x_start = pixel[0]
                y_start = pixel[1]
                x1 = x
                y1 = y
                x = x1**2 - y1**2 + x_start
                y = 2 * x1 * y1 + y_start
                count += 1
                if count > 1000:
                    print(255)
                    return 255
        print(count)
        return count

    def julia_computation(pixel):
        """Function for Julia fractals."""
        x = pixel[0]
        y = pixel[1]
        count = 0
        if x**2 + y**2 > 4:
            count += 1
        else:
            count += 1
            while x**2 + y**2 <= 4:
                x_start = 0.28
                y_start = 0.008
                x1 = x
                y1 = y
                x = math.sin(x1**2 - y1**2 + x_start)
                y = 2 * x1 * y1 + y_start
                count += 1
                if count > 1000:
                    return 200
        return count
    
    def anime():
        """Function for making gif."""
        delta = 0.09075
        for i in range(0, 1400, 1):
            #julia = Fractal((300, 300), [(-2 * 0.95**i - delta, -2 * 0.95**i - delta), (2 * 0.95**i - delta, 2 * 0.95**i - delta)], julia_computation)
            julia = Fractal((1000, 1000), [(-2 * 0.99 ** i - delta, -2 * 0.99 ** i - delta),
                                         (2 * 0.99 ** i - delta, 2 * 0.99 ** i - delta)], julia_computation)
            julia.compute()
            name = "julia" + str(i) + ".png"
            julia.save_image(name)

    anime()
    """
    mandelbrot = Fractal((1000, 1000), [(-2, -2), (2, 2)], mandelbrot_computation)
    mandelbrot.compute()
    mandelbrot.save_image("mandelbrot.png")
    mandelbrot2 = Fractal((1000, 1000), [(-0.74877, 0.065053), (-0.74872, 0.065103)], mandelbrot_computation)
    mandelbrot2.compute()
    mandelbrot2.save_image("mandelbrot2.png")
    julia = Fractal((1000, 1000), [(-2, -2), (2, 2)], julia_computation)
    julia.compute()
    julia.save_image("julia.png")
    """
