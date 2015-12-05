from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)


def gatherstuff(name, url):
	domain_name = get_domain_name(url)
	ip_address = get_ip_address(domain_name)
	nmap = get_nmap('-F', ip_address)
	#robots_txt = get_robots_txt(url)
	whois = get_whois(domain_name)
	create_report(name, url, domain_name, nmap,whois)


def create_report(name, url, domain_name, nmap ,whois):
	project = ROOT_DIR + '/' + name
	create_dir(project)
	write_file(project + '/full_url.txt',url)
	write_file(project + '/domain_name.txt',domain_name)
	write_file(project + '/nmap.txt',nmap)
	#write_file(project + '/robots.txt',robots_txt)
	write_file(project + '/whois.txt',whois)


gatherstuff('songdew', 'http://www.songdew.com')