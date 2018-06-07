# -*- coding:utf-8 -*-
__author__ = 'xuan'


import  re

link = 'https://www.amazon.com/Will-this-fan-work-dark/forum/Fx2K0VD6D56JZXH/Tx366CEHUPJ26JR/2/ref=cm_cd_al_psf_al_pg2?_encoding=UTF8&asin=B001R1RXUG'

link_regex1=r'https://www.amazon.com/(\w+.*)/forum/(\w+.*)/(\w+.*)/(\d+.*)/ref=cm_cd_al_psf_al_pg(\d+.*)\?_encoding=UTF8&asin=(\w+.*)'
result = re.match(link_regex1, link)


print(result.group())



