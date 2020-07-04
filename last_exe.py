import pickle, os, sys, logging
from httplib import HTTPConnection, socket
from smtplib import SMTP
from requests.auth import HTTPBasicAuth
import requests

def get_response_time(url):
    return requests.get(url, auth=HTTPBasicAuth('admin', 'secpasswd')).elapsed.total_seconds()

def email_alert(message, status):
    fromaddr = 'abc@mysite.com'
    toaddrs = 'xyz@mysite.com'

    server = SMTP('smtp.office365.com')
    server.starttls()
    server.login(fromaddr, 'mypasswd')
    server.sendmail(fromaddr, toaddrs, 'Subject: %s\r\n%s' % (status, message))
    server.quit()



if __name__ == '__main__':
    content = []
    with open("/home/support/url_list.txt") as f:
        content = f.readlines()
    for url in content:
        url = url.strip()
        r_time = get_response_time(url)
        print(r_time)
        if r_time > 0.5 :
        #print("Please send email", url, "as Response Time is", r_time)
         email_alert(str(r_time), url)

    status = get_site_status(url)
    if status == "down":
        #print("Send email", url, "is", status, "and Response is", get_response(url))
        email_alert(str(get_site_status(url)), url)