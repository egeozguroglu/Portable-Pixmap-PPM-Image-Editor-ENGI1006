# Portable Pixmap (PPM) Image Editor

Columbia University - Computing for Engineers and Applied Scientists (ENGI1006)

Midterm Project. Spring 2020

Instructor: Timothy Paine

Detailed project instructions can be reached at https://github.com/egeozguroglu/Portable-Pixmap-PPM-Image-Editor-ENGI1006/blob/master/Midterm-ENGI1006.pdf

"In this assignment you will write an application in Python that takes as input a series of three similar
images and outputs a new image with unwanted objects from the original series removed. The images
will be provided as ppm files so all your program needs to do is edit them as text files to accomplish
your goal. I have provided three images attached to this assignment:
1. tetons1.ppm
2. tetons2.ppm
3. tetons3.ppm
See if you can guess which objects should be removed from these images. 

How do you remove the unwanted objects?
Notice that the unwanted objects appear in different parts of each image. This allows you to simply write
a new ppm file where each RGB value will be whatever the majority of the three images above suggests.
So in this case at least 2 of the files will always have the right pixel values.
More details please....
Write a module called effects. In it go ahead and write a function called object_filter that takes
as input (parameters) the file objects to filter and the name of the new file to create. The function should
then create a new ppm file using the majority rules approach described above for each pixel's RGB
value. 

but wait, there's more....
In addition to the object_filter function above write a function called shades_of_gray that
converts a color image to a black and white image. One way to convert a color image to black and white
is to replace each pixel's individual RGB values with the average of the three values. So for example if a
particular pixel had RGB values 100 200 300 you could change them to 200 200 200 for the black and
white version.
and one more thing….
Finally, you should write a function horizontal_flip which flips the image horiontally (e.g. swap left
and right)."
