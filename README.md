# Wavelength API

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

### Frameworks, Libraries, and Programs Used

- [diagrams.net](https://www.diagrams.net/) - Used to create ER diagrams during planning of this website.

## Deployment

## Testing

Please find the testing write-up for this project in [this Testing Document](testing.md).

## Credits

### Contents

### Acknowledgements
