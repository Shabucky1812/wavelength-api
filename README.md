# Wavelength API

Wavelength API provides the backend functionality needed by the Wavelength website (found using the link below). How a user behaves with profiles, tracks, reviews, and followers is defined here and made available to the Wavelength frontend by certain url endpoints. As this repo is only the backend for the project, to find a more thorough explanation of how the features shown in this repo interact directly with users, please head over to the main repo.

[Find Wavelength's main repo here](https://github.com/Shabucky1812/wavelength-front)

To view the planning board used throughout this project's creation, [use this link](https://github.com/users/Shabucky1812/projects/3).

## Contents

- [UX](#ux)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Testing](#testing)
- [Credits](#credits)

## UX

### User Stories

#### EPIC: Profiles

- US01 - Create Profile

  - As a developer I can automatically create a corresponding profile for each new user so that every user has there own profile that belongs to them.

- US02 - Edit Profile

  - As a developer I can allow users to edit there own profiles so that every user can customize their identity within the application.

- US03 - Delete Profile

  - As a developer I can allow users to delete their profile so that a user that no longer wants to use Wavelength can remove their profile.

- US04 - View Profiles

  - As a developer I can allow users to view profiles so that users can interact with each other.

#### EPIC: Followers

- US05 - Follow Users

  - As a developer I can allow users to follow other users so that users can tailor their feeds by following profiles that share content relevant to them.

- US06 - Unfollow Users

  - As a developer I can allow users to unfollow accounts they were previously following so that users can remove content from their feed that they no longer wish to interact with.

#### EPIC: Tracks

- US07 - Share Tracks

  - As a developer I can let users create instances of the track model so that they can share music that they have been enjoying.

- US08 - Edit Track

  - As a developer I can allow users to edit the details of tracks they have shared so that they can fix any mistakes they may have made whilst creating the instance/reflect any opinion changes they have had about the track.

- US09 - Delete Track

  - As a developer I can allow users to delete tracks that they have shared so that users can remove tracks that the no longer want on their profile.

- US10 - View Tracks (list view)

  - As a developer I can display a list view of all shared tracks so that users can explore new music.

- US11 - View Track (detail view)

  - As a developer I can display a detailed view of an individual track so that users can read a track's reviews and add their own.

#### EPIC: Reviews

- US12 - Create Review

  - As a developer I can allow users to review shared tracks so that they can share their opinion on the music.

- US13 - Edit Review

  - As a developer I can allow users to edit any review that they have created so that they can change their reviews if their opinions about the track change.

- US14 - Delete Review

  - As a developer I can allow users to delete any of their reviews so that they can remove them if they would like to.

- US15 - View Reviews

  - As a developer I can display all of the reviews for a track beneath it in the detailed view so that users can see what other users are thinking about a track.

### Entity-Relationship Diagram

For planning the data model for Wavelength, I created this ER diagram (using [diagrams.net](https://www.diagrams.net/)) to demonstrate how each of the custom models for the website would interact and what fields they should have.

![Entity-Relationship Diagram for custom wavelength models.](/documentation/readme/er-diagram.png)

## Features

### Existing Features

As the API is intended to serve as the backend for the Wavelength website, no navigation is present throughout the development version. Instead each page is accessed by going to certain urls. The features below are associated with these urls.

- **F01 - Welcome Message**  
  ![Root route](/documentation/readme/root_route.png)  
  The root route ("/") for the API renders the above content, a simple welcome message.

- **F02 - Log in + out**  
  ![Login route](/documentation/readme/log_in.png)  
  The login route ("/api-auth/login/?next=/") for the API renders the above content. This is just a simple login form provided by Django Rest Framework. Once logged in,the log in button that was previously located at the right of the header becomes a dropdown that lets the user log out.

- **F03 - Profiles List**  
  ![Profiles list view header](/documentation/readme/profiles_list_header.png)  
  ![Profiles list view](/documentation/readme/profiles_list.png)  
  The profiles list route ("/profiles/") for the API renders the above content. The filter option in the header lets the user order the profiles (ascending/descending) by: tracks_count, followers_count and following_count. The user can also search the profiles by username and filter them by users they are following and are being followed by. Below the header, the profiles are listed by the time they were created by default.

- **F04 - Profile Detail**  
  ![Profile detail view](/documentation/readme/profile_detail.png)  
  The profile detail route ("/profiles/:id/") for the API renders the above content. This view renders the details of a single profile, decided by the id in the url. If the user is the owner of the profile, they can use the form at the bottom to change the profiles image.

- **F05 - Tracks List**  
  ![Tracks list view](/documentation/readme/tracks_list.png)  
  ![Track create form](/documentation/readme/tracks_create_form.png)  
  The tracks list route ("/tracks/") for the API renders the above content. The filter option in the header lets the user order the tracks (ascending/descending) by: reviews_count, and the time the reviews were made. They can also search the tracks by title and owner and filter them by genre. Below the header, the tracks are listed by the time they were created by default. The create form can be used by logged in users to create a new Track instance.

- **F06 - Track Detail**  
  ![Track detail view](/documentation/readme/track_detail.png)  
  ![Track edit form](/documentation/readme/track_edit_form.png)  
  The track detail route ("/tracks/:id/") for the API renders the above content. This view renders the details of a single track, decided by the id in the url. If the user is the owner of the track, they can use the form at the bottom to change the track data or use the delete button to delete the track and all of it's associated reviews.

- **F07 - Reviews List**  
  ![Reviews list view](/documentation/readme/reviews_list.png)  
  ![Review create form](/documentation/readme/review_create_form.png)  
  The reviews list route ("/reviews/") for the API renders the above content. The filter option in the header lets the user order the reviews (ascending/descending) by score and filter the reviews by the track they are for. Below the header, the reviews are listed by the time they were created by default. The create form can be used by logged in users to create a new Review instance. Importantly, each user can only review each a track once.

- **F08 - Review Detail**  
  ![Review detail view](/documentation/readme/review_detail.png)  
  The review detail route ("/review/:id/") for the API renders the above content. This view renders the details of a single review, decided by the id in the url. If the user is the owner of the review, they can use the form at the bottom to change the review data or use the delete button to delete the review.

- **F09 - Followers List**  
  ![Followers list view](/documentation/readme/followers_list.png)  
  The followers list route ("/followers/") for the API renders the above content. The existing follower instances are listed by the time they were created at and a create form at the bottom lets the user follow other profiles. Importantly, users cannot follow themselves and they cannot follow the same user twice.

- **F10 - Follower Detail**  
  ![Follower detail view](/documentation/readme/follower_detail.png)  
  The follower detail route ("/followers/:id/") for the API renders the above content. The data of the follower instance targeted by the id in the url is displayed and a delete button is available to the owner of the instance.

### Future Implementations

The development of this API is very much driven by the needs of the Wavelength front-end. The features available right now fully meet the requirements of the project, so no major future implementations are planned/necessary for the moment. Should any changes be planned for Wavelength, this API will be updated accordingly.
If I decided to lean further into the social-media aspect of Wavelength, then I could create a new messages app which would let users message one another using the platform, however, I am happy with where Wavelength is currently.

## Technologies Used

### Languages Used

- [Python](https://www.python.org/)

### Frameworks, Libraries, and Programs Used

- [Django Rest Framework](https://www.django-rest-framework.org/) - Used as this project's main python framework.
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/installation.html) - Used for authentication.
- [django-allauth](https://allauth.org/) - Used for authentication.
- [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - Used to handle JWT tokens.
- [dj_database_url](https://pypi.org/project/dj-database-url/) - Used to connect to postgres database.
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) - Used to connect API to frontend.
- [Gunicorn](https://gunicorn.org/) - Used as the web server that allows Django to run on Heroku.
- [Cloudinary](https://cloudinary.com/) - Used to store all images uploaded to the website (e.g. cover_art + profile_images).
- [Pillow](https://pypi.org/project/Pillow/) - Used for additional image processing.
- [ElephantSQL](https://www.elephantsql.com/) - Used to create PostgreSQL database.
- [Heroku](https://www.heroku.com/) - Used to deploy and host the website.
- [diagrams.net](https://www.diagrams.net/) - Used to create ER diagrams during planning of this website.

## Deployment

To clone this repository paste `git clone https://github.com/Shabucky1812/wavelength-api.git` into the terminal of the editor you are using. Then follow the steps below to get everything up and running.

### Configuring environment variables

- Firstly, you need to install the project dependencies listed in the requirements.txt file. To do this paste `pip install -r requirements.txt` into the terminal and hit enter.
- Next, you need to create a new file at lowest level of your workspace (the same level as README.md) called **env.py**.
- IMPORTANT: the env.py file will be used to store hidden variables such as your SECRET_KEY, to prevent any security issues you must ensure that your workspace contains a **.gitignore** file and that **env.py** is listed within it. This will ensure that your env.py file is not pushed to GitHub and made publicly available.
- Within **env.py**, import the os module by adding `import os` at the top of the file.
- Now, you need to create 3 environment variables using this code format: `os.environ['variable_name'] = 'value'` for each. The 3 **variable_name**'s should be: **SECRET_KEY**, **CLOUDINARY_URL**, and finally **DEV**.
- As for the **values**, leave **CLOUDINARY_URL** blank for now. Set the **value** of the **DEV** variable to '1' and set the **SECRET_KEY** variable to any random string of characters you like, do not share this value with anyone.

### Setting up your ElephantSQL database

- Now, lets move on to setting up your PostgreSQL database.
- First, use this [link](https://www.elephantsql.com/) to reach the ElephantSQL website.
- Click on the **Log In** button to get signed in, if you already have an account then sign in as usual. If not then I recommend just using GitHub to sign in by pressing the **Sign In with GitHub** button. A window may pop-up asking for verification, if so, confirm your agreement.
- You are now at the ElephantSQL dashboard, from this screen click the **Create New Instance** button.
- In the **Name** field, enter a name for your database, this is usually the project name so I would suggest 'wavelength_api'. In the **Plan** field, select whatever plan works best for you. I used the free **Tiny Turtle** plan but if you regularly use ElephantSQL, feel free to use another.
- Ignore the **Tags** field and click on the **Select Region** button to move on.
- In the **Data center** field, choose any data center that is available and near you, it doesn't really matter which. Press **Review** to continue.
- Finally, on the review screen, ensure your details are correct and hit **Create instance**.
- You will now be returned to the dashboard. From here, click on your newly created instance to be taken to it's details screen.
- Remember the URL from the **URL** field as you will need it later when deploying to heroku.

### Connecting to Cloudinary

- The last environment variable that needs configuring is the **CLOUDINARY_URL**. We will set that up now.
- Use this [link](https://cloudinary.com/) to reach the Cloudinary website. From here you need to either log in using the **Login** button or create an account if you don't yet have one using **SIGN UP FOR FREE**.
- Once authenticated, navigate to your cloudinary dashboard under **Programmable Media > Dashboard**.
- Copy the URL within the **API Environment variable** card and use this as the value for your **CLOUDINARY_URL** variable in **env.py**. IMPORTANT: the url you copy will include 'CLOUDINARY_URL=' at the start, this is unnecessary and should be deleted. The url you are left with as your value should start with 'cloudinary://'.

### How to make and push changes

- To save all of your files and make migrations paste the command `python3 manage.py migrate` into your terminal.
- Your local workspace should now be runnable. To view a local version of the website, use the command `python3 manage.py runserver` and click **Open Browser** on the pop-up that appears.
- If you wish to make any changes to the code then you can use git to save and push those changes using the following steps:
  - Save your changes to a file using **CTRL + S**.
  - In the terminal type `git add .` to push all changes or you can use `*git add 'file_name_here'` to be more specific.
  - Commit your changes using `git commit -m "'commit_message_here'"`.
  - Finally, push your changes to your main GitHub repository using `git push`.

### Deploy with Heroku

- Lastly, follow these steps to deploy the website to Heroku.
- Use this link to log-in/sign-up to [Heroku](https://id.heroku.com/login).
- From the Heroku dashboard, select the **New** dropdown from the top-right, and then click **Create new app**.
- Enter a name into the **App name** input, select your region from the **Region** dropdown, and then click **Create app**.
- From the tabs near the top of the screen, select **Settings** and scroll down to the **Config Vars** sub-heading.
- Press **Reveal Config Vars**.
- You now need to re-create the following variables from your **env.py** file as config vars: **CLOUDINARY_URL** and **SECRET_KEY**.
- Enter these variables as keys for each config var and paste the values from your **env.py** file as the matching values.
- You will additionally need to create 5 new config vars:

  - KEY: **ALLOWED_HOST** - VALUE: **'this will be the live link of the deployed API once deployed (without the 'https://')'**
  - KEY: **CLIENT_ORIGIN** - VALUE: **'this will be the live link of the front end website'**
  - KEY: **CLIENT_ORIGIN_DEV** - VALUE: **'this will be the dev link of the front end website**
  - KEY: **DATABASE_URL** - VALUE: **''this will be the url from the ElephantSQl url field refrenced earlier**
  - KEY: **DISABLE_COLLECTSTATIC** - VALUE: **1**

- Now, scroll back up and select the **Deploy** tab.
- Under the **Deployment method** sub-heading, select **GitHub**.
- Search for the GitHub repo for your application and then click **Connect**.
- You can now deploy your application in two ways:
  - Select **Enable Automatic Deploys** to automatically deploy your program. This means that whenever a change is pushed, Heroku will automatically update your live app.
  - This project was manually deployed by selecting **Deploy Branch** under the **Manual Deploy** sub-heading. A manually deployed site will only update with new pushes when re-deployed next.
- Once Heroku has deployed your application, it will present you with a link to the live site.
- IMPORTANT: After your first deploy, Heroku may automatically add its Heroku Postgres add-on to your application. This add-on is not free and you will be charged if you leave it. To prevent this from happening after your first deploy:
  - Head over to your application's **Resources** tab.
  - Check under the **Add-ons** subheading for the Heroku Postgres add-on.
  - If the add-on is present, delete it to avoid being charged. The API will still function because of ElephantSQL.

You now have a deployed API, however it may not be much use until you clone the front end for it to interact with. To replicate full Wavelength functionality, [use this link](https://github.com/Shabucky1812/wavelength-front#deployment) to find the deployment steps for the Wavelength front end.

## Testing

Please find the testing write-up for this project in [this Testing Document](testing.md).

## Credits

### Contents

All of the code for this API was written by me, [Shaun Buck](https://github.com/Shabucky1812), although I extend my thanks to Code Institute for the drf-api walkthrough which was a great help when structuring this project.
