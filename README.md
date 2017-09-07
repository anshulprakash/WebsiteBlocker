# WebsiteBlocker
It is a URL blocker, which, within specified hours of the day, blocks access to specified websites and infact redirects you to a motivational website, useful for the ones who get distracted at work. Utilized host files to achieve the purpose. Works seamlessly on all operating systems including windows, Linux and Mac.

<u><b>Platform specific details:</b></u>
<b>In windows:</b>
  <ul><li>
  Use Task Scheduler to convert the program into a process and run at startup, running with highest privledges
  </li></ul>
<b>In Unix based systems:</b>
  <ul><li>
  Hostfile Path: /etc/hosts</li>
  <li>run sudo crontab -e</li>
  <li>then add the line: @reboot python3 <.py filepath></li>
