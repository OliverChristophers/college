import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os
import pandas as pd
from tqdm import tqdm

load_dotenv()

from_email = os.getenv('EMAIL_USER')
from_password = os.getenv('EMAIL_PASS')

mail_list = pd.read_csv('mail_list.csv')
mail_list['College'] = mail_list['College'].apply(lambda x: x.replace('University', '').replace('College', '') if 'of' not in x and 'the' not in x else x)
mail_list['College'] = mail_list['College'].apply(lambda x: x[:-1] if x[-1] == ' ' else x)




def send_email(subject, body, to_email):

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg['X-Priority'] = '2' 
    msg['X-MSMail-Priority'] = 'High'
    msg['Importance'] = 'High'

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(from_email, from_password)
        
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()



if __name__ == "__main__":
    subject = "SWEDISH CM | GRADUATION YEAR 2023"    
    with open('mail.txt', 'r', encoding='utf-8') as f:
        body = f.read()
    
    #send_email(subject, body, 'oliverchristophers@gmail.com')
    
    tqdm.pandas()
    #mail_list.progress_apply(lambda x: send_email(subject, body.replace('!coach_name', x['Name']).replace('!school_name', x['College'].lower()), x), axis=1)
    
