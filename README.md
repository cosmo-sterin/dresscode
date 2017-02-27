# DressCode
This repository contains code that performs a **catalogue matching** task on a custom dataset.
## Catalogue Matching
Given the catalogue of a retailer as a dataset of photos, the task is to indentificate which of these objects people are wearing in 
real life photos that we call **queries**.
## The Dataset
We choose a dataset that simplfies a bit the task. It consists in all the dresses of the H&M french online catalogue.    
The **real world** photos consists in the models that wear the items. You get associations like these:
## Catalogue Item
![alt text](ex_cat.jpg "An item of the catalogue")
## Corresponding Model (Query)
![alt text](ex_mod.jpg "A model wearing it")
## Getting the dataset
To get get the dataset you should execute *get_dataset.py* with python3.   
It will download the catalogue items in **db/robes/cat/** and the corresponding models in **db/robes/mod/**.   
At the time the experiment was made it consisted in 210 items, the photos are of good quality the whole takes about **200Mo**.    
**Important:** if you want to re-compute the following results you should check that the variable **to_ignore** is still 
adequate to the DB. This variable stores ill-formed examples (where no models wear the item or ill formated jpg files).   
There were 10 such items when the exeperiment was made.   
