Hello, friend of Progi Pix!

This is my project on the exercise of ProgiPix and then I will tell you about this adventure.

Before you run the project I want to tell you a few things.

- The test can be understood in many ways. There is no mention of the scope that it can have. However, I am very confident in the project that I built thinking about the details.

- Borrow multimedia content from its official page to give a harmony and more pleasant environment to the project.

- I'm excited for you to run the project and see my great work. With nothing more to say, you can continue :)

The project has 2 main applications. Administrator and bidding.

In the administrator application is the logic by a hypothetical admin user

In the bidding application there is the logic of the bidding calculations of a normal user.

The logic of the applications is in the "views.py" files corresponding to each one, in which what each function and class does is documented in detail.

In what language is this project developed?
Answer: I developed this project in Django/Python. Backend and Frontend are not separated. By the way, the Frontend is magical thanks to Bootstrap 5
Django version: 4.0.5
Python: 3.9.7

How do I run the project?
Answer: It is very easy.

1. You must download the repository, there you will find two main folders; a folder for the environment and another folder for the rest of the project itself.
2.You must activate the virtual environment in the path /env/scripts. There you must run the "activate" command if you are on windows or "source activate" if you are on linux.
3. You must go to the /Progipix path. There run the following command "python manage.py runserver"
4. Done. That easy!. Just open localhost:8000

Does this project have a database?
Answer: Yes, this project has a relational database in SQLLITE3, I store the project data there. I used this database, since it doesn't need a single service to run it.

Is there a diagram of the database?
Answer: Yes, at the root of this project you will find an image so you can see how the tables are related graphically and very simply.

How are the tables related?
Answer: There is a main table (Biddingvariable), which is related by foreign keys to the tables (biddingcalculation) (basicusagerate) (partneshipcostrange), the last relationship being many to many. All data types are decimal where you are talking about numbers.

How do you query the tables?
Answer: I used the Django ORM to do the queries.

I would like to receive feedback on this project independent of the decision made. I like to learn from my mistakes and improve.

Thanks for taking the time to read.

This work was designed, built and tested by Santiago Corrales Londoño; with brain and love.