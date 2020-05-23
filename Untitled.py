#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
import sys

first_filter_size = int(sys.argv[1])
count_conv_layer = int(sys.argv[2])
count_epoch = int(sys.argv[3])


# In[ ]:


(X_train, y_train), (X_test, y_test) = mnist.load_data()


# In[ ]:


X_train = X_train.reshape(60000,28,28,1)
X_test = X_test.reshape(10000,28,28,1)


# In[ ]:


y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


# In[ ]:


model = Sequential()#add model layers
model.add(Conv2D(first_filter_size, kernel_size=1, activation='relu', input_shape=(28,28,1)))
for i in range(count_conv_layer):
	model.add(Conv2D(first_filter_size//(2**i), kernel_size=1, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))


# In[ ]:


model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


# In[ ]:


history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=count_epoch)


accuracy_file = open('accuracy.txt', 'w+')
accuracy_file.writelines(history.history['accuracy'][::-1])
accuracy_file.close()



