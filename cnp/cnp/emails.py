import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('abrarjr66@gmail.com', '')
server.sendmail('abrarjr66@gmail.com', 'ibrarkhan123589640@gmail.com', 'Test email from Python')
server.quit()
