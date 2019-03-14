## Python Custom Model Baised Form Validation 

#### Configure Database Url, Name, Username and Password in Databse Config File [db_config.json](src/db_config.json)
```json
 {
   "db": {
            "url" : "mongodb://localhost:27017/",
            "name" :"db_name",  
            "user" :"",
            "password" :""
    }
 }
```
#### From [model](src/model) folder write your individual database collection name and field type
#### Example
- In todo [model](src/model/todo) update collection name and fields types
```py
collection_name = 'todo'
fields = {
    "title"     : "string",
    "body"      : "string",
    "created"   : "datatime"
} 
```