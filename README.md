
# Nearby Restaurants Django Web App using Google Places API

The "Nearby Restaurants Django Web App using Google Places API" is a web application built on the Django framework that leverages the Google Places API to help users find nearby restaurants.

## Getting Started

These instructions will help you set up and deploy the project on your local machine for development and testing purposes.

### Prerequisites: 
#### Enabling Google Places API and JavaScript Maps API
To use the Google Places API and JavaScript Maps API in your project, you need to enable these APIs through the Google Cloud Console and obtain API keys. Follow these steps:

##### Enabling Google Places API
Go to the Google Cloud Console: 

Visit the Google Cloud Console(https://console.cloud.google.com/) .

##### Create or Select a Project:

If you haven't already created a project, click on the project selector at the top of the page and create a new project. Otherwise, select an existing project from the list.

###### Enable the Google Places API and JavaScript Maps API:
In the Cloud Console, click on the navigation menu (☰) on the top left.
Navigate to "APIs & Services" > "Library."
In the "API Library" page, search for "Google Places API" and select it.
Click the "Enable" button.
And also search for "Maps JavaScript API" and select it.
Click the "Enable" button.
Create Credentials:

After enabling the API, go back to the navigation menu and navigate to "APIs & Services" > "Credentials."
Click the "Create Credentials" dropdown and select "API Key."
Your API key is now generated.


### Installing

1. Clone the repository to your local machine:  First, clone the app's repository from GitHub to your local machine. You can use git for this:

   ```bash
   git clone https://github.com/shamimkhaled/nearby-restaurants.git
   
   ```
#### 2. Set Up a Virtual Environment:
 Open the cloned project in Visual Studio Code (VS Code). In the VS Code terminal (either Command Prompt or Git Bash), create a virtual environment inside the project root folder:
```bash
  python -m venv env
```
#### Activate the virtual environment:

#### In Command Prompt terminal:
```bash
  .\env\Scripts\activate
```

#### or

#### In Git Bash terminal (replace the path with your virtual environment path):
```bash
source "C:\Users\shamim\Desktop\nearby\env\Scripts\activate"
```

3. #### 3.  Navigate to the Project Directory:
If you're not already in the project root directory, navigate to the Django project directory named "nearby-restaurants":

```bash
  cd nearby-restaurants
```

#### 4. Google API Key:  In the settings.py file add your Google Places API key
```bash
API_KEY=YOUR_API_KEY
```
And also replace your api in index.html in templates folder.
```bash
<!-- Include Google Maps JavaScript API with your API key -->
    <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places&callback=initMap"></script>
```
Replace YOUR_API_KEY with your actual Google Places API key.

#### 5.  Install Project Dependencies:
Install all project dependencies by running the following command:

```bash
  pip install -r requirements.txt
```

#### 6. Database Migration:
Migrate the database to create necessary tables:

```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```

#### 7. Create a Superuser:
Create a superuser account to access the admin panel of the project:

```bash
  python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password for the superuser.

#### 8. Run the Project:
Start the Django development server:

```bash
  python manage.py runserver
```

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |


## Authors

- [@shamimkhaled](https://www.github.com/shamimkhaled)

