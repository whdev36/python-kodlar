# 🔥 1. GET so‘rovi

import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

print(response.status_code)
print(response.json())

# 📝 2. POST so‘rovi
url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'Salom dunyo!',
    'body': "Men API orqali ma'lumot yuboratapman.",
    'userId': 1
}

resp = requests.post(url, json=data)
print(resp.status_code)
print(resp.json())

# 🔄 3. PUT so‘rovi
url = 'https://jsonplaceholder.typicode.com/posts/1'
updated_data = {
    'title': 'Yangilangan sarlavha',
    'body': "Bu ma'lumot PUT orqali yangilandi",
    'userId': 1
}

resp = requests.put(url, json=updated_data)
print(resp.status_code)
print(resp.json())

# ❌ 4. DELETE so‘rovi
url = 'https://jsonplaceholder.typicode.com/posts/1'
resp = requests.delete(url)

print(resp.status_code)

# 🛡️ 5. So‘rovga header va token qo‘shish
url = "https://api.example.com/user"
headers = {
    'Authorization': 'Bearer SIZNING_API_TOKENINGIZ'
}
# resp = requests.get(url, headers=headers)
# print(resp.json())

# 📂 6. JSON ma’lumotlarni faylga saqlash
import json
url = "https://jsonplaceholder.typicode.com/posts"
resp = requests.get(url)

data = resp.json()

# JSON faylga saqlash
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# 🧐 API xatolarini ushlash (try-except)
try:
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/1000")
    resp.raise_for_status()
    print(resp.json())
except requests.exceptions.HTTPError as e:
    print('Xatolik:', e)