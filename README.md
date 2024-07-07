# tensorflow2
TensorFlow2

## Get started. 

1. Create a new folder in the git repository of your choice. 
1. Initialized it with README.md. 
1. Open your dev box. Open your terminal. 
1. Go to whichever location you want your code folders to be in. 
1. Cone the online git folder to your dev box. 

```
kaunjovi@devbook ~ % cd code 
kaunjovi@devbook code % git clone git@github.com:kaunjovi/tensorflow2.git
Cloning into 'tensorflow2'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
```

1. Peek into the folder and check if README.md is there. 
1. Open the folder in your favorite editor. 

```
kaunjovi@devbook code % cd tensorflow2
kaunjovi@devbook tensorflow2 % ls -lart
total 8
drwxr-xr-x   6 kaunjovi  staff  192 Jul  7 15:55 ..
drwxr-xr-x   4 kaunjovi  staff  128 Jul  7 15:55 .
-rw-r--r--   1 kaunjovi  staff   26 Jul  7 15:55 README.md
drwxr-xr-x  12 kaunjovi  staff  384 Jul  7 15:55 .git
kaunjovi@devbook tensorflow2 % codium .
```

1. Happy coding. 

## [Setting up for TensorFlow2](https://www.tensorflow.org/install)

### Pre Requisites 

1. Python 3.8–3.11

## Which python do we have 

```
kaunjovi@devbook tensorflow2 % python3 --version 
Python 3.12.3
```

1. We have 3.12. TensorFlow2 needs no more than 3.11. 
1. Check [python downloads](https://www.python.org/downloads/). 
1. Python 3.11.9 April 2, 2024 seems ok. 
1. That can work only on for macOS 10.9 and later. We have 14.4. So, go ahead and install. 
1. Post this install check python version again. 

```
kaunjovi@devbook tensorflow2 % ls -lart 
total 8
drwxr-xr-x   6 kaunjovi  staff   192 Jul  7 15:55 ..
drwxr-xr-x   4 kaunjovi  staff   128 Jul  7 15:55 .
-rw-r--r--   1 kaunjovi  staff  1567 Jul  7 16:18 README.md
drwxr-xr-x  15 kaunjovi  staff   480 Jul  7 16:18 .git
kaunjovi@devbook tensorflow2 % python3 --version 
Python 3.11.9
```

## Create a virtual environment with these requirements

1. Create a venv called .venv 
1. Check if the new folder was indeed made. 

```
kaunjovi@devbook tensorflow2 % python3 -m venv .venv
kaunjovi@devbook tensorflow2 % ls -lart 
total 8
drwxr-xr-x   6 kaunjovi  staff   192 Jul  7 15:55 ..
-rw-r--r--   1 kaunjovi  staff  1962 Jul  7 16:26 README.md
drwxr-xr-x  15 kaunjovi  staff   480 Jul  7 16:27 .git
drwxr-xr-x   5 kaunjovi  staff   160 Jul  7 16:34 .
drwxr-xr-x   6 kaunjovi  staff   192 Jul  7 16:34 .venv
```

1. Activate it 
1. Check if python3 is being picked from the local folder 

```
kaunjovi@devbook tensorflow2 % source .venv/bin/activate

(.venv) kaunjovi@devbook tensorflow2 % which python3 
/Users/kaunjovi/code/tensorflow2/.venv/bin/python3
```

1. Install pip so you can install other stuff. 

```
(.venv) kaunjovi@devbook tensorflow2 % pip install --upgrade pip
Requirement already satisfied: pip in ./.venv/lib/python3.11/site-packages (24.0)
Collecting pip
  Downloading pip-24.1.1-py3-none-any.whl.metadata (3.6 kB)
Downloading pip-24.1.1-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 2.4 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.0
    Uninstalling pip-24.0:
      Successfully uninstalled pip-24.0
Successfully installed pip-24.1.1

(.venv) kaunjovi@devbook tensorflow2 % where pip 
/Users/kaunjovi/code/tensorflow2/.venv/bin/pip
```

1. Install TensorFlow2
2. Don't forget to create .gitignore before this and add /.venv to it 

```
(.venv) kaunjovi@devbook tensorflow2 % pip install tensorflow
A lot of downloads 
A lot of files will show up in your .venv folder. 
```



## TensorFlow 

- TensorFlow makes it easy to create ML models that can run in any environment. 

- Install TensorFlow 2 
- Python 3.8–3.11 - we have Python 3.12.3
- macOS 10.12.6 (Sierra) or later (no GPU support) - we have Sonoma 14.4

```
pip install --upgrade pip
pip install tensorflow
```




