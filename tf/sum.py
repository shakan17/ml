import tensorflow as tf



#demo constant - graph 
#tensorboard tensorboard --logdir="./graphs" --port 6006  
a=tf.constant(4,name="a")
b=tf.constant(5,name="b")
c=tf.add([4,5,6], [5,5,6])
d=tf.subtract([4,4,5],[4,5,6])
f=tf.add(c,d,name="Result")
with tf.Session() as sess:
	sum_r,diff_r,result  = sess.run([c,d,f])
	writer=tf.summary.FileWriter("./graphs",sess.graph)
	print "Diff = " + str(diff_r) + " Sum = " + str(sum_r)
	writer.close()



