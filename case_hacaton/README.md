# Mobile App for a Dog Shelter

This is a mobile app (will be in the future) for a dog shelter. On it, you can take a dog for a walk, take a dog for foster care (take a dog for guardianship), and adopt a dog.

## Description of the Visual Part

### Panels on the Site
- Login panel with different rights
- Admin panel
- User panel

### Login Panel
- Shelter name
- User login button
- Admin login button

### Admin Panel
- Shelter name
- Counter of donated money for food
- Counter of donated money for medicine
- Window for adding a dog from the list
  - Field for entering the dog's name
  - Field for entering the dog's age
  - Field for entering the dog's description
  - Field for entering the URL link to the dog's photo (not implemented)
  - Button for adding a dog to the list
- Window for removing a dog from the list
  - Field for entering the dog's name
  - Button for removing a dog from the list
- "Back" button

### User Panel
- Shelter name
- Button for opening the list of dogs
  - List of dogs
- "Walk a Dog" button
  - Field for entering the name of the dog you want to walk
  - List of dog names that can be walked
  - "Submit a Walk Request" button
- "Donate Food" button
  - Counter of donated money for food
  - Field for entering the amount of money to donate
  - "Donate Food" button
- "Donate Medicine" button
  - Counter of donated money for medicine
  - Field for entering the amount of money to donate
  - "Donate Medicine" button
- "Become a Foster Parent" button
  - Field for entering the name of the dog you want to foster
  - List of dog names that can be fostered
  - "Submit a Foster Request" button
- "Adopt a Foster Dog" button
  - Field for entering the name of the dog you want to walk
  - List of dog names that can be walked
  - "Submit an Adoption Request" button
- "Return a Dog" button
  - "Return a Dog from a Walk" button
    - Field for entering the name of the dog you want to return from a walk
    - "Submit a Request to Return a Dog" button
  - "Return a Dog from Foster Care" button
    - Field for entering the name of the dog you want to return after fostering
    - "Submit a Request to Return a Dog" button
- "Back" button

## Description of the Software Part

### Libraries
- Flet
- SQLite3
- sys

### Classes
- Dog
- User
- Admin
- Glav_page
