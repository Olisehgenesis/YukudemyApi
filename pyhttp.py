import http.client
#importJson
conn = http.client.HTTPSConnection("api.yukusite.com")
headers = {
  'secret-key': str(input("Secret Key"))
}
article_title = str(input("Article Title:"))
key_points = str(input("Key Points Atleast 16 Word:"))
article_content = str(input("Body :"))
article_content_format="html"
tags= str(input("Tags:"))
eyrie_id=str(int(input("Eyrie_id:")))
payload = { 
    'article_title':article_title,
    'article_content':article_content,
    'key_points':key_points,
    'article_content_format':"html",
    'tags':tags,
    'eyrie_id':eyrie_id
    }
#payload = json.dumps(payload)
conn.request("POST", "/v1/owner/create_new_article", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

