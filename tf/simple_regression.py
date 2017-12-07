
import tensorflow as tf

#define variables 
a=tf.Variable(0.0,name="weights")
b=tf.Variable(0.0, name="bias")
#define input output 
x=tf.constant([1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])
y=tf.constant([3,6,9,12,15,18,21,24,27,30],dtype=tf.float32)

#model : Y=aX+b
y_pred = a*x+b
#loss
loss = tf.square(y-y_pred)
#define loss function optimizer 
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)
#run session
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	total_loss = 0
	for i in range(500):
		opt,my_loss=sess.run([optimizer,loss])
		total_loss += my_loss
	print str(total_loss)
	#assign a,b 	
	a,b = sess.run([a,b])
	print "a=" + str(a) + " &  b= " + str(b)

print "predicted value for 30 = " + str(30*a+b)

				
