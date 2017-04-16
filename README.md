# Image-management-api

clone or download the repo.
open project folder.
open command line.
execute start.bat

navigate to http://localhost:8000/

you should see "Hello World"

To generate the api key user needs to run the following api.

http://localhost:8000/getkey/

copy the api key.

now go to the url 
http://localhost:8000/upload/

provide the copied api key and browse the image file you wish to upload, and click on upload.your file should get saved.

Now go to 

http://localhost:8000/list/[your_api_key]

you should see all the images related to that particular api key.
To view an image either click on it or give the image id(shown before the img name)  after the url like below...

http://localhost:8000/list/[your_api_key]/1

you should see your uploaded img.

now to delete the image, write delete after the image id as given below.

http://localhost:8000/list/[your_api_key]/1/delete



in case for any clarification reach out to me on DivineDeepak92@gmail.com
