
  #      PassiveHunter 
  ![Passivehunter](https://github.com/devanshbatham/Passivehunter/blob/master/Images/passive.PNG)
  
 # **What is PassiveHunter ?**
 Passivehunter uses https://dns.bufferover.run for enumerating subdomains , This project  uses the `The Rapid7 [Project Sonar](https://opendata.rapid7.com/) datasets`  . dns.bufferover.run uses DNSGrep for quickly searching the the large data sets , Passivehunter enumerates the subdomains using query `https://dns.bufferover.run/dns?q=<hostname>`. It uses some regex magic to filter out the subdomains from the raw json output , then all the alive subdomains are filtered. It shows the status code of the alive subdomains. It is fast as it uses `asynchronous` requests instead of traditional `synchronous` requests.

 # **Why PassiveHunter ?** 
 I created this for my personal use , as enumerating the subdomains and filtering out the alive subdomains among hundreds of domains is a tedious task and ofcourse not a programmer way of doing things , Passivehunter automates all this , from filtering out the domains from raw json output to removing all the dead domains , It helped me a lot in finding a lot of potential hidden assets of the BB companies (And yes a lot of $$$$ bounties too) . 

# **Compatability**
It works on anything that has Python installed.

# **How to install and use ?**

` > mkdir Passive-hunter`

`> cd Passive-hunter`
`> git clone https://github.com/devanshbatham/Passivehunter`
`> sudo apt install python3.7 python3-venv python3.7-venv`
`> python3.7 -m venv py37-venv`
`> . py37-venv/bin/activate`
`> cd Passivehunter`
`> pip install -r requirements.txt` 
`> python passivehunter domainname.tld` 

# Files :

When a scan is successfully completed , **3 files** are created 
`1 - domainname.txt : contains all domains dead + alive` 
`2 - domainname-200.txt : contains domains with 200 status` 
`3 - domainname-other.txt : contains domains with status other than 200. `

# Example Usage
![Total Unique Subdomains Found](https://github.com/devanshbatham/Passivehunter/blob/master/Images/run1.PNG)
![Alive Subdomains](https://github.com/devanshbatham/Passivehunter/blob/master/Images/run2.PNG)
# Credits 
Huge shoutout to `erbbysam` <3 . 
You can read about **DNSGREP** here : https://blog.erbbysam.com/index.php/2019/02/09/dnsgrep/

#  Wanna show support for the tool ?

**I will be more than happy if you will show some love for Animals by donating to [Animal Aid Unlimited](https://animalaidunlimited.org/)** **,Animal Aid Unlimited saves animals through street animal rescue, spay/neuter and education. Their mission is dedicated to the day when all living beings are treated with compassion and love.** ✨
