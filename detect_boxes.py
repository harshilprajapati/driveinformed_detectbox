"""Finds the position boxes from images of forms"""
#title           : findcodes.py
#author          : Harshil Prajapati
#date            : 09-20-2018
#version         : 0.1
#usage           : python3 detect_boxes.py --inputdir input/ --outputdir output/
#python_version  : 3.6.5
#=============================================================================

# import libraries
from json import dumps
from os import listdir,getcwd
from argparse import ArgumentParser
import cv2

def get_edges(img):
    """"Get binary image post thresholding"""

    # convert to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # applying 5x5 gaussian filter to remove noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # use adaptive threshold with neighbourhood size 11 x 2
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
            cv2.THRESH_BINARY, 11, 2)

    return thresh

def get_boxes(contours, img):
    """Find boxs from list of countours, create a dump of coordinates and """
    # initalize list
    boxes = []
    for contour in contours:
        # Get an approximate contour with specifications
        approx_contour = cv2.approxPolyDP(contour, 0.025 * cv2.arcLength(contour, True), True)

        # for contours of interest
        if len(approx_contour) == 4:

            # get bounding box
            (x_pos, y_pos, width_box, height_box) = cv2.boundingRect(approx_contour)

            # for box larger than a threshold
            if height_box >= 10 and width_box >= 10:

                # append coordinates
                boxes.append({"points": [[x_pos, y_pos], [x_pos, y_pos+height_box], \
                [x_pos+width_box, y_pos], [x_pos+width_box, y_pos+height_box]]})

                # draw the box on image
                cv2.rectangle(img, (x_pos, y_pos), (x_pos + width_box, y_pos + height_box),\
                 (0, 255, 0), 3)

    return boxes, img

def save_data(out_dir, input_image, boxes, img):
    """Save Coordinates to json and images to output"""

    # dict to save data
    dump_data = dict()

    # assign the data to dict
    dump_data["boxes"] = boxes

    # dump coordinates to json file
    fname = input_image.replace('.jpg', '.json')
    write_json(dump_data, out_dir+fname)

    # save image
    cv2.imwrite(out_dir+input_image, img)

def write_json(data, fname):
    """Save dictionary into a .json file"""

    # open file
    file_open = open(fname, 'w')

    # write data
    file_open.write(dumps(data, indent=4))

    # close file
    file_open.close()

def main():
    """Main Function"""
    # get input from commandline
    args_parser = ArgumentParser()
    args_parser.add_argument("--inputdir", type=str, nargs=1, required=True, dest='inputdir')
    args_parser.add_argument("--outputdir", type=str, nargs=1, required=True, dest='outputdir')
    commandLine_Args = args_parser.parse_args()
    in_dir = commandLine_Args.inputdir[0]
    out_dir = commandLine_Args.outputdir[0]

    # list of files in input library
    list_images = listdir(in_dir)

    for input_image in list_images:

        # if the file is a '.jpg'
        if '.jpg' in input_image:
            
            # read the image
            img = cv2.imread(getcwd()+'/'+in_dir+input_image)

            # get binary image post thresholding
            thresh = get_edges(img)

            # find contours
            contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]

            # get coordinates of boxes and image with thats
            boxes, img = get_boxes(contours, img)

            # save data to output directory
            save_data(out_dir, input_image, boxes, img)

if __name__ == '__main__':
    main()
