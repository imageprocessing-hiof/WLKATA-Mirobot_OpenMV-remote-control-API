### Remote device

The remote device script is run on the OpenMV module. Here is a description of the functionality in this script.

```python
def calibration():
```
Initializes the dictionary of april tags used throughout the program.
Runs a loop 25 times and make a picture and store the found april tags 
in the dictionary.

Returns a the dictionary of april tags and a calibration_result,
True if all four tags where found, False if not.

```python
def get_roi(april_tags):
```
Finds the region of interest for where cubes are detected.

The algorithm loops through all the april tags,
finds its corners and loops through them.

For each corner, it's x and y coordinates will be
added to each other, If this sum is smaller than x_min + y_min
then this will be the new values for x_min and y_min.
And vice versa with larger values than x_max + y_max.

The width of the ROI is then found by subtracting x_min from x_max.
The height of the ROI is found by subtracting y_min from y_max.

The find blobs function that will be fed theese values requires
they are integers so therefore they are first rounded and then converted 
to integers before returning them.

The values returned will be the top left corner of the ROI given by
x_min and y_min. And also the width and height of the ROI. 
(x_min, y_min, w, h)


Importnat to remember is that ROI is found using QQVGA so
there is neccessary to call the function upscale_QQVGA_to_QVGA
on theese coordinates before using them to find blobs.


```python
def mask_april_tags(april_tags):
```
Using the inbuilt method to find the rectangle area of each april tag.
Then upscaling those coordinates from QQVGA to QVGA, and finally
drawing a black rectangle over them.

```python
def upscale_QQVGA_to_QVGA(x,y,w,h):
```
returns coordinates in QQVGA.

```python
def find_blobs(x,y,w,h):
```
Returns a list of blobs separated by color. 
Each color is also a list of its own, containing all
the blobs found of that color.

(white_blobs, red_blobs, green_blobs, blue_blobs)

```python
def get_blob_data(blobs, data_dict):
```
Parameters: The list of blobs returned from the fins_blobs function,
            and the data_dict containing data about position, orientation and 
            color of each blob.
            
Returns:    The data dictionary containg blob data.


Loops through the list of blob lists with the enumeration function of python, and so gaining
access to both the counter and the list.

Further loops through each list in the same manner and gains access to both counter and blob.

Gets the color by sending the "color_code" (counter from the first loop) to the function get_color().

The variable total count is used to keep an unique identifier for each blob to use as key while adding/updating
the dictionary.

The angle of rotation is found by calling the function get_angle_of_rotation_tan()

If the object is a cuboid or a rectangle is found by calling is_cuboid_or_rectangle()

Finally all data is stored to the dictionary like so,

data_dict[total_count] = (color, cx, cy, angle_of_rotation, is_cuboid).

```python
def get_color(color_code):
```
Translates the color code into its string representation.
0 = red,
1 = green,
2 = bluee

```python
def draw_blobs(blobs):
```
Draws a rectangle around the minimum area of each blob.
Also draws a cross at cx,cy of each blob.
