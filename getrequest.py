import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


def http_ok(site):
    output(site['http://ec2-3-19-239-145.us-east-2.compute.amazonaws.com/health.html'] + " reported OK.")
    return


def send_report():
    # Create multipart message headers
    fromaddr = "xxx@gmail.com"
    toaddr = "xxx@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "response error!"
    body = "Python test mail"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("xxxx", "pswrd")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)


def get_status_code():
    pass


def main():

        if (code == 200):
            http_ok(site)
        else:
            all_valid = False
            http_error(site, code)

    output(str(datetime.now()) + ': Checking completed.')

    # Send report when failures need reporting
    if (not all_valid):
        output('Some sites failed.')
        send_report()
    else:
        output(
            '<span style="background-color: #79b530; font-weight: bold; font-size: 16px; color: #fff;">All sites reported status code 200.</span>')

    # Log results to a file
    if (config['file']['log']):

        try:
            # Status file
            f = open(config['file']['status_file'], 'w')
            f.write(str(all_valid))
            f.close()
        except Exception:
            output("Error writing status log file!")

        try:
            # Console output file
            f = open(config['file']['output_file'], 'w')
            f.write(output_buffer)
            f.close()
        except Exception:
            output('Error writing output buffer file')


# Buffer output for e-mail
def output(string):
    global output_buffer
    output_buffer += "<br />" + string
    print
    string


# Call the main function
main()
