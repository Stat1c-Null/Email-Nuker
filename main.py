import smtplib
import argparse
import random
letters = "wertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

def sendEmail(sender, password, receiver, times):
  subject_list = ["SPECIAL PROMOTION", "YOU WON THE LOTTER", "HAVE YOU HEARD ABOUT THIS?"]
  msg_list = ["You should check this out!", "wow this is incredible", "please work", "wake up Neo"]
  try:
    for x in range(1, times):
      #UNCOMMENT IF YOU DONT WANNA USE RANDOM SUBJECTS
      #subject = random.choice(subject_list)#Randomly choose subject
      #COMMENT THIS OUT IF YOU DONT WANT RANDOM SUBJECTS
      subject = ""
      for z in range(7):
        subject += random.choice(letters)
        
      msg = random.choice(msg_list)#Randomly choose message body
      header = 'From :{}\n'.format(sender)
      header += 'To :{}\n'.format(receiver)
      header += 'Subject :{}\n'.format(subject)
      message = header + msg
      server = smtplib.SMTP(host='smtp.gmail.com', port=587)#Use gmail to send mails
      server.starttls()
      server.login(sender, password)#Login to gmail account
      server.sendmail(from_addr=sender, to_addrs=receiver, msg=message)
      server.quit()
      print('{} Emails sent'.format(x))
  except:
    print("Failed to send email!")
      
def main():
  #Email Template set up
  template = argparse.ArgumentParser(description = "Email Nuker")
  template.add_argument("-f", "--sender", type=str, help="Email address from which mails will be sent. Has to be gmail")
  template.add_argument("-p", "--passwd", type=str, help="App Password from Email")
  template.add_argument("-t", "--to", type=str, help="Target email to nuke")
  template.add_argument("-s", "--subject", type=str, help="Subject of the email")
  template.add_argument("-m", "--message", type=str, help="Message body")
  template.add_argument("-n", "--times", type=int, help="Number of times to send")
  args = template.parse_args()
  #Set arguments and specify data
  args.sender = "slabysh2015@gmail.com"
  args.passwd = "wnyketrjiuzpxmjr"
  args.to = "undonecayon@gmail.com"
  #Send the email
  if not args.sender or not args.passwd or not args.to:
    print("Fields not specified")
    exit()
  else:
    #Default data
    times = 100 #Number of times to send
    #Use default data in case user didnt specify this fields
    if args.times:
      times = args.times
    sendEmail(args.sender, args.passwd, args.to, times)

if __name__ == "__main__":
  main()
    
  