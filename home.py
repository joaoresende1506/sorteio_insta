# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)


# driver.get("https://www.instagram.com/p/C64mfeRvn3z")

# time.sleep(10)

# driver.quit()


import instaloader
from instaloader.exceptions import TwoFactorAuthRequiredException
import pandas as pd


# Crie uma instância do Instaloader
L = instaloader.Instaloader()

# Faça login (necessário para acessar perfis privados)
login = '123'
password = '123'

try:
    L.login(login, password)
except TwoFactorAuthRequiredException:
    L.two_factor_login(335029)

# Carregue o post
post = instaloader.Post.from_shortcode(L.context, 'C64mfeRvn3z')

# Extraia os comentários
comments_data = []
for comment in post.get_comments():
    comments_data.append({
        'Nome': comment.owner.username,
        'Comentário': comment.text,
        'Hora': comment.created_at_utc
    })

# Crie um DataFrame com os dados dos comentários
df = pd.DataFrame(comments_data)

# Salve o DataFrame em uma planilha Excel
df.to_excel('comentarios2.xlsx', index=False)

print(f"Extraído {len(comments_data)} comentários e salvo em comentarios.xlsx.")