import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_mail():
        
    ll = []    
    for page in tqdm(range(200)):
        cookies = {
            '_fbp': 'fb.1.1723450571988.89398787172581608',
            '_gid': 'GA1.2.1235165277.1724053866',
            '_gat_gtag_UA_114510433_4': '1',
            'XSRF-TOKEN': 'eyJpdiI6InU4SFl2Y2JkQzY0Q3NxZUVBRkVaZmc9PSIsInZhbHVlIjoiSFhwUEJWeTJtQWg0T2s3Qlp5aFBTMnp3TTFyWnRBM0FJZDl0YkpESy9KWnl3VFN2NTJBWVFpdCtMajN5Nm1JZmQ0ZzIybWI2ZUt3WHhpbmIrVnFudTdaUy9WTmZkWEtFL0FQdHVrZDNDbTdqWFExTHlHOWZUS2c5Mmd0Z3d5cmIiLCJtYWMiOiJhNTFkNTM4MjVlMTQ0ODU5ZDdlZmY2ZmU4MzM5MmZmNzhkOTY1MDE5ODEyY2Y5NjI2ODEwNWQ0NTYxNTVmMjk2In0%3D',
            'recruitref_session': 'eyJpdiI6Im5LY053K2VpY3JtdDZWTlMwbkdKVGc9PSIsInZhbHVlIjoid1ozU1dwRUhULzgyQnJ0VVZhNkZzeVZQK3R3a002UUpaSC92RTdJMWFNUFdPaEtmR082NjV3cUV1ZzVISk1iTTZpVUlkNkQzQ3dqK05CalRKaEp3TzlwT3hSSThOQXdna2FaWlBYaGJEbTZmMEtubE95M0dTWkFna2RwZWhwRnoiLCJtYWMiOiI3Nzk5MGExYmY0MDQyNzdkMWYwN2EyMzM0NGU4MTY4MGY1NTgzZjdlMDViYzY3OTcxYzFlZDQxNjJmYzc1YzEwIn0%3D',
            '_ga_PNHZM3XYNX': 'GS1.1.1724072597.5.1.1724072599.58.0.0',
            '_ga': 'GA1.1.541319496.1723450572',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,sv;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': '_fbp=fb.1.1723450571988.89398787172581608; _gid=GA1.2.1235165277.1724053866; XSRF-TOKEN=eyJpdiI6IkxIcGtES0MwM3NJWXl4UjJSQVBZSGc9PSIsInZhbHVlIjoieXRzZHMvOFFWd3N5N2Y2L2YxSVlJdzFYbFVVTSsyY2ZvSnZKMU5JazBPRytidFI1eitZVmRpNGQzMGU1WmxCZitLMXJBZnMydzN5dDlPTkFWUFlGb2hKaUJnRFFia3hTek15V2d6UGVnYVdyYTRzbFZNU3hyc285UnF1cGlLeGQiLCJtYWMiOiJjMjBjOTU1OWZhMjBmNjdiNGUyMGI3Y2VlNWMzNDBiZGQxMzViM2RmMjYwNTZhYTlhYjZkYTYwZTFiMTA2MDhiIn0%3D; recruitref_session=eyJpdiI6Im5pZU9PbVBxU3lWYXZJS0R3elIyM1E9PSIsInZhbHVlIjoibDIxUURsSjNnbUlDeHV5QUFzdmJjR1ZEOGxpUlpZSEJVaXQzS2JKcHVvS2xxSEJCOGNuZEl2L2dacS9jWkNXWWVqcEg0WmRFRjhvK3hNeC8waytsbE5DSVZmRlc1YnNwdmJXR2ZvVm1JcFdmR1c3QVljNDdVaEhmK3dhdUFRUS8iLCJtYWMiOiI1MzNiZGQ5OTkzOWZiMjZhNmJhZTk1NDU0ZDJmZTQ2OWZjZjQwNjE1M2Y1YWFlYzZjYjI4NWM1MmNhZTZhYTQ3In0%3D; _ga_PNHZM3XYNX=GS1.1.1724053866.3.1.1724054087.2.0.0; _ga=GA1.1.541319496.1723450572',
            'Referer': 'https://www.recruitref.com/dashboard/sports/mens-soccer',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'page': page + 1,
        }

        response = requests.get(
            'https://www.recruitref.com/dashboard/sports/mens-soccer',
            params=params,
            cookies=cookies,
            headers=headers,
        )
        
        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('div', {'class':'grid grid-cols-1 sm:grid-cols-3 p-4 md:p-0 gap-4 text-gray-700 overflow-auto'})
            all_s = table.find_all('div', {'class':'overflow-auto'})
            
            def parse_school(c):
                
                try:
                    c = list(filter(None, c.split('\n')))
                    if len(c) < 5:
                        return 400
                    wanted = ['College', 'Conference', 'Division','Null', 'State', 'Name', 'Position', 'Email', 'Phone']
                    ret = {wanted[c.index(i)]:i for i in c}
                    
                    return ret
                except:
                    return None
            
            payload = [parse_school(i.text) for i in all_s]
            if 400 in payload:
                break
            
            ll += [i for i in payload if i]
            
            
        else:
            print(response.text)
            break
                        
            
    
    
    