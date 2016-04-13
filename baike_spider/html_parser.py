#coding:utf8
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    
    def _get_new_urls(self, page_url, soup):
        new_urls=[]
        
        link_nodes=soup.find_all('a',href=re.compile(r'/\D*view/\d+'))
        for link_node in link_nodes:
            new_url=urlparse.urljoin(page_url, link_node['href'])
            #print new_url
            new_urls.append(new_url)
            #print(new_urls)
        #for new_u in new_urls:
         #   print new_u
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        res_data={}
        
        res_data['url']=page_url
        #<dd class="lemmaWgt-lemmaTitle-title">  <h1>Python</h1>
        title_node=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title']=title_node.get_text()
        
        summary_node=soup.find('div',class_="lemma-summary")
        res_data['summary']=summary_node.get_text()
        
        return res_data
    
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_url=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_url,new_data
        
    
    



