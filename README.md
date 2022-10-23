# Django Email Scraper

This is simple Email Scraper is built using Django with help of *request* library. 

## Installation
Python, Django and request need to be installed

```bash
pip install django request
```

## Usage

Go to the django_email_scraper folder and run

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**

## How to use django email scraper
1. Enter any number of URLs in textbox.
2. Click **Extract Email** button.
3. All URLs will be processed one by one and if there is emails found, then it will displayed.
4. Copy extracted emails.

![index-page](https://user-images.githubusercontent.com/20318536/197402797-6ba48ec2-6202-4836-b446-6621e18f6d58.jpg)

## Future scope
1. It only check given URL for email. The script can be modifed to navigate about-us, contact-us page if email is not found on given url.
2. Email scraping order is not sequential. Some website appears first if they processed page before.
