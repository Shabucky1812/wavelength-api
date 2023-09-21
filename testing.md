# Star Seekers Testing

## Automated Testing

### Python validation

All of the custom python written for this API passes through [this PEP8 linter](https://pep8ci.herokuapp.com/) without raising any errors.

#### Wavelength app

##### permissions.py

![PEP8 linter results for wavelength permissions](/documentation/testing/wavelength_permissions.png)

##### serializers.py

![PEP8 linter results for wavelength serializers](/documentation/testing/wavelength_serializers.png)

##### urls.py

![PEP8 linter results for wavelength urls](/documentation/testing/wavelength_urls.png)

##### views.py

![PEP8 linter results for wavelength views](/documentation/testing/wavelength_views.png)

#### Followers app

##### models.py

![PEP8 linter results for followers models](/documentation/testing/followers_models.png)

##### serializers.py

![PEP8 linter results for followers serializers](/documentation/testing/followers_serializers.png)

##### urls.py

![PEP8 linter results for followers urls](/documentation/testing/followers_urls.png)

##### views.py

![PEP8 linter results for followers views](/documentation/testing/followers_views.png)

#### Profiles app

##### models.py

![PEP8 linter results for profiles models](/documentation/testing/profiles_models.png)

##### serializers.py

![PEP8 linter results for profiles serializers](/documentation/testing/profiles_serializers.png)

##### urls.py

![PEP8 linter results for profiles urls](/documentation/testing/profiles_urls.png)

##### views.py

![PEP8 linter results for profiles views](/documentation/testing/profiles_views.png)

#### Reviews app

##### models.py

![PEP8 linter results for reviews models](/documentation/testing/reviews_models.png)

##### serializers.py

![PEP8 linter results for reviews serializers](/documentation/testing/reviews_serializers.png)

##### urls.py

![PEP8 linter results for reviews urls](/documentation/testing/reviews_urls.png)

##### views.py

![PEP8 linter results for reviews views](/documentation/testing/reviews_views.png)

#### Tracks app

##### models.py

![PEP8 linter results for tracks models](/documentation/testing/tracks_models.png)

##### serializers.py

![PEP8 linter results for tracks serializers](/documentation/testing/tracks_serializers.png)

##### urls.py

![PEP8 linter results for tracks urls](/documentation/testing/tracks_urls.png)

##### views.py

![PEP8 linter results for tracks views](/documentation/testing/tracks_views.png)

## Manual Testing

### User Stories

To show how the features of this api meet the requirements of the user stories, I have created this chart that demonstrates which features are relevant to each user story:

| User Story                      | Achieved | Relevant Features                            |
| ------------------------------- | -------- | -------------------------------------------- |
| US01 - Create Profile           | YES      | F02 - Log in + out (\*additional note below) |
| US02 - Edit Profile             | YES      | F04 - Profile Detail                         |
| US03 - Delete Profile           | NO       | (\*\*read more about below)                  |
| US04 - View Profiles            | YES      | F03 - Profiles List, F04 - Profile Detail    |
| US05 - Follow Users             | YES      | F09 - Followers List, F10 - Follower Detail  |
| US06 - Unfollow Users           | YES      | F09 - Followers List, F10 - Follower Detail  |
| US07 - Share Tracks             | YES      | F05 - Tracks List                            |
| US08 - Edit Track               | YES      | F06 - Track Detail                           |
| US09 - Delete Track             | YES      | F06 - Track Detail                           |
| US10 - View Tracks (list view)  | YES      | F05 - Tracks List                            |
| US11 - View Track (detail view) | YES      | F06 - Track Detail                           |
| US12 - Create Review            | YES      | F07 - Reviews List                           |
| US13 - Edit Review              | YES      | F08 - Review Detail                          |
| US14 - Delete Review            | YES      | F08 - Review Detail                          |
| US15 - View Reviews             | YES      | F07 - Reviews List, F08 - Review Detail      |

\* currently, for the backend, new users can only be created by creating a new superuser from the workspace terminal. This is fine for the backend, however users CAN create new accounts from the front end (which you can read more about from the frontend repo's README).

\*\* I ultimately decided not to include profile deletion in this version of the project. It's not a necessary or major feature and I wanted to spend more time on the more important features (tracks/reviews). If the site was to develop popularity, then I would consider adding this feature.

### Functionality

| Test Label                    | Test Action                                                     | Expected Outcome                                | Test Outcome |
| ----------------------------- | --------------------------------------------------------------- | ----------------------------------------------- | ------------ |
| URLs render correct views     | Manually visit every URL                                        | All URLs should render the correct views        | PASS         |
| Profile list filtering        | Attempt to use all Profile filter options                       | The profile list should be rendered accordingly | PASS         |
| Conditional profile edit form | View a profile detail page whilst logged in as a different user | The edit form should not render                 | PASS         |
| Profile edit works correctly  | Edit a profile using the form                                   | The changes should be saved                     | PASS         |
| Create follow works correctly | Try to follow a user                                            | New follower instance should be created         | PASS         |
| Follower duplicates prevented | Attempt to follow a user already followed                       | The API should raise an Integrity Error         | PASS         |
| Follower delete works         | Delete a follower instance                                      | The instance should be deleted                  | PASS         |
| Track list filtering          | Attempt to use all Track filter options                         | The track list should be rendered accordingly   | PASS         |
| Create track works correctly  | Attempt to share a track with valid data                        | The track should be created                     | PASS         |
| Cover art validation          | Try to create a track with a large image                        | The API shouldn't accept the image              | PASS         |
| Conditional track edit form   | View a track detail page whilst logged in as a different user   | The edit form should not render                 | PASS         |
| Track edit form works         | Edit a track using the form                                     | The changes should be saved                     | PASS         |
| Track delete works            | Delete a track                                                  | The track instance should be deleted            | PASS         |
| Review list filtering         | Attempt to use all Review filter options                        | The review list should be rendered accordingly  | PASS         |
| Create review works correctly | Attempt to create a review with valid data                      | The review should be created                    | PASS         |
| Review duplicates prevented   | Attempt to create a duplicate review                            | The API should prevent the review creation      | PASS         |
| Conditional review edit form  | View a review detail page whilst logged in as a different user  | The edit form should not render                 | PASS         |
| Review edit form works        | Edit a review using the form                                    | The changes should be saved                     | PASS         |
| Review delete works           | Delete a review                                                 | The review instance should be deleted           | PASS         |
| Log in/out                    | Attempt to log in and out                                       | Should work as expected                         | PASS         |

## Bugs

### Known Bugs

As far as I can tell from my testing, this API currently suffers from no bugs.

### Solved Bugs

- When the reviews app was first created, I had a small issue preventing users from creating multiple reviews for the same track. I fixed this by adding the 'unique_together' field to the reviews model Meta class and checking for an integrity error before saving the review instance.
- When the genre field was first created, I had an issue with the genre displaying as an integer value because I used an integer field with a 'choices' field to determine the genre options. I fixed this by splitting the genre field into two (genre_id, genre) and using the serializer to set the new 'genre' field to the display value of the 'genre_id' field.

Return to [README](README.md)
