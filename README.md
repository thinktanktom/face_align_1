# Facial Recognition - Aligning faces in images for better results
This guide will showcase how one can de-skew skewed images so that facial recognition models have a higher chance of detecting faces in the images. The complete alignment procedure has been divided into two parts. The first part rotates the image until a face is recognized, the second part aligns the face so as to better the odds of it being recognized. 


# Requirements and Installation
I used python to implement this project so the requirements mostly refer to python libraries that can be installed via pip.

If you are using a newer version of linux you will find that pip is no longer available by default. You can either install pip3 using the following command:

    sudo apt-get install python3-pip

Or if you still prefer to use pip you can download it:

    sudo add-apt-repository universe

    sudo apt update

    sudo apt install python2

    curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py

    sudo python2 get-pip.py

Now after getting your preferred version of pip, you now need to download the required libraries. I recommend setting up a virtual environment before downloading these libraries so that dependencies from different projects don't mix up and cause problems in the future.
You can take the following steps to set up a virtual environment in your preferred directory:

1. First create a directory for your installation:

        mkdir .virtualenv

2. Install virtualenvwrapper with pip3. If you wish to use pip replace 'pip3' with 'pip:

        pip3 install virtualenvwrapper

3. Now you must access your .bashrc file and add the virtualenvwrapper environment variable. You can use any editor for this but I prefer Vim.

        vim .bashrc

4. Add the following text to the .bashrc file:

   ```
     #Virtualenvwrapper settings:

     export WORKON_HOME=$HOME/.virtualenvs

     VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3

     . /usr/local/bin/virtualenvwrapper.sh 
 
5. After saving your edit you can create a virtual environment in the directory of your choice using the following command:
    
    ```
    mkvirtualenv name_of_your_env
6.  To deactivate the environment, use the command:

    
        deactivate
    
    And to work on a previously created environment use the command:
    
     
        workon
     
After setting up your virtual environment you have to download OpenCV and Numpy libraries for image processing.

To download OpenCV, take the following steps:

```
    sudo apt update
    sudo apt install libopencv-dev python3-opencv
```
To verify the installation type in the following command:

    python3 -c "import cv2; print(cv2.__version__)"

If you get your OpenCV version as your output then you have successfully installed OpenCV.

To download Numpy, simply type in the following command:

    pip3 install numpy


# Working

The logic behind the program is very easy to understand. We simply rotate the image until the face_cascade detector recognizes a face in the image. On doing so it breaks out of the loop and gives us the aligned image. 

# Fin 

The second part of this project which includes further alignment of the resultant image will be coming soon. I will also dockerize both parts so that you can sample them without much hassle.