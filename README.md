# Warbler - A Microblogging Application

Warbler is a microblogging web application that allows users to post short messages, follow other users, and engage in discussions.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **User Registration and Authentication:** Users can create accounts, log in, and log out securely.
- **Posting Messages:** Users can post short messages (warbles) with text and images.
- **Following Other Users:** Users can follow and unfollow other users to see their warbles in their feed.
- **User Profiles:** Each user has a profile page displaying their warbles, followers, and following.
- **Likes and Replies:** Users can like and reply to warbles, fostering engagement.
- **User Feed:** The home feed displays warbles from users the logged-in user follows.
- **Search Functionality:** Users can search for other users or warbles by username or content.
- **Edit and Delete Warbles:** Users can edit and delete their own warbles.
- **Notifications:** Users receive notifications for new followers, likes, and replies.

## Installation

1. **Clone the repository to your local machine:**

   git clone https://github.com/your-username/warbler.git
   cd warbler
   
Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate

Install the required dependencies:
pip install -r requirements.txt

Set up the database:
createdb warbler
python seed.py

Start the Flask development server:
export FLASK_ENV=development
flask run

Access the application in your web browser at http://localhost:5000.

Usage
Register for a new account or log in with an existing one.

Create a new account with a unique username and password.
Log in using your registered username and password.
Create warbles, follow other users, and engage in discussions.

Post your own warbles with text and images.
Explore other users' profiles and follow them to see their warbles in your feed.
Like and reply to warbles to interact with other users.
Explore user profiles, like and reply to warbles, and customize your feed.

Visit user profiles to see their warbles, followers, and who they are following.
Engage with other users' warbles by liking and replying to them.
Customize your home feed by following and unfollowing users.
