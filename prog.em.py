import smtplib
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("vibhasree99@gmail.com", "password-")
message = ("hii,how are you")
s.sendmail("vibhasree99@gmail.com", "tejeswini13kolekar@gmail.com", message)
print("success")
s.quit()
