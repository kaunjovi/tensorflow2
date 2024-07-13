import tensorflow as tf
import numpy as np
from tensorflow import keras
# from typing import List

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

model.fit(xs, ys, epochs=500)

# This snippet works in standalone devbox, with following versions.
# Python 3.11.9
# absl-py==2.1.0
# astunparse==1.6.3
# certifi==2024.7.4
# charset-normalizer==3.3.2
# flatbuffers==24.3.25
# gast==0.6.0
# google-pasta==0.2.0
# grpcio==1.64.1
# h5py==3.11.0
# idna==3.7
# keras==3.4.1
# libclang==18.1.1
# Markdown==3.6
# markdown-it-py==3.0.0
# MarkupSafe==2.1.5
# mdurl==0.1.2
# ml-dtypes==0.3.2
# namex==0.0.8
# numpy==1.26.4
# opt-einsum==3.3.0
# optree==0.12.1
# packaging==24.1
# protobuf==4.25.3
# Pygments==2.18.0
# requests==2.32.3
# rich==13.7.1
# six==1.16.0
# tensorboard==2.16.2
# tensorboard-data-server==0.7.2
# tensorflow==2.16.2
# tensorflow-io-gcs-filesystem==0.37.1
# termcolor==2.4.0
# typing_extensions==4.12.2
# urllib3==2.2.2
# Werkzeug==3.0.3
# wrapt==1.16.0

x = np.array([10.0], dtype=float)
print(model.predict(x))

# This snippet works on colab, but not on the above dev box. 
print(model.predict([10.0]))

# print("Hello world")