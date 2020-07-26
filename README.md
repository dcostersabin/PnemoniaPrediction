# Pneumonia Prediction
Predicts The Case Of Pneumonia From The Given Images with a web based monitoring system for realtime COVID-19 patients in different countries

It uses rapid api to get the data where django controls the backend and UI is generated using Angular

-------------------------------- __To Run The Monitoring System__ --------------------------------------
1. install ng cli and django 
2. install bootstrap using npm or do __npm install__
3. get your key from __Rapi Api__ [link]: [https://rapidapi.com/astsiatsko/api/coronavirus-monitor]
4. Modify __x-rapidapi-key__ in django server on cacheupdate/updater.py under __HEADERS__
5. go to backend and run __python manage.py runserver__
6. to start __UI__ run __ng serve__

---------------------------------- __To Run Prediction Model__ -------------------------------------
1. install __TensorFlow__ or __KERAS__ 
2. modify the variables in __cnn.py__
3. then run __python cnn.py__ 
4. after the training is completed the model is saved inside __models__
5. load __myModel__ using __TensorFlow__ and use __.predict__ method 



==========ENJOY LEARNING EVERYDAY==========================




__First test with only 5 epoch gave an accuracy of 91% on testing and 95%+ on training
There are lot of things that can be improve since i was limited by my computing power try your best to tweak the neural network to predict more accurate result__

__[Dataset (PROVIDED VIA KAGGLE)]__

