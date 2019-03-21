## Model Based Custom Validator design for Python (Flask)
#### Model based custom validation for python. Use Flask server and mongo db. Integrate with any API development.  
<p align="center">
  <img width="280" height="160" src="https://kenya-tech.com/wp-content/uploads/2019/01/flask-python.png">
</p>

### Create [virtual environment]('https://docs.python.org/3/library/venv.html) and install requirements 
```sh
pip install -r requirements.txt
```
### Configure Database
#### From [db_config.json](src/db_config.json) configure datbase url, name, user and password 
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
## In model update collection name and desire fields name and fields type. For example see todo [model](src/models/todo.py) file
#### From [model](src/models) folder write your individual model and configure db collection name, fields name and fields type
#### Example
- In todo [model](src/models/todo.py) update collection name, fields name and fields type
```py
collection_name = 'todo'   # collection name
fields = {   
    "title"     : "string",
    "body"      : "string",
    "created"   : "datatime"
} 
```
- Update required fields, optional fields from todo [model](src/models/todo.py)
```py
create_required_fields = []  # example create_required_fields = ["title", "body"]
create_optional_fields = []  # example create_required_fields = ["created"]
update_required_fields = []
update_optional_fields = []
```
#### Example 
```py
create_required_fields = ["title", "body"] 
create_optional_fields = []  
update_required_fields = ["title", "body"]
update_optional_fields = []
```
### Lets run the App
```sh
python app.py 
```
