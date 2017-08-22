# https://reservation.pc.gc.ca/view.ashx?view=grid&async=true&nav=0&order=prev

import requests
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

g_cookie = "twxvyup1uparxvlir405jtd5"
g_account = 'kevenbot3@gmail.com'
g_pw = '4%x4fI927vdw'

def sendEmail(urls):
	content = ''
	subject = ''
	if len(urls):
		for url in urls:
			content += url + '\n'
		subject = 'Am I going to Yoho?'
	else:
		subject = 'Check your yoho crawler'
		content = 'Uh oh something went wrong'

	msg = MIMEText(content)
	msg['Subject'] = subject
	me = g_account
	you = 'hxydiana@gmail.com'
	msg['From'] = me
	msg['To'] = you

	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	try:  
		server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server_ssl.ehlo()
		server_ssl.login(g_account, g_pw)
		server_ssl.sendmail(me, [you], msg.as_string())
		server_ssl.quit()
	except:  
		print 'Something went wrong...'


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

		found_unavailability = raw_response.text.find('https://reservation.pc.gc.ca/Images/unavailable_icon20x20.png')
		found_unavailability_r = raw_response.text.find('https://reservation.pc.gc.ca/Images/unavailable_icon20x20.png')
		health_check = found_unavailability != found_unavailability_r

		if found_availability == True:
			urls_to_send += [url]
			print "Hooray!"
		else:
			print "Meh"

	if len(urls_to_send):
		sendEmail(urls_to_send)
	elif health_check == False:
		sendEmail(None)


if __name__ == "__main__": main()