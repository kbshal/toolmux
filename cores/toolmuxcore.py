# module for toolmux
# hardworking 
# help people 
import os
import sys
import time

toolmux_banner = """
 @@@@@@@@@@@  @         @       @  @     @
     @        @         @ @   @ @    @  @
     @        @         @   @   @      @
     @        @         @       @     @  @
     @        @         @       @    @     @
     @        @@@@@@@@  @       @   @        @






          
"""
backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the toolmux
"""
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print backtomenu_banner
	backtomenu = raw_input(" ")
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print "ERROR: Wrong data"
		time.sleep(2)
		restart_program()

def banner():
	print toolmux_banner

def nmap():
	print '>>>> Installing Nmap'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap')
	print '>>>> Done'
	print ">>>>Type 'nmap' to use."
	backtomenu_option()

def red_hawk():
	print '>>>> Installing RED HAWK'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	os.system('mv RED_HAWK ~')
	print '>>>> Done'
	backtomenu_option()

def dtect():
	print '>>>> Installing D-Tect'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/bibortone/D-Tech')
	os.system('mv D-TECT ~')
	print '>>>> Done'
	backtomenu_option()

def sqlmap():
	print '>>>> Installing sqlmap'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	os.system('mv sqlmap ~')
	print '>>>> Done'
	backtomenu_option()

def infoga():
	print '>>>> Installing Infoga'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests urllib3 urlparse')
	os.system('git clone https://github.com/m4ll0k/Infoga')
	os.system('mv Infoga ~')
	print '>>>> Done'
	backtomenu_option()

def reconDog():
	print '>>>> Installing ReconDog'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/UltimateHackers/ReconDog')
	os.system('mv ReconDog ~')
	print '>>>> Done'
	backtomenu_option()

def androZenmap():
	print '>>>> Installing AndroZenmap'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap curl')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh')
	os.system('mkdir ~/AndroZenmap')
	os.system('mv androzenmap.sh ~/AndroZenmap')
	print '>>>> Done'
	backtomenu_option()

def sqlmate():
	print '>>>> Installing sqlmate'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install mechanize bs4 HTMLparser argparse requests urlparse2')
	os.system('git clone https://github.com/UltimateHackers/sqlmate')
	os.system('mv sqlmate ~')
	print '>>>> Done'
	backtomenu_option()

def astraNmap():
	print '>>>> Installing AstraNmap'
	os.system('apt update && apt upgrade')
	os.system('apt install git nmap')
	os.system('git clone https://github.com/Gameye98/AstraNmap')
	os.system('mv AstraNmap ~')
	print '>>>> Done'
	backtomenu_option()

def wtf():
	print '>>>> Installing WTF'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip bs4 requests HTMLParser urlparse mechanize argparse')
	os.system('git clone https://github.com/Xi4u7/wtf')
	os.system('mv wtf ~')
	print '>>>> Done'
	backtomenu_option()

def easyMap():
	print '>>>> Installing Easymap'
	os.system('apt update && apt upgrade')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Easymap')
	os.system('mv Easymap ~')
	os.system('cd ~/Easymap && sh install.sh')
	print '>>>> Done'
	backtomenu_option()

def xd3v():
	print '>>>> Installing XD3v'
	os.system('apt update && apt upgrade')
	os.system('apt install curl')
	os.system('curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh')
	os.system('mv xd3v.sh ~/../usr/bin/xd3v && chmod +x ~/../usr/bin/xd3v')
	print '>>>> Done'
	print ">>>> Type 'xd3v' to start."
	backtomenu_option()

def crips():
	print '>>>> Installing Crips'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 openssl curl libcurl wget")
	os.system("git clone https://github.com/Manisso/Crips")
	os.system("mv Crips ~")
	print '>>>> Done'
	backtomenu_option()

def sir():
	print '>>>> Installing SIR'
	os.system("apt update && apt upgrade")
	os.system("apt install python2 git")
	os.system("python2 -m pip install bs4 urllib2")
	os.system("git clone https://github.com/AeonDave/sir.git")
	os.system("mv sir ~")
	print '>>>> Done'
	backtomenu_option()

def xshell():
	print '>>>> Installing Xshell'
	os.system("apt update && apt upgrade")
	os.system("apt install lynx python2 figlet ruby php nano w3m")
	os.system("git clone https://github.com/Ubaii/Xshell")
	os.system("mv Xshell ~")
	print '>>>> Done'
	backtomenu_option()

def evilURL():
	print '>>>> Installing EvilURL'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 python3")
	os.system("git clone https://github.com/UndeadSec/EvilURL")
	os.system("mv EvilURL ~")
	print '>>>> Done'
	backtomenu_option()

def striker():
	print '>>>> Installing Striker'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/UltimateHackers/Striker')
	os.system('mv Striker ~')
	os.system('cd ~/Striker && python2 -m pip install -r requirements.txt')
	print '>>>> Done'
	backtomenu_option()

def dsss():
	print '>>>> Installing DSSS'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/stamparm/DSSS')
	os.system('mv DSSS ~')
	print '>>>> Done'
	backtomenu_option()

def sqliv():
	print '>>>> Installing SQLiv'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Hadesy2k/sqliv')
	os.system('mv sqliv ~')
	print '>>>> Done'
	backtomenu_option()

def sqlscan():
	print '>>>> Installing sqlscan'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone http://www.github.com/Cvar1984/sqlscan')
	os.system('mv sqlscan ~')
	print '>>>> Done'
	backtomenu_option()

def wordpreSScan():
	print '>>>> Installing Wordpresscan'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev')
	os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	os.system('mv Wordpresscan ~')
	os.system('cd ~/Wordpresscan && python2 -m pip install -r requirements.txt')
	print '>>>> Done'
	backtomenu_option()

def wpscan():
	print '>>>> Installing WPScan'
	os.system('apt update && apt upgrade')
	os.system('apt install git ruby curl')
	os.system('git clone https://github.com/wpscanteam/wpscan')
	os.system('mv wpscan ~ && cd ~/wpscan')
	os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
	print '>>>> Done'
	backtomenu_option()

def wordpresscan():
	print '>>>> Installing wordpresscan(2)'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap figlet git')
	os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
	os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
	os.system('mv termux-wordpresscan ~')
	print '>>>> Done'
	print ">>>> Type 'wordpresscan' to start."
	backtomenu_option()

def routersploit():
	print '>>>> Installing Routersploit'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/reverse-shell/routersploit')
	os.system('mv routersploit ~;cd ~/routersploit;python2 -m pip install -r requirements.txt;termux-fix-shebang rsf.py')
	print '>>>> Done'
	backtomenu_option()

def torshammer():
	print '>>>> Installing Torshammer'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/dotfighter/torshammer')
	os.system('mv torshammer ~')
	print '>>>> Done'
	backtomenu_option()

def slowloris():
	print '>>>> Installing Slowloris'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/gkbrk/slowloris')
	os.system('mv slowloris ~')
	print '>>>> Done'
	backtomenu_option()

def fl00d12():
	print '>>>> Installing Fl00d & Fl00d2'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 curl')
	os.system('mkdir ~/fl00d')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py')
	os.system('mv fl00d.py ~/fl00d && mv fl00d2.py ~/fl00d')
	print '>>>> Done'
	backtomenu_option()

def goldeneye():
	print '>>>> Installing GoldenEye'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/jseidl/GoldenEye')
	os.system('mv GoldenEye ~')
	print '>>>> Done'
	backtomenu_option()

def xerxes():
	print '>>>> Installing Xerxes'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('apt install clang')
	os.system('git clone https://github.com/zanyarjamal/xerxes')
	os.system('mv xerxes ~')
	os.system('cd ~/xerxes && clang xerxes.c -o xerxes')
	print '>>>> Done'
	backtomenu_option()

def planetwork_ddos():
	print '>>>> Installing Planetwork-DDOS'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Hydra7/Planetwork-DDOS')
	os.system('mv Planetwork-DDOS ~')
	print '>>>> Done'
	backtomenu_option()

def hydra():
	print '>>>> Installing Hydra'
	os.system('apt update && apt upgrade')
	os.system('apt install hydra')
	print '>>>> Done'
	backtomenu_option()

def black_hydra():
	print '>>>> Installing Black Hydra'
	os.system('apt update && apt upgrade')
	os.system('apt install hydra git python2')
	os.system('git clone https://github.com/Gameye98/Black-Hydra')
	os.system('mv Black-Hydra ~')
	print '>>>> Done'
	backtomenu_option()

def cupp():
	print '>>>> Installing Cupp'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Mebus/cupp')
	os.system('mv cupp ~')
	print '>>>>  Done'
	backtomenu_option()

def asu():
	print '>>>> Installing ASU'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 php')
	os.system('python2 -m pip install requests bs4 mechanize')
	os.system('git clone https://github.com/LOoLzeC/ASU')
	os.system('mv ASU ~')
	print '>>>> Done'
	backtomenu_option()

def hash_buster():
	print '>>>> Installing Hash-Buster'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/UltimateHackers/Hash-Buster')
	os.system('mv Hash-Buster ~')
	print '>>>> Done'
	backtomenu_option()

def instaHack():
	print '>>>> Installing InstaHack'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/avramit/instahack')
	os.system('mv instahack ~')
	print '>>>> Done'
	backtomenu_option()

def indonesian_wordlist():
	print '>>>> Installing indonesian-wordlist'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/geovedi/indonesian-wordlist')
	os.system('mv indonesian-wordlist ~')
	print '>>>> Done'
	backtomenu_option()

def fbBrute():
	print '>>>> Installing Facebook Brute Force 3'
	os.system('apt update && apt upgrade')
	os.system('apt install curl python2')
	os.system('python2 -m pip install mechanize')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/facebook3.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/wordlist/password.txt')
	os.system('mkdir ~/facebook-brute-3')
	os.system('mv facebook3.py ~/facebook-brute-3 && mv password.txt ~/facebook-brute-3')
	print '>>>> Done'
	backtomenu_option()

def webdav():
	print '>>>> Installing Webdav'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 openssl curl libcurl')
	os.system('python2 -m pip install urllib3 chardet certifi idna requests')
	os.system('mkdir ~/webdav')
	os.system('curl -k -O http://override.waper.co/files/webdav.txt;mv webdav.txt ~/webdav/webdav.py')
	print '>>>> Done'
	backtomenu_option()

def xGans():
	print '>>>> Installing xGans'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 curl')
	os.system('mkdir ~/xGans')
	os.system('curl -O http://override.waper.co/files/xgans.txt')
	os.system('mv xgans.txt ~/xGans/xgans.py')
	print '>>>> Done'
	backtomenu_option()

def webmassploit():
	print '>>>> Installing Webdav Mass Exploiter'
	os.system("apt update && apt upgrade")
	os.system("apt install python2 openssl curl libcurl")
	os.system("python2 -m pip install requests")
	os.system("curl -k -O https://pastebin.com/raw/K1VYVHxX && mv K1VYVHxX webdav.py")
	os.system("mkdir ~/webdav-mass-exploit && mv webdav.py ~/webdav-mass-exploit")
	print '>>>> Done'
	backtomenu_option()

def wpsploit():
	print '>>>> Installing WPSploit'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone git clone https://github.com/m4ll0k/wpsploit')
	os.system('mv wpsploit ~')
	print '>>>> Done'
	backtomenu_option()

def sqldump():
	print '>>>> Installing sqldump'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 curl')
	os.system('python2 -m pip install google')
	os.system('curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py')
	os.system('mkdir ~/sqldump && chmod +x sqldump.py && mv sqldump.py ~/sqldump')
	print '>>>> Done'
	backtomenu_option()

def websploit():
	print '>>>> Installing Websploit'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install scapy')
	os.system('git clone https://github.com/The404Hacking/websploit')
	os.system('mv websploit ~')
	print '>>>> Done'
	backtomenu_option()

def sqlokmed():
	print '>>>> Installing sqlokmed'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install urllib2')
	os.system('git clone https://github.com/Anb3rSecID/sqlokmed')
	os.system('mv sqlokmed ~')
	print '>>>> Done'
	backtomenu_option()

def zones():
	print '>>>> Installing zones'
	os.system("apt update && apt upgrade")
	os.system("apt install git php")
	os.system("git clone https://github.com/Cvar1984/zones")
	os.system("mv zones ~")
	print '>>>> Done'
	backtomenu_option()

def metasploit():
	print '>>>> Installing Metasploit'
	os.system("apt update && apt upgrade")
	os.system("apt install git wget curl")
	os.system("wget https://gist.githubusercontent.com/Gameye98/d31055c2d71f2fa5b1fe8c7e691b998c/raw/09e43daceac3027a1458ba43521d9c6c9795d2cb/msfinstall.sh")
	os.system("mv msfinstall.sh ~;cd ~;sh msfinstall.sh")
	print '>>>> Done'
	print ">>>> Type 'msfconsole' to start."
	backtomenu_option()

def commix():
	print '>>>> Installing Commix'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/commixproject/commix')
	os.system('mv commix ~')
	print '>>>> Done'
	backtomenu_option()

def brutal():
	print '>>>> Installing Brutal'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/Screetsec/Brutal')
	os.system('mv Brutal ~')
	print '>>>> Done'
	backtomenu_option()

def a_rat():
	print '>>>> Installing A-Rat'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Xi4u7/A-Rat')
	os.system('mv A-Rat ~')
	print '>>>> Done'
	backtomenu_option()

def knockmail():
	print '>>>> Installing KnockMail'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install validate_email pyDNS')
	os.system('git clone https://github.com/4w4k3/KnockMail')
	os.system('mv KnockMail ~')
	print '>>>> Done'
	backtomenu_option()

def spammer_grab():
	print '>>>> Installing Spammer-Grab'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git && python2 -m pip install requests')
	os.system('git clone https://github.com/p4kl0nc4t/spammer-grab')
	os.system('mv spammer-grab ~')
	print '>>>> Done'
	backtomenu_option()

def hac():
	print '>>>> Installing Hac'
	os.system('apt update && apt upgrade')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Hac')
	os.system('mv Hac ~')
	print '>>>> Done'
	backtomenu_option()

def spammer_email():
	print '>>>> Installing Spammer-Email'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 && python2 -m pip install argparse requests")
	os.system("git clone https://github.com/p4kl0nc4t/Spammer-Email")
	os.system("mv Spammer-Email ~")
	print '>>>> Done'
	backtomenu_option()

def rang3r():
	print '>>>> Installing Rang3r'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 && python2 -m pip install optparse termcolor")
	os.system("git clone https://github.com/floriankunushevci/rang3r")
	os.system("mv rang3r ~")
	print '>>>> Done'
	backtomenu_option()

def sh33ll():
	print '>>>> Installing SH33LL'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2")
	os.system("git clone https://github.com/LOoLzeC/SH33LL")
	os.system("mv SH33LL ~")
	print '>>>> Done'
	backtomenu_option()

def social():
	print '>>>> Installing Social-Engineering'
	os.system("apt update && apt upgrade")
	os.system("apt install python2 perl")
	os.system("git clone https://github.com/LOoLzeC/social-engineering")
	os.system("mv social-engineering ~")
	print '>>>> Done'
	backtomenu_option()

def spiderbot():
	print '>>>> Installing SpiderBot'
	os.system("apt update && apt upgrade")
	os.system("apt install git php")
	os.system("git clone https://github.com/Cvar1984/SpiderBot")
	os.system("mv SpiderBot ~")
	print '>>>> Done'
	backtomenu_option()

def ngrok():
	print '>>>> Installing Ngrok'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/themastersunil/ngrok')
	os.system('mv ngrok ~')
	print '>>>> Done'
	backtomenu_option()

def sudo():
	print '>>>> Installing sudo'
	os.system('apt update && apt upgrade')
	os.system('apt install ncurses-utils git')
	os.system('git clone https://github.com/st42/termux-sudo')
	os.system('mv termux-sudo ~ && cd ~/termux-sudo && chmod 777 *')
	os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
	os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
	print '>>>> Done'
	backtomenu_option()

def ubuntu():
	print '>>>> Installing Ubuntu'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
	os.system('mv termux-ubuntu ~ && cd ~/termux-ubuntu && bash ubuntu.sh')
	print '>>>> Done'
	backtomenu_option()

def fedora():
	print '>>>> Installing Fedora'
	os.system('apt update && apt upgrade')
	os.system('apt install wget git')
	os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
	os.system('mv termux-fedora.sh ~')
	print '>>>> Done'
	backtomenu_option()

def nethunter():
	print '>>>> Installing Kali NetHunter'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
	os.system('mv Nethunter-In-Termux ~')
	print '>>> Done'
	backtomenu_option()

def blackbox():
	print '>>>> Installing BlackBox'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git && python2 -m pip install optparse passlib')
	os.system('git clone https://github.com/jothatron/blackbox')
	os.system('mv blackbox ~')
	print '>>>> Done'
	backtomenu_option()

def xattacker():
	print '>>>> Installing XAttacker'
	os.system('apt update && apt upgrade')
	os.system('apt install git perl')
	os.system('cpnm install HTTP::Request')
	os.system('cpnm install LWP::Useragent')
	os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
	os.system('mv XAttacker ~')
	print '>>>> Done'
	backtomenu_option()

def vcrt():
	print '>>>> Installing VCRT'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/LOoLzeC/Evil-create-framework')
	os.system('mv Evil-create-framework ~')
	print '>>>> Done'
	backtomenu_option()

def socfish():
	print '>>>> Installing SocialFish'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git && python2 -m pip install wget')
	os.system('git clone https://github.com/UndeadSec/SocialFish')
	os.system('mv SocialFish ~')
	print '>>>> Done'
	backtomenu_option()

def ecode():
	print '>>>> Installing ECode'
	os.system('apt update && apt upgrade')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Ecode')
	os.system('mv Ecode ~')
	print '>>>> Done'
	backtomenu_option()

def hashzer():
	print '>>>> Installing Hashzer'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/Anb3rSecID/Hashzer')
	os.system('mv Hashzer ~')
	print '>>>> Done'
	backtomenu_option()

def xsstrike():
	print '>>>> Installing XSStrike'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install fuzzywuzzy prettytable mechanize HTMLParser')
	os.system('git clone https://github.com/UltimateHackers/XSStrike')
	os.system('mv XSStrike ~')
	print '>>>> Done'
	backtomenu_option()

def breacher():
	print '>>>> Installing Breacher'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests argparse')
	os.system('git clone https://github.com/UltimateHackers/Breacher')
	os.system('mv Breacher ~')
	print '>>>> Done'
	backtomenu_option()

def stylemux():
	print '>>>> Installing Termux-Styling'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/BagazMukti/Termux-Styling-Shell-Script')
	os.system('mv Termux-Styling-Shell-Script ~')
	print '>>>> Done'
	backtomenu_option()

def txtool():
	print '>>>> Installing TXTool'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 nmap php curl')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/kuburan/txtool')
	os.system('mv txtool ~')
	print '>>>> Done'
	backtomenu_option()

def passgencvar():
	print '>>>> Installing PassGen'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Cvar1984/PassGen')
	os.system('mv PassGen ~')
	print '>>>>  Done'
	backtomenu_option()

def owscan():
	print '>>>> Installing OWScan'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/OWScan')
	os.system('mv OWScan ~')
	print '>>>> Done'
	backtomenu_option()

def sanlen():
	print '>>>> Installing santet-online'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/santet-online')
	os.system('mv santet-online ~')
	print '>>>> Done'
	backtomenu_option()

def spazsms():
	print '>>>> Installing SpazSMS'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/SpazSMS')
	os.system('mv SpazSMS ~')
	print '>>>> Done'
	backtomenu_option()

def hasher():
	print '>>>> Installing Hasher'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install passlib binascii progressbar')
	os.system('git clone https://github.com/ciku370/hasher')
	os.system('mv hasher ~')
	print '>>>>> Done'
	backtomenu_option()

def hashgenerator():
	print '>>>>> Installing Hash-Generator'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install passlib progressbar')
	os.system('git clone https://github.com/ciku370/hash-generator')
	os.system('mv hash-generator ~')
	print '>>>> Done'
	backtomenu_option()

def kodork():
	print '>>>> Installing ko-dork'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/ciku370/ko-dork')
	os.system('mv ko-dork ~')
	print '>>>> Done'
	backtomenu_option()

def snitch():
	print '\n###### Installing snitch'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Smaash/snitch')
	os.system('mv snitch ~')
	print '###### Done'
	backtomenu_option()

def osif():
	print '\n###### Installing OSIF'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/ciku370/OSIF')
	os.system('mv OSIF ~')
	print '###### Done'
	backtomenu_option()

def nk26():
	print '\n###### Installing nk26'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone ')
	os.system('mv nk26 ~')
	print '###### Done'
	backtomenu_option()

def devploit():
	print '\n###### Installing Devploit'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git && python2 -m pip install urllib2')
	os.system('git clone https://github.com/joker25000/Devploit')
	os.system('mv Devploit ~')
	print '###### Done'
	backtomenu_option()

def hasherdotid():
	print '\n###### Installing Hasherdotid'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/galauerscrew/hasherdotid')
	os.system('mv hasherdotid ~')
	print '###### Done'
	backtomenu_option()

def namechk():
	print '\n###### Installing Namechk'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/HA71/Namechk')
	os.system('mv Namechk ~')
	print '###### Done'
	backtomenu_option()

def xlPy():
	print '\n###### Installing xl-py'
	os.system('apt update && apt upgrade')
	os.system('apt install python git')
	os.system('git clone https://github.com/albertoanggi/xl-py')
	os.system('mv xl-py ~')
	print '###### Done'
	backtomenu_option()

def beanshell():
	print '\n###### Installing Beanshell'
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/amsitlab/amsitlab.github.io/raw/master/dists/termux/amsitlab/binary-all/beanshell_2.04_all.deb')
	os.system('dpkg -i beanshell_2.04_all.deb')
	os.system('rm beanshell_2.04_all.deb')
	print '###### Done'
	print "###### Type 'bsh' to start."
	backtomenu_option()

def msfpg():
	print '\n###### Installing MSF-Pg'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/haxzsadik/MSF-Pg')
	os.system('mv MSF-Pg ~')
	print "###### Done"
	backtomenu_option()

def crunch():
	print '\n###### Installing Crunch'
	os.system('apt update && apt upgrade')
	os.system('apt install unstable-repo')
	os.system('apt install crunch')
	print "###### Done"
	print "###### Type 'crunch' to start."
	backtomenu_option()

def webconn():
	print '\n###### Installing WebConn'
	os.system('apt update && apt upgrade')
	os.system('apt install python git')
	os.system('git clone https://github.com/SkyKnight-Team/WebConn')
	os.system('mv WebConn ~')
	print "###### Done"
	backtomenu_option()

def binploit():
	print '\n###### Installing Binary Exploitation'
	os.system('apt update && apt upgrade')
	os.system('apt install gdb radare2 ired ddrescue bin-utils yasm strace ltrace cdb hexcurse memcached llvmdb')
	print "###### Done"
	print "###### Tutorial: https://youtu.be/3NTXFUxcKPc"
	backtomenu_option()

def textr():
	print '\n###### Installing Textr'
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/amsitlab/textr/master/textr_1.0_all.deb')
	os.system('dpkg -i textr_1.0_all.deb')
	os.system('rm textr_1.0_all.deb')
	print '###### Done'
	print "###### Type 'textr' to start."
	backtomenu_option()

def apsca():
	print '\n###### Installing ApSca'
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/BlackHoleSecurity/apsca/master/apsca_0.1_all.deb')
	os.system('dpkg -i apsca_0.1_all.deb')
	os.system('rm apsca_0.1_all.deb')
	print '###### Done'
	print "###### Type 'apsca' to start."
	backtomenu_option()

def amox():
	print '\n###### Installing amox'
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://gitlab.com/dtlily/amox/raw/master/amox_1.0_all.deb')
	os.system('dpkg -i amox_1.0_all.deb')
	os.system('rm amox_1.0_all.deb')
	print '###### Done'
	print "###### Type 'amox' to start."
	backtomenu_option()

def fade():
	print '>>>> Installing FaDe'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FaDe')
	os.system('mv FaDe ~')
	print '>>>> Done'
	backtomenu_option()

def ginf():
	print '>>>> Installing GINF'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/GINF')
	os.system('mv GINF ~')
	print '>>>> Done'
	backtomenu_option()

def auxile():
	print '>>>> Installing AUXILE'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install requests bs4 pexpect')
	os.system('git clone https://github.com/CiKu370/AUXILE')
	os.system('mv AUXILE ~')
	print '>>>> Done'
	backtomenu_option()

def inther():
	print '>>>> Installing inther'
	os.system('apt update && apt upgrade')
	os.system('apt install git ruby')
	os.system('git clone https://github.com/Gameye98/inther')
	os.system('mv inther ~')
	print '>>>> Done'
	backtomenu_option()

def hpb():
	print '>>>> Installing HPB'
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/Cvar1984/HPB/master/html_0.1_all.deb')
	os.system('dpkg -i html_0.1_all.deb')
	os.system('rm html_0.1_all.deb')
	print '>>>> Done'
	print ">>>> Type 'hpb' to start."
	backtomenu_option()

def fmbrute():
	print '>>>> Installing FMBrute'
	os.system('apt update && apt upgrade')
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/BlackHoleSecurity/FMBrute')
	os.system('mv FMBrute ~')
	print '>>>> Done'
	backtomenu_option()

def hashid():
	print '>>>> Installing HashID'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 && python2 -m pip install hashid')
	print ">>>> Done"
	print ">>>>  Type 'hashid -h' to show usage of hashid"
	backtomenu_option()

def gpstr():
	print '>>>> Installing GPS Tracking'
	os.system('apt update && apt upgrade')
	os.system('apt install php git')
	os.system('git clone https://github.com/indosecid/gps_tracking')
	os.system('mv gps_tracking ~')
	print ">>>> Done"
	backtomenu_option()

def pret():
	print '>>>> Installing PRET'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 imagemagick git')
	os.system('python2 -m pip install colorama pysnmp')
	os.system('git clone https://github.com/RUB-NDS/PRET')
	os.system('mv PRET ~')
	print ">>>> Done"
	backtomenu_option()

def autovisitor():
	print '>>>> Installing AutoVisitor'
	os.system('apt update && apt upgrade')
	os.system('apt install git curl')
	os.system('git clone https://github.com/wannabeee/AutoVisitor')
	os.system('mv AutoVisitor ~')
	print ">>>> Done"
	backtomenu_option()

def atlas():
	print '>>>> Installing Atlas'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/m4ll0k/Atlas')
	os.system('mv Atlas ~')
	print ">>>> Done"
	backtomenu_option()

def hashcat():
	print '>>>> Installing Hashcat'
	os.system('apt update && apt upgrade')
	os.system('apt install unstable-repo')
	os.system('apt install hashcat')
	print ">>>> Done"
	print ">>>> Type 'hashcat' to start."
	backtomenu_option()

def liteotp():
	print '>>>> Installing LiteOTP'
	os.system('apt update && apt upgrade')
	os.system('apt install php wget')
	os.system('wget https://raw.githubusercontent.com/Cvar1984/LiteOTP/master/build/main.phar -O $PREFIX/bin/lite')
	print ">>>> Done"
	print ">>>> Type 'lite' to start."
	backtomenu_option()

def fbbrutex():
	print '>>>> Installing FBBrute'
	os.system('apt update && apt upgrade')
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FBBrute')
	os.system('mv FBBrute ~')
	print '>>>> Done'
	backtomenu_option()

def fim():
	print '>>>> Installing fim'
	os.system('apt update && apt upgrade')
	os.system('apt install git python && python -m pip install requests bs4')
	os.system('git clone https://github.com/karjok/fim')
	os.system('mv fim ~')
	print '>>>> Done'
	backtomenu_option()

def rshell():
	print '>>>> Installing RShell'
	os.system('apt update && apt upgrade')
	os.system('apt install git python && python -m pip install colorama')
	os.system('git clone https://github.com/Jishu-Epic/RShell')
	os.system('mv RShell ~')
	print '>>>> Done'
	backtomenu_option()

def termpyter():
	print '>>>> Installing TermPyter'
	os.system('apt update && apt upgrade')
	os.system('apt install git python')
	os.system('git clone https://github.com/Jishu-Epic/TermPyter')
	os.system('mv TermPyter ~')
	print '>>>> Done'
	backtomenu_option()

def maxsubdofinder():
	print '>>>> Installing MaxSubdoFinder'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/maxteroit/MaxSubdoFinder')
	os.system('mv MaxSubdoFinder ~')
	print '>>>> Done'
	backtomenu_option()

def jadx():
	print '>>>> Installing jadx'
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Lexiie/Termux-Jadx/blob/master/jadx-0.6.1_all.deb?raw=true')
	os.system('dpkg -i jadx-0.6.1_all.deb?raw=true')
	os.system('rm -rf jadx-0.6.1_all.deb?raw=true')
	print '>>>> Done'
	print ">>>> Type 'jadx' to start."
	backtomenu_option()

def pwnedornot():
	print '>>>>> Installing pwnedOrNot'
	os.system('apt update && apt upgrade')
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/thewhiteh4t/pwnedOrNot')
	os.system('mv pwnedOrNot ~')
	print '>>>> Done'
	backtomenu_option()

def maclook():
	print '>>>>> Installing Mac-Lookup'
	os.system('apt update && apt upgrade')
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/T4P4N/Mac-Lookup')
	os.system('mv Mac-Lookup ~')
	print '>>>> Done'
	backtomenu_option()

def f4k3():
	print '>>>> Installing F4K3'
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Gameye98/Gameye98.github.io/blob/master/package/f4k3_1.0_all.deb')
	os.system('dpkg -i f4k3_1.0_all.deb')
	os.system('rm -rf f4k3_1.0_all.deb')
	print '>>>> Done'
	print ">>>> Type 'f4k3' to start."
	backtomenu_option()

def katak():
	print '>>>> Installing Katak'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests progressbar')
	os.system('git clone https://github.com/Gameye98/Katak')
	os.system('mv Katak ~')
	print '>>>> Done'
	backtomenu_option()
