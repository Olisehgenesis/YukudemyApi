import requests

#url
Base_Url = "https://api.yukusite.com"
create_new_article = "/v1/owner/create_new_article"
endpoint_Url = create_new_article
Url = Base_Url + endpoint_Url

#headers
headers = {
    'secret-key' : 'Y2J4dWZuY3pucmtmbGF6dG1sa29vcGRz',
    'content-type' : 'application/x-www-form-urlencoded'
    }

#body
article_title = str(input("Article Title:"))
key_points = str(input("Key Points Atleast 16 Word:"))
article_content = str(input("Body :"))
article_content_format="html"
tags= str(input("Tags:"))
eyrie_id=str(int(input("Eyrie_id:")))
payload = "article_title="+article_title+"&"+"key_point="+key_points+"&"+"article_content="+article_content+"&"+"article_content_format=html"+"tags="+tags+"&"+"eyrie_id="+eyrie_id

#request
response = requests.request(method="POST" ,url=Url,data=payload,headers=headers)
print(response.text)
