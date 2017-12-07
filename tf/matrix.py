import tensorflow as tf

a=tf.constant([1,2,3,4,5,6,7,8,9],name="a",shape=(3,3))
b=tf.constant([1,1,1,1,1,1,1,1,1],name="b",shape=(3,3))
u=tf.Variable(tf.ones([3,3]))
#use reshape to make diminsons

#global varibale initialization
init=tf.global_variables_initializer()

c=tf.matmul(tf.reshape(a,[3,3]),tf.reshape(b,[3,3]))
with tf.Session() as sess:
	#global variables
	sess.run(init)
	print a
	print b
	print u.eval()
	print sess.run(c)
	
