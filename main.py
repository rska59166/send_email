# In[ ]:


from sklearn import datasets
import matplotlib.pyplot as plt


# In[ ]:


digits = datasets.load_digits()
digits.images[0]


# In[ ]:


_, axes =  plt.subplots(nrows=1, ncols=5, figsize=(8, 8))
for axis, image, label in zip(axes, digits.images, digits.target):
    axis.imshow(image, cmap=plt.cm.gray_r)
    axis.set_title(f"num: {label}")


# In[ ]:


from sklearn.model_selection import train_test_split


n = len(digits.images)
data = digits.images.reshape((n, -1))

X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.3, shuffle=False
)

X_train.shape, X_test.shape


# In[ ]:


from sklearn.linear_model import LogisticRegression


model = LogisticRegression(fit_intercept=True,
                         multi_class='auto',
                         penalty='l1',  # lasso regression
                         solver='saga',
                         max_iter=1000,
                         C=50,
                         verbose=2,  # output progress
                         n_jobs=5,  # parallelize over 5 processes
                         tol=0.01
                         )

model.fit(X_train, y_train)


# In[ ]:


predicted = model.predict(X_test)
predicted[0:10], y_test[0:10]


# 

# In[ ]:


test_images = X_test.reshape((X_test.shape[0], 8, 8))

_, axes =  plt.subplots(nrows=1, ncols=5, figsize=(8, 8))
for ax, image, prediction in zip(axes, test_images, predicted):
    ax.imshow(image, cmap=plt.cm.gray_r)
    ax.set_title(f"predict: {prediction}")


# In[ ]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test, predicted)
