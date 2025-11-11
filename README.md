## Instructions
1. [Create](https://console.cloud.google.com/projectcreate) a new project in Google Cloud  (20 secs)
2. [Enable](https://console.cloud.google.com/flows/enableapi?apiid=tasks.googleapis.com) Google Tasks API  (5 secs)
3. [Setup](https://console.cloud.google.com/auth/overview/create?project=aqueous-heading-477920-t8) project (20 secs)
4. In [Clients](https://console.cloud.google.com/auth/clients): Create client → Desktop App → Download JSON (20 secs)
5. Rename the file to "credentials.json" and move it to the folder with this project (20 secs)
6. Create new tasks list in your Google Tasks or use existing and paste its name to 'list_name.txt'
7. Install required python packages ('pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib')
8. All done! 

You can use script by launching 'main.py'\
If you want to change repetition intervals, look at row 32 in 'main.py'

If at some moment it stopped to work, just delete 'token.json'