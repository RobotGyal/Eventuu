# Eventuu

## A site for helping to bridge the gap between student volunteers and hackathon event cooridnators, hosts, and staff.

## Motivation
My project is a site for helping with the organization, communication, and coordination between mentors, participants, and organizers/hosts of hackathons and other related events. This was brought about by seeing the frustration event coordinators, mentors, and hosts have with running hackathons.
 
## Built with
* Python 3
* Flask
* HTML
* CSS
* Heroku

## Screenshots
![Image](../static/homepage.png)

## Features
* Adding Events (also Editing and Deleting)
* Adding time slots to Events

## Code Example
```
  <title>
        {% block title %}
        <div class="event_show_title">
        <h2><u><strong>{{ event.title }}</strong></u></h2>
        </div>
        {% endblock %}
    </title>

    <body> 
        {% block content %}
        <div class="event_show_body">
        <h4>Date: {{event.date }}</h4>
        <h4>Time : {{event.s_time }} until {{event.e_time }}</h4><hr>
        <h4>{{event.description }}</h4><br><br>

        <p><form action='/event/{{event._id}}/edit'>
            <button class='btn btn-primary' type='submit'>Edit</button>
        </form>
```

## Installation
* Clone repo to local device git clone https://github.com/RobotGyal/Eventuu.git
* Install dependencies (see requirements.txt)
* In command line run `flask run'

## Live Site
[Eventuu](https://eventuu-ak.herokuapp.com/)

## How to use?
This site id built for creating events.Time slots can also be added for the purpose of cuilding a through schedule that anyone can view.

## License
MIT © Aleia Knight