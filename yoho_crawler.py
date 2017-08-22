# https://reservation.pc.gc.ca/view.ashx?view=grid&async=true&nav=0&order=prev

import requests
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

g_cookie = "twxvyup1uparxvlir405jtd5"

def sendEmail(urls):
		content = ''
		for url in urls:
			content += url + '\n'
		msg = MIMEText(content)
		msg['Subject'] = 'Am I going to Yoho?'
		me = 'hxydiana@gmail.com'
		you = 'hxydiana@gmail.com'
		msg['From'] = me
		msg['To'] = you

		# Send the message via our own SMTP server, but don't include the
		# envelope header.
		s = smtplib.SMTP('localhost', 1025)
		s.sendmail(me, [you], msg.as_string())
		s.quit()

def main():
	headers = {'Cookie': 'ASP.NET_SessionId='+g_cookie+'; CookieLocaleName=en-CA; testcookie=cookie'}
	urls_to_send = []
	for i in range(0, 4):
		url = 'https://reservation.pc.gc.ca/view.ashx?view=grid&async=true&nav='+str(i)+'0&order=prev'
		raw_response = requests.get(url, headers=headers)
		# print raw_response.text
		occurence_forward = raw_response.text.find('https://reservation.pc.gc.ca/Images/available_icon20x20.png')
		occurence_reverse = raw_response.text.rfind('https://reservation.pc.gc.ca/Images/available_icon20x20.png')
		found_availability = occurence_forward != occurence_reverse
		if found_availability == False:
			urls_to_send += [url]
			print "Hooray!"
		else:
			print "Meh"

	if len(urls_to_send):
		sendEmail(urls_to_send)


if __name__ == "__main__": main()