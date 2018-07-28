## Face tracking

In this project was created an application that perform face tracking in real-time.

## Hardware configuration

- OS: Linux [Ubuntu 16.04 LTS - 64 bits]
- GPU: NVIDIA GeForce GTX 1060 (6GB)
- Memory: 16 GB
- Processor: Intel Core i7 (7th Gen)

## Instalation

1. Install virtualenv using step #3 from this [post](https://www.pyimagesearch.com/2017/09/27/setting-up-ubuntu-16-04-cuda-gpu-for-deep-learning-with-python/).
2. Create a new env using this command ```mkvirtualenv "name_env" -p python3```. Change "name_env" for your choice name.
3. Enter inside env: ```workon "name_env"```. Change "name_env" for your choice name.
4. Clone this respository using ```git clone https://github.com/ximenesfel/face_tracking.git``` command.
5. Install dependences: ```pip -r requirements.txt```.

## Usage

Run 

```sh
$ cd [project root]
$ python object_tracker.py --prototxt models/deploy.prototxt --model models/res10_300x300_ssd_iter_140000.caffemodel
```
Quit

```sh
Press "q" key
```

## Reference

Thanks to Adrian Rosebrock for [Simple object tracking with OpenCV](https://www.pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/) post.