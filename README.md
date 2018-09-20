# Driveinformed: Box Detection

This is a part of coding challenge provided by DriveInformed (https://github.com/Informed/hiring/tree/master/coding_challenges/box_detection#box-detection). 

### Dependencies

```
Python 3.6.5
OpenCV 3.4.1
```

### Installing

Clone the repository and organize the data in the following format.

```
driveinformed_detectbox
|     detect_boxes.py
|_____input/
|
|_____output/

```
Add pictures in .jpg format that you want to test in ```input/```


## Running the tests

To run the test
```
python3 detect_boxes.py --inputdir input/ --outputdir output/
```

### Sample Output

![Sample Input](https://github.com/harshilprajapati/driveinformed_detectbox/input/1099.png)

![Sample Input](https://github.com/harshilprajapati/driveinformed_detectbox/output/1099.png)

```output/1099.json```
```
{
    "boxes": [
        {
            "points": [
                [
                    0,
                    0
                ],
                [
                    0,
                    952
                ],
                [
                    1432,
                    0
                ],
                [
                    1432,
                    952
                ]
            ]
        },
        {
            "points": [
                [
                    938,
                    815
                ],
                [
                    938,
                    909
                ],
                [
                    1205,
                    815
                ],
                [
                    1205,
                    909
                ]
            ]
        },
        .
        .
        .
      ]
}
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV documentation
* DriveInformed
