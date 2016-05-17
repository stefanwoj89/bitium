# bitium

Hey everyone,

You'll need Python 2.xx, virtualenv and a clone of this repo.

## Instructions

**Setup a virtual env with the command:**
```
virtualenv ENV
```
**Activate your virtualenv:**
```
source ./ENV/bin/activate
```
*Now you're using your virtualenv! To install the requirements (django, django-registration etc.) there is a requirements.txt file at the top level of the django project directory.*
**Change directory to that root directory and enter the following command:**
```
pip install -r requirements.txt
```

*There are only two major and one minor requirement. Django and django-registration (a user registration tool) hopefully these have installed properly.*

**Run our database migrations.**

```
python manage.py migrate
```

*Now we have our db setup! Victory is nigh.*


**Last step is to create an administrator.**

```
python manage.py createsuperuser
```

**To run the server:**
```
python manage.py runserver
```

Now if all went without a hitch you may login, view and alter DB rows via http://127.0.0.1:8000/admin/.

This is where you can enter in the apps with appropriate asset url for testing. To test you may open an incognito window in chrome for a clean cache.

1. Login via the admin above and insert app entries with an app name and url of an app asset. 

2. Login normally via http://127.0.0.1:8000/accounts/login/. You may use the same login as your admin.

3. Once logged in, the javascript would have already run as you are now at accounts/profile. Your apps should appear gray in color.

4. Now open a new tab and try to hit an app asset url you've stored in the DB to simulate app use.

5. Return to your accounts/profile tab and refresh. The used app should now appear green. You may repeat step 4-5 to test other app assets.

6. To reset state, you have to delete the AppUser table entries generated when an app is found as visited. go back to http://127.0.0.1:8000/admin/ and delete the entries.

7. That's it!

Design:

- There are two tables, App and AppUser, with AppUser establishing relationships between Apps and Users

- accounts/profile is an API point that is used for both POST and GET. A lot of the boiler plate code in there is formatting for javascript usage.

- The template uses the template engine for populating the initial list of targets when a GET request is called for accounts/profile. The POST ajax request is called once after all targets have been tested. This is for efficiency. Once called, the screen is updated once the ajax call returns with a response. This is done asynchronously.

- Only a little bit of the code has been altered or removed from the original cache source.

Thank you for your time!

Stefan


