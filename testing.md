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

| Test Label | Test Action | Expected Outcome | Test Outcome |
| ---------- | ----------- | ---------------- | ------------ |

## Bugs

### Known Bugs

### Solved Bugs

Return to [README](README.md)
