import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, activation_function=None):
    # define layer name
    with tf.name_scope('layer'):
        # define weights name
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs


x_data = np.linspace(-1, 1, 300, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_in')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_in')

with tf.name_scope('l1'):
    l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

with tf.name_scope('prediction'):
    prediction = add_layer(l1, 10, 1, activation_function=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))

with tf.name_scope('train'):
    train_step = tf.train.AdamOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    writer = tf.summary.FileWriter("logs/", sess.graph)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x_data, y_data)
    plt.ion()
    plt.show()

    for i in range(1000):
        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
        if i % 50 == 0:
            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            prediction_value = sess.run(prediction, feed_dict={xs: x_data})
            # plot the prediction
            lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
            plt.pause(0.1)
            print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))

