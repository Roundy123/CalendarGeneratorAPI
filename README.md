# CalendarGeneratorAPI

## Overview

An API to create a calendar with half hour intervals between a given time frame as shown in the image below.

![Image of DataFrame](http://renewable.exchange/backend/calendar_dataframe.png)

The API accpets a start date, end date, creates a pandas dataframe then converts this to a JSON file as a response.

## Installation

Requires [Docker](https://www.docker.com/) to be installed. Clone the repository then build an image and run it:

```
sudo docker build -t myimage .
sudo docker run -d --name mycontainer -p 80:80 myimage 
```

You should be able to check it in your Docker container's URL, for example: http://192.168.99.100/calendar?start_date=20200101&end_date=20200120 or http://127.0.0.1/calendar?start_date=20200101&end_date=20200120 (or equivalent, using your Docker host).
