This is a python django full-stack project of a feature/issue tracker called Unicorn Attractor. The Unicorn Attractor web site presents users with options to input and track issues and features of a project and the ability to vote and pay for features or issues that they see as important.

The UX Design:

The motivation of the user to use the product is to keep track of issues and features of a project. The functionality of the product includes a user being able to register and log in to view and track issues and features of a project and the ability to vote and pay for features that they see as important. The user should also be able to view a visualisation of statistics on current issues in the project. To achieve this goal, the UX design emcompasses  the entire user journey, across the requirements of the application, using wireframes to illustrate the design decisions. The design across all of the web site should be user-centered, and focus on the user nad provide ease of use of the website - creating a positive user experience without features that necessarily surprise the user negatively. Information should be displayed in an organised manner and the web site and it's layout should be intuitive and provide a solution to the users' demands.

The wireframes are illustrated in the ui folder and are designed using an application called Pencil.

The front page (wireframe home.png in ui  folder) is the first presentation to hte user of the web site, as the home page. The home page should provide a warm, friendly feeling to the user and invite the user into the website to explore further. To achieve this end, a non-intrusive background image is presented and persisted across the visit to the website. The appealing font Courgette provided by google is also used consistently across the site. The background colors are light colours, mostly white, and a color scheme for the nav bar are allocated according to these colors. The aim for this website was to a simple colour scheme, to keep it warm and friendly and non-intrusive to the eye. The navigation bar is coloured in white with black text, which is a scheme adopted throughout the rest of the website too. The navigation bar invites the user, at this point on the user journey, to either log in or register which is illustrated on the navigation bar below the title, Unicorn Attractor. The navigation bar also adapts to a mobile navigation bar depending on the user's device.

The login page (login.png in the ui folder) is a simple page using the existing colour scheme that presents a username and password prompt and a login button to validate and submit. If there are validation errors they are displayed before the user continues

The register page (register.png in the ui folder) is a simple page using the existing colour scheme that asks the user with an email address, username and password / password confirmation. The Register button checks and validates the form and only proceeds if the validation is successful. Error messages are displayed if unsuccessful.

The accounts info page (account-info.png in ui folder) is the portal site for a user logging in and is designed to be as user-centered and user-friendly as possible. To achieve this end, the account information is grouped together like the username, email address, and number of tickets. The main presentation of this page is the bug and features list that the user has already submitted to the site, and this information is presented in an organised manner. Each feature or bug is given a particular 'card' or 'box' around which it presents the visual and textual information of what it is, at a glance. The View buttun underneath the feature or bug, invites the user to investigate that feature or bug further and redirects to that particular bug or feature that illustrates more information about it. This presentation expands and shrinks according to the user's screen and this allows easy navigation and presentation to users with smaller screens on mobile devices.

The create ticket page (createticket.png in ui folder) is the way in which a user can create a new ticket and allows a user to insert a bug or feature, once he or she is logged in. This option becomes available in the navigation bar once the user is logged in. The page presents forms to the user, to prompt for the relevant information to create a ticket. The forms are then validated before the user can proceed, ensuring the user has not added erroneous, incorrect or malicious data in.

The bugs/features pages (bugs.png/features.png in ui folder) present the bugs/features to the user. Each page presents text boxes or 'cards' around each bug or feature with information about each, so the user can tell at a glance what they are about. The user can view more information about the bug or feature by clicking the view button or edit the information clicking the edit button. The user can also upvote a bug or feature using the vote button. If the item is a feature, then the user must pay 50 euro to proceed to upvote that item.

The graphs page (graphs.png in the ui folder) is the graph page that allows a user to view the statistics of the bug/features in a visual format. There are five types of statistics. The first two graphs include a bar chart and pie chart of progress statistics of all tickets. The third statistic shows the daily stats. The fourth statistics shows the weekly stats. The fifth statistics shows the monthly stats

TESTING:

Testing - Test Plan: The test plan is to cover as much of the code as possible, both in the backend and the frontend of the unicorn issue tracker application. The items to be tested are the models, views and controllers.

Testing - Test Implementation: The test implementation is implemented according to the code-institute code testing tutorials - in an automated way. In implementation of the automated testing covers as much as possible of the code that can be automated. The automated testing is implemented in django's 'unittest' framework, which is part of django. The output of the automated testing, after being run, should be success or failure.

Testing - automated testing. To run use the command line: python manage.py test

The output results after running this should be similar to below:...

Ran 28 tests in 1.25s

OK




INSTALLATION AND DEPLOYMENT
To install:

Install Django
Install SQLAlchemy library
run python manage.py runserver to run the application


To deploy on heroku:

Create a new project on heroku and give it a unique name - in this case unicornproj was used.
Under deploy settings link the heroku application to github and choose the master branch to deploy.
Enable Manual Deployment
The requirements.txt lists the dependancies and takes care they are installed on heroku
The proc file should take care of the installers and running the executable file 'manage.py'
Heroku Deployment: https://unicornproj.herokuapp.com/

