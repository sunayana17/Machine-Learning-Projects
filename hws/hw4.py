# -*- coding: utf-8 -*-
"""hw4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sQTRntvaa0bASR4qiXrjlakBGTObO_9j
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale, normalize

data = np.load('/content/drive/MyDrive/Colab Notebooks/SML/pca_data.npz')
d= data['data']

print(d.shape)

plt.scatter(d[:, 0], d[:, 1], alpha=1, label="samples")

pca = PCA(n_components=2)

pca.fit(d)

print(pca.explained_variance_ratio_)

print(pca.singular_values_)

pca.get_covariance()

pca.get_params([d])

pca.components_

pca.mean_

pca.explained_variance_

import numpy as np

X_meaned = d - np.mean(d , axis = 0)

cov_mat = np.cov(X_meaned , rowvar = False)

cov_mat

eigen_values , eigen_vectors = np.linalg.eigh(cov_mat)

#sort the eigenvalues in descending order
sorted_index = np.argsort(eigen_values)[::-1]
 
sorted_eigenvalue = eigen_values[sorted_index]
#similarly sort the eigenvectors 
sorted_eigenvectors = eigen_vectors[:,sorted_index]

n_components = 2 #you can select any number of components.
eigenvector_subset = sorted_eigenvectors[:,0:n_components]

X_reduced = np.dot(eigenvector_subset.transpose(),X_meaned.transpose()).transpose()

eigenvector_subset

print(pca.explained_variance_ratio_)
print(pca.components_)
print(pca.mean_)

plt.scatter(d[:, 0], d[:, 1], alpha=1, label="samples")
plt.quiver(pca.mean_[0], pca.mean_[1], pca.components_[0][0], pca.components_[0][1],
         scale_units='inches',scale=1/pca.explained_variance_ratio_[0],units='inches')
plt.quiver(pca.mean_[0], pca.mean_[1], pca.components_[1][0], pca.components_[1][1],
        scale_units='inches',scale=1/pca.explained_variance_ratio_[1],units='inches')

