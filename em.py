Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /home/ec2017b221/prog.email.py ==================
Traceback (most recent call last):
  File "/home/ec2017b221/prog.email.py", line 12, in <module>
    s.login("sender_email_id", "sender_email_id_password")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials h127sm16072114pfc.14 - gsmtp')
>>> 
================== RESTART: /home/ec2017b221/prog.email.py ==================
Traceback (most recent call last):
  File "/home/ec2017b221/prog.email.py", line 4, in <module>
    s.login("sender_email_id", "sender_email_id_password")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials n24sm65523875pfi.175 - gsmtp')
>>> 
==================== RESTART: /home/ec2017b221/prog.em.py ====================
Traceback (most recent call last):
  File "/home/ec2017b221/prog.em.py", line 4, in <module>
    s.login("sender_email_id", "sender_email_id_password")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials m83sm61531934pfk.107 - gsmtp')
>>> 
==================== RESTART: /home/ec2017b221/prog.em.py ====================
Traceback (most recent call last):
  File "/home/ec2017b221/prog.em.py", line 2, in <module>
    s = smtplib.smtp('smtp.gmail.com', 587)
AttributeError: module 'smtplib' has no attribute 'smtp'
>>> 
==================== RESTART: /home/ec2017b221/prog.em.py ====================
Traceback (most recent call last):
  File "/home/ec2017b221/prog.em.py", line 4, in <module>
    s.login("vibhasree99@gmail.com", "ammu1324")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbux\n5.7.14 jXqmeInfK3A7kR3kO0WXBt-YlJHs-66ZrJRgrHcmemBWuvp9Rk0glmmUh_ejMm47VXSWdG\n5.7.14 yJw7wWUU0zm2g4y1RACmio9o6dLvu03QJm9qu8ieGQXqd6gA34nbwn1xrraa_TiYtMg_RA\n5.7.14 0R_IoBVRMvc0Fjzhu-Rcy_Ua3x-IZFffGo1jy5npd9tmNCdGR0Qwz2tH-l7yCuWKlheQYq\n5.7.14 gpWGeEUMLfixIbCF2MDpweQDSj7mU> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 j25sm59093650pfi.118 - gsmtp')
>>> 
==================== RESTART: /home/ec2017b221/prog.em.py ====================
Traceback (most recent call last):
  File "/home/ec2017b221/prog.em.py", line 4, in <module>
    s.login("vibhasree99@gmail.com", "ammu1324")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbu5\n5.7.14 rozJkK1rmwMGyJJzMNShfIDBkj9FOnpuRR2zWusSaqH91Cq-F7fgTCqIYLof-3JUuqKa2u\n5.7.14 AzlMzq0QbrgIhvSOo7nlV9Dkpn3xXlg_TxGq6Iat1adtTeYyWlViEEO5WK1DHR1ui__Jkq\n5.7.14 JYfi4jHYn2kUVG2maqp9tFh4QKZ-lfV9REmzxjjvaF6zXxS_505L6iN53U_ntMCfFPVXzr\n5.7.14 CuOHpTx1iVhCeDCONupjFdM2ZFcB0> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 f204sm1290765itc.40 - gsmtp')
>>> 
==================== RESTART: /home/ec2017b221/prog.em.py ====================
Traceback (most recent call last):
  File "/home/ec2017b221/prog.em.py", line 4, in <module>
    s.login("vibhasree99@gmail.com", "ammu1324")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbsT\n5.7.14 x9jGJ7e2-Iq-to9drZUPyggrXA19LTEsbgCI-1DWb6OrWhyEewtXUGX8bc0Jgx87ciThbZ\n5.7.14 uugaj1mjYa0lIXSaZZgGM9oXvAOR4-8eqMOztuDfF69gbbtW_PRl1_ffRQ1dHG1JVgyPtH\n5.7.14 ZfE7s_kK1yPMSPJRWnIT9fdCOGiV30UzIOL2OncLmF7f7fLtnJFe0UGpu2ZLTYhzYLpkV-\n5.7.14 h15411W3zwX3rGx3kaQ5vHResUANg> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 b68sm46515578pfg.18 - gsmtp')
>>> 
==================== RESTART: /home/ec2017b221/prog.em.py ====================
Traceback (most recent call last):
  File "/home/ec2017b221/prog.em.py", line 4, in <module>
    s.login("vibhasree99@gmail.com", "ammu1324")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbtN\n5.7.14 ClDCp1Uc6eXCkJaN04sUjWfmdbwVdvBe-_Nsr23e7tBwT7gWDD6T9-VNq2d5QCyCkaUMAI\n5.7.14 GmvdatAjrKB5H6l80Zx5D41eU0OHKgKNEUqdOQtON6u4srV8fdZy9Bjlwc6L_d5mkpgN3H\n5.7.14 VveGBCnCGbvioFREAbOv9plGLzGtwwQXKFB9EF016-4VchBWnoG7-gbk1i7hCnLKIp2Qpe\n5.7.14 23yM5XxWX7-aA4IM_k_7v7hnXsFVI> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 s129sm1465624ita.39 - gsmtp')
>>> 
==================== RESTART: /home/ec2017b221/prog.em.py ====================
success
>>> 
==================== RESTART: /home/ec2017b221/prog.em.py ====================
success
>>> 
==================== RESTART: /home/ec2017b221/prog.em.py ====================
success
>>> 
