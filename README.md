# django_rest_example

# **People Management App**
run server command:         python .\manage.py runserver
server address and port:    http://127.0.0.1:8000/

**Whole API swagger documentation:**
http://127.0.0.1:8000/swagger

**Grouping API documentation:**
http://127.0.0.1:8000/grouping/people               - get/post name,age of people
http://127.0.0.1:8000/grouping/people/<id>          - get/post/update/delete id,name,age,group of person
http://127.0.0.1:8000/grouping/groups               - get/post name of groups
http://127.0.0.1:8000/grouping/groups/<id>          - get/post/update/delete name of group
http://127.0.0.1:8000/grouping/people_groups        - get id,name,age,group of people


**Activity_app API documentation:**
http://127.0.0.1:8000/activity/activity_list        - get/post name of activity 
http://127.0.0.1:8000/activity/activity_list/<id>   - get/post name of activity 
http://127.0.0.1:8000/activity/users                - get activities of all users 
http://127.0.0.1:8000/activity/users/<id>           - get activities of user 


**Superuser Credentials:**
login:  admin
pass:   Strongpass123


### **Grouping app documentation**

Rest API for create/display/edit/delete people and groups. People can be added/removed to groups.

People:
    - name
    - age
Group:
    - name


### **Activity app documentation**

Simple Rest API endpoint to write, display and delete user activity (after login). Delete permission is only for is_staff user.



