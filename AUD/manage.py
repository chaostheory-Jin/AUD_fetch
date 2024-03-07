#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body):
    sender = 'your_email@example.com'
    receiver = 'receiver_email@example.com'
    password = 'your_password'
    smtp_server = 'smtp.example.com'
    port = 587  # SMTP端口号，根据您的邮件服务商可能不同

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    body = MIMEText(body, 'plain')
    msg.attach(body)

    # 连接到SMTP服务器并发送邮件
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # 启动TLS加密
    server.login(sender, password)
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AUD.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
