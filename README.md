## Model based Custom Validator design for Python (Flask)

<p align="center">
  <img width="220" height="130" src="https://kenya-tech.com/wp-content/uploads/2019/01/flask-python.png">
</p>

### Create virtual environment and install requirements 
```sh
pip install -r requirements.txt
```
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
- In todo [model](src/model/todo.py) update collection name and fields types
```py
collection_name = 'todo'
fields = {
    "title"     : "string",
    "body"      : "string",
    "created"   : "datatime"
} 
```
- Update required fields, optional fields from todo [model](src/model/todo.py)
```py
create_required_fields = []  # example create_required_fields = ["title", "body"]
create_optional_fields = []  # example create_required_fields = ["time"]
update_required_fields = []
update_optional_fields = []
```
### Lets run the App
```sh
python app.py 
```
