from java import jclass
import numpy as np
import tensorflow as tf
# import torch

def greet(name):
    print("--- hello,%s ---" % name)

def add(a,b):
    return a + b

def sub(count,a=0,b=0,c=0):
    return count - a - b -c

def get_list(a,b,c,d):
    return [a,b,c,d]

def print_list(data):
    print(type(data))
    # 遍历Java的ArrayList对象
    for i in range(data.size()):
        print(data.get(i))

def print_numpy():
    y = np.zeros((5,), dtype = np.int)
    print(y)

def test_tensorflow():
    # print(tf.test.is_gpu_available())
    # print(tf.__version__)
    # a = tf.constant(1.)
    # b = tf.constant(2.)
    # print(a+b)
    return tf.test.is_gpu_available()
    # print('GPU:', tf.test.is_gpu_available())
    # print(torch.cuda.is_available())
    # a = tf.constant(1)
    # b = tf.constant(2)
    # print(sess.run(a+b))


# # python调用Java类
# def get_java_bean():
#     JavaBean = jclass("com.wwb.test.python.JavaBean")#用自己的包名
#     jb = JavaBean("python")
#     jb.setData("json")
#     jb.setData("xml")
#     jb.setData("xhtml")
#     return jb
