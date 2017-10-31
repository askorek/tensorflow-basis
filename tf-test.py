import tensorflow as tf

tf_session = tf.Session()
x = tf.constant(1)
y = tf.constant(1)
print(tf_session.run(x + y))
tf_session.close()