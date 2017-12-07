import tensorflow as tf

a=tf.constant([1,2,3,4,5,6,7,8,9])
b=tf.constant([1,0,0,0,1,0,0,0,1])

#use reshape to make diminsons
c=tf.matmul(tf.reshape(a,[3,3]),tf.reshape(b,[3,3]))
with tf.Session() as sess:
	print sess.run(c)
	
