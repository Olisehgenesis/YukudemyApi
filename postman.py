import requests

url = "https://api.yukusite.com/v1/owner/create_new_article"

payload='article_title=Google%20Developers%20Muni&key_points=%20%20working%20with%20the%20Yukemy%20Api%20By%20Google%20devopers%20Muni%20University%20and%20Working%20with%20YUkusites%20and%20Yuku%20Apps&article_content=article%20content1article%20content1article%20content1article%20content1article%20content1article%20content1article%20content1article%20content1article%20content1article%20content1article%20content1article%20content1article%20content1article%20content1article%20content1article%20content1article%20content1article&article_content_format=html&tags=tag1%20%2C%20tag%202%2C%20tag3%2C%20&eyrie_id=223'
headers = {
  'secret-key': 'Y2J4dWZuY3pucmtmbGF6dG1sa29vcGRz'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
