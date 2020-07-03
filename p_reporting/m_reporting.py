import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import os

import matplotlib.pyplot as plt


def generate_csv(grouped_df, output):
    print('generating csv...')
    grouped_df.to_csv(output, header=False, index=False)

def plot_returns(grouped):
    plt.style.use('ggplot')
    chart = grouped['Lifestyle'].value_counts().plot(kind='bar', color='#6c3376')
    plt.title('Lifestyle Groupped')
    plt.xlabel('Lifestyle')
    plt.xticks(rotation=0)
    plt.savefig('urban_rural.png')
    return chart


def send_email(to_addr, file_path, from_email='adjitta94@gmail.com'):
    subject = 'Project Module 1'
    body = """
     <html>
    <head></head>
    <body>
    <h3>Project Module 1</h3>
    <p>A quien corresponda,</p>
    <p> </p>
    <p> </p>
    <li>  </li>
    <li> </li>
    <p> </p>
    <p> </p>
    <p><i> </i></p></p>
    </body>
    </html>
    """
    if not os.path.exists(file_path):
        return "file no exist"

    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_addr
    print(message)
    message['Subject'] = subject
    message.attach(MIMEText(body, 'html'))
    print(message)

    file = open(file_path, 'rb')

    files_MIME = MIMEBase('application', 'octet-stream')
    files_MIME.set_payload(file.read())
    encoders.encode_base64(files_MIME)
    files_MIME.add_header('Content-Disposition', f'attachment; filename= {file_path}')
    message.attach(files_MIME)

    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    sesion_smtp.starttls()
    sesion_smtp.login('adjitta94@gmail.com', 'pindodisanta1994')
    text = message.as_string()
    sesion_smtp.sendmail(from_email, to_addr, text)
    sesion_smtp.quit()


def report(grouped_df, output, grouped, to_addr, file_path):
    generate_csv(grouped_df, output)
    bar_plot = plot_returns(grouped)
    send_csv = send_email(to_addr, file_path, from_email='adjitta94@gmail.com')
    return bar_plot
