# Process Images with Sobel Operator
For purposes such as edge detection in images, it can be useful to approximate the
change in image intensity with respect to position. This can be done by computing a
convolution of the image with the Sobel operator. This program iteratively calculates
the convolution using horizontal and vertical operators and then displays the gradient.
Note: This program uses a relatively slow algorithm. Actual CV applications make use of
the convolution theorem and the fast Fourier transform algorithm.

## Usage:
`python image_derivatives.py --image your_image.jpg`
## Example:
