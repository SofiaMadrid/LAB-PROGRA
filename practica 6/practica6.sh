IP_publica=$(curl ifconfig.me)
nmap scanme.nmap.org   
nmap --script Discovery $IP_publica

