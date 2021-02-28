# Simple Face Detection

Simple Face Detection using Python and OpenCV.

---

## Arguments

### `--type`

* **Type**: int
* **Description**: 1 for image, 2 for video
* **Default**: 1

(Note: to exit video mode press ESC key)

### `--source`

* **Type**: string
* **Description**: a string of the image/video to read, there are a few samples in media folder. If you want to use new samples they must be added to the folder
* **Default**: a sample image or video depending on the type

### `--webcam`

* **Type**: boolean
* **Description**: if you call it it becomes true and activates webcam mode
* **Default**: false

---

### Examples:

```
python face_detection.py --webcam
```
Will take a webcam picture and use it.

```
python face_detection.py --source ocean.jpg
```
Will use the image `ocean.jpg` from the media folder.

```
python face_detection.py --type 2 --webcam
```
Will use webcam stream as a video
