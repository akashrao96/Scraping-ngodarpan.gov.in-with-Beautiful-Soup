from bs4 import BeautifulSoup
import requests
import time
import csv

def get_token(sess):
    req_csrf = sess.get('https://ngodarpan.gov.in/index.php/ajaxcontroller/get_csrf')
    return req_csrf.json()['csrf_token']


search_url = "https://ngodarpan.gov.in/index.php/ajaxcontroller/search_index_new/{}"
details_url = "https://ngodarpan.gov.in/index.php/ajaxcontroller/show_ngo_info"

sess = requests.Session()
fp=open('ngo_data.csv','a')
for page in range(0,77550,10):    # Advance 10 at a time
    print(f"Getting results from {page}")

    for retry in range(1, 5):

        data = {
            'state_search' : '', 
            'district_search' : '',
            'sector_search' : 'null',
            'ngo_type_search' : 'null',
            'ngo_name_search' : '',
            'unique_id_search' : '',
            'view_type' : 'detail_view',
            'csrf_test_name' : get_token(sess), 
        }

        req_search = sess.post(search_url.format(page), data=data, headers={'X-Requested-With' : 'XMLHttpRequest'})
        soup = BeautifulSoup(req_search.content, "html.parser")
        table = soup.find('table', id='example')

        if table:
            for tr in table.find_all('tr'):
                row = [td.text for td in tr.find_all('td')]
                link = tr.find('a', onclick=True)

                if link:
                    link_number = link['onclick'].strip("show_ngif(')")
                    req_details = sess.post(details_url, headers={'X-Requested-With' : 'XMLHttpRequest'}, data={'id' : link_number, 'csrf_test_name' : get_token(sess)})
                    json = req_details.json()
                    details = json['infor']['0']
                    print([details['Mobile'], details['Email'], row[1], row[2]])
                    x=[str(row[1]),str(details['Mobile']),str(details['Email']),str(row[2])]
                    csv_writer = csv.writer(fp)
                    csv_writer.writerow(x)


            break
        else:
            print(f'No data returned - retry {retry}')
            time.sleep(3)

fp.close()
        
  
