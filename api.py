import requests

#url
Base_Url = "https://api.yukusite.com"
create_new_article = "/v1/owner/create_new_article"
endpoint_Url = create_new_article
Url = Base_Url + endpoint_Url

#headers
headers = {
    'secret-key' : str(input("Secret Key:")),
    'content-type' : 'application/x-www-form-urlencoded'
    }

#body
article_title = str(input("Article Title:"))
for key_words in range(0,15):
     key_points = str(input(" Please Enter Key Points Above 15 Word:"))
     key_words = len(key_points.split())
     if (key_words > 15):
         break
article_content = str(input("Body :"))
article_content_format="html"
tags= str(input("Tags:"))
eyrie_id=str(int(input("Eyrie_id:")))
payload={ "article_title":article_title,
          "article_content":article_content,
          "key_points":key_points,
          "article_content_format":"html",
          "tags":tags,
          "eyrie_id":eyrie_id }


#request
response = requests.request(method="POST" ,url=Url,data=payload,headers=headers)
print(response.text)
