# Job_App

This is a very basic app which has the following features - 

- There are 2 user modes ( Recruiter & Applicant ). Upon registering as a Recruiter, you can create,update and delete job postings made by yourself.
- The applicant can view the job postings and add them as favourites.

This app has been solely made to demonstrate CRUD functionalities and an authentication layer. Hence it does not contain all the features expected out of a similar application.

## Usage

```sh
git clone https://github.com/RitiKarayat/JApp.git
cd JApp
python3 -m venv venv
pip install -r requirements.txt
python3 app.py
```

### With Docker

```sh
docker-compose up
```

Now visit <http://127.0.0.1:5000> and the app will be running there.
