#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.datasets import mnist


# In[2]:


(X_train, y_train), (X_test, y_test) = mnist.load_data()


# In[5]:


X_train = X_train.reshape(60000,28,28,1)
X_test = X_test.reshape(10000,28,28,1)


# In[6]:


from keras.utils import to_categorical#one-hot encode target column
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


# In[32]:


from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten#create model
model = Sequential()#add model layers
model.add(Conv2D(1, kernel_size=1, activation='relu', input_shape=(28,28,1)))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))


# In[33]:


#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


# In[34]:


#train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=1)


# In[19]:


history.history['accuracy']


# In[ ]:




