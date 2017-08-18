This repository contains code that performs a **catalogue matching** task on a custom apparel dataset with Deep Convolutional Neural Networks (DCNNs) techniques.
Please consider looking at the [report](https://github.com/tcosmo/dresscode/blob/master/report.pdf) for a full description of this work.
## Catalogue Matching
Given the catalogue of a retailer as a dataset of photos, the task is to indentificate which of these objects people are wearing in 
real life photos that we call **queries**.
## The Dataset
The chosen dataset simplfies the task. It consists in all the dresses of the H&M french online catalogue.    
The **real world** photos consists in the models that wear the items. You get associations like these:
### Catalogue Item
![alt text](old/ex_cat.jpg "An item of the catalogue")
### Corresponding Model (Query)
![alt text](old/ex_mod.jpg "A model wearing it")
### Getting the dataset
To get get the dataset you should execute *get_dataset.py* with python3.   
It will download the catalogue items in **db/robes/cat/** and the corresponding models in **db/robes/mod/**.   
At the time the experiment was made it consisted in 210 items, the photos are of good quality the whole takes about **200Mo**.    
**Important:** if you want to re-conduct the following results you should check that the file **to_ignore.txt** is still 
adequate to the DB. This variable stores ill-formed examples (where no models wear the item or ill formated jpg files).  
## Structure of this repo
Here's a short description of each file in this repo:    
- `report.pdf`: main file of this repo, it explains all of what this is about.      
- Results_DCNNs.ipynb: main results of our work, using deep neural features in order to retrieve intraclass apparels.      
- Results_ORB_BagOfWords.ipynb: implementation of "old-school" Bag-Of-Words method on the same problem for comparison purpose.
- Visualization_SOM.py: various features visualization with the Self-Organizing Map.     
- cache.py: caching tools, directly issued from this [awesome github repo](https://github.com/Hvass-Labs/TensorFlow-Tutorials).     
- data_manager.py: routines for data management.    
- download.py: models downloading utility, directly issued from this [awesome github repo](https://github.com/Hvass-Labs/TensorFlow-Tutorials).   
- get_dataset.py: our script for dataset gathering.    
- inception.py: manipulation of the inception v3 model, directly issued from this [awesome github repo](https://github.com/Hvass-Labs/TensorFlow-Tutorials).    
- rect_tools.py: routines for manipulating rectangles.     
- som.py: our implementation of the SOM.      
- to_ignore.txt: specify db items to ignore.           
- models/: where to store tensorflow models.     
- dumps/: where to store dumps of heavy calculations.     
