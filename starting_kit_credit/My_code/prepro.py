# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 22:37:06 2018

@author: PC MILO fixe
"""

from sys import argv, path
path.append ("../ingestion_program") # Contains libraries you will need
from data_manager import DataManager  # such as DataManager

from sklearn.base import BaseEstimator
from sklearn.decomposition import PCA
from sklearn.cluster import FeatureAgglomeration
from sklearn.feature_selection import VarianceThreshold
from sklearn.cluster import FeatureAgglomeration

from sklearn.pipeline import Pipeline

class Preprocessor(BaseEstimator):
    def __init__(self):
        estimators = [('reduce_dim', PCA(n_components=20)), ('cluster',FeatureAgglomeration(n_clusters = 2) )]
        pipe = Pipeline(estimators)
        self.transformer = pipe
        
        
        #comment l'utiliser : tu met les méthodes que tu veux employer dans 
        #l'ordre dans lequel tu vux les employer dans la liste estimator et c'est bon
        
        
        #self.transformer = PCA(n_components=2)
        #self.transformer = FeatureAgglomeration(n_clusters=32)

    def fit(self, X, y=None):
        return self.transformer.fit(X, y)

    def fit_transform(self, X, y=None):
        return self.transformer.fit_transform(X)

    def transform(self, X, y=None):
        return self.transformer.transform(X)
    
if __name__=="__main__":
    # We can use this to run this file as a script and test the Preprocessor
    if len(argv)==1: # Use the default input and output directories if no arguments are provided
        input_dir = "../public_data"
        output_dir = "../results" # Create this directory if it does not exist
    else:
        input_dir = argv[1]
        output_dir = argv[2];
    
    basename = 'credit'
    D = DataManager(basename, input_dir) # Load data
    print("*** Original data ***")
    print D
    
    Prepro = Preprocessor()
 
    # Preprocess on the data and load it back into D
    D.data['X_train'] = Prepro.fit_transform(D.data['X_train'], D.data['Y_train'])
    D.data['X_valid'] = Prepro.transform(D.data['X_valid'])
    D.data['X_test'] = Prepro.transform(D.data['X_test'])
  
    # Here show something that proves that the preprocessing worked fine
    print("*** Transformed data ***")
    print D