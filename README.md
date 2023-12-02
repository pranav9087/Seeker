# Introduction

## What is Seeker?

This web app is for students, especially incoming ones, who have trouble seeking the right club of their interests and friends who share similar interests, Seeker is a website that integrates both functionalities, which helps them quickly find friends and clubs that match their interests.

Functionalities:
1. Users can view a list of clubs that match their input interest tags. 
2. Users can view a list of other users based on the interest tags. 
3. Users can create an account. 
4. Users can join clubs directly from the platform. 
5. Users can update their profile and interest tags.

For more details, view the full project proposal [here](https://docs.google.com/document/d/1HntOp2URS7A_DO_r31DlWtkkvD0WplxUDnhFP6Zu5xg/edit?usp=sharing).

# Technical Architecture
[
![technical architecture](https://github.com/CS222-UIUC-FA23/group-project-team38/assets/87254803/232e15b4-8d7c-4e3b-843d-b491b4c30eda)
](url)

# Developers

- **Peize Li**: Managing database and Worked on backend API creation, interaction and a few SQL scripts
- **Pranav Penmatcha**: Worked on most frontend web pages
- **Pranash Krishnan**: Assisted on both backend API and frontend and mostly Worked on writing SQL scripts and populating the database 
- **Naman Goyal**: Assisted on backend and mostly Worked on writing SQL scripts and populating the database


# Development

## Package Management

To install packages for backend, run the following:

```
pip install -r requirements.txt
```

To install packages for frontend, run the following:

```
cd frontend
npm install
```

# Project Instructions

1. To run backend:
```
cd backend
python -m flask run
```
or sometimes 

```
python3 -m flask run
```
Database will be automatically generated in the backend/instance

2. To run frontend:
```
cd frontend
npm start
```

3. To view database :

You can use any preferred DB explorer or you can install SQLite, which is a recommended explorer in extensions of VSCode
