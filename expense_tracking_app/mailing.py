import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendmailto(email, html_content,subject):
        message = MIMEMultipart("alternative")
        message["Subject"] = f"{subject}"
        print("============================================")
        print(os.getenv('dev_email'))
        print("============================================")

        message["From"] = os.getenv('dev_email')

        message["To"] = email
        part = MIMEText(html_content, "html")
        message.attach(part)
        with smtplib.SMTP_SSL("smtp.gmail.com") as server:
            server.login(os.getenv('dev_email') , os.getenv('pass_key'))
            server.sendmail(os.getenv('dev_email'),
                            email, message.as_string())
            server.quit()

def deliver_password_reset(subject,name,email,username,password):
    html_content = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                </head>

                <body style="font-family: 'Times New Roman', Times, serif;">
                <table cellpadding="0" cellspacing="0" border="0" align="center" style="background-color: rgb(217, 216, 216); margin: 4% 10%; border-bottom: outset 6px rgb(255, 166, 0); border-radius: 0 30px;">
                    <tr>
                        <td>
                            <div style="color: rgb(1, 101, 189); background-color: rgb(255, 166, 0); padding: 1px 20px; border-bottom: inset 5px rgb(7, 111, 163); border-top-right-radius: 30px;">
                                        <h2 >{subject}</h2>
                            </div>
                            <div style="padding: 5%;">
                                        <p>Dear {name}, <br> your account has been reset. Please use the below credentials to access your account and update your password.</p>
                               <ul>
                                            <li>Username: {username}</li>
                                            <li>Password: {password}</li>
                                        </ul>
                                <a title="Login" href="https://yosefe.pythonanywhere.com/login" style="text-decoration: none; background-color: rgb(0, 136, 215); color: rgb(255, 255, 255); font-size: larger; margin: 5%; padding: 0.5% 3%;">Login</a>
                            </div>
                            <hr>
                            <h5 style="padding-left: 10px; width: 90%; text-align: center; font-style: italic; color: rgb(70, 80, 80);">From <i>Rumi Press's Book Distribution Expense Management Tool</i></h5>
                        </td>
                    </tr>
                </table>
                </body>
                </html>
                """
    sendmailto(email, html_content,subject)