# test-datasets-creater
Test Database Creater is a Python application to create datasets from selected information from the loaded csv files and store them in the database.

***

In app/ folder are 5 scripts that:
- **load_files**: 
  loads files from input_files folder (class.csv, test.csv, level_test.csv);
  save them in app/files folder (class_file_load.csv, test_file_load.csv, level_test_file_load.csv);
  delete rows in the class_file_load that contain non ascii signs and backslash in 'name' column 
  (class_file_load_correct.csv);
- **create_dataset_utilization**
  create dataset which contain information about frequency of tests utilization by classes (final dataset test_utilization in app/files)
- **create_dataset_average**
  create dataset which contain information about average overall scores for tests in classes 
  (final dataset test_average_scores in app/files)
- **load_datasets_to_database**
  load the earlier prepared datasets to tables in a database 
  (name of database: TestDB in app/ folder)
- **main**
  do everything above step by step

***
  
To load csv files and manipulate them I used Pandas library.  
Another 4 scripts in tests/ folder contain unit tests (I used unittest library)

***   

**Requirements**   
url addresses to file: [requirements](https://github.com/trzcioli/test-datasets-creater/blob/master/requirements.txt) 


***

**Running**      
You can run application using command(from root of app):  
```console
python3 app/main.py 
```

You can also run only one of all scripts if you want, running the app with optional arguments:   
"-lf", "--load_files"    
"-cuti", "--create_dataset_utilization"    
"-cavg", "--create_dataset_average"    
"-ld", "--load_datasets_to_database"    

***

**Testing**  
You can run tests using command:    
```console
python3 -m unittest discover tests  
```

