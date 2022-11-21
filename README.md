# Process Images with Sobel Operator
For purposes such as edge detection in images it can be useful to approximate the
change in image intensity with respect to position. This can be done by computing a
convolution of the image with the Sobel operator. This program iteratively calculates
the convolution using horizontal and vertical operators and then displays the gradient.

## Usage:
`python image_derivatives.py --image your_image.jpg`
## Example:
![diffeq1](https://user-images.githubusercontent.com/47088251/203008298-d1eeeed8-c67d-4a26-82c0-064ff9584d70.jpg)
![diffeq](https://user-images.githubusercontent.com/47088251/203008292-21f94b9d-78bf-428f-9d49-595ea8ce9449.jpg)
