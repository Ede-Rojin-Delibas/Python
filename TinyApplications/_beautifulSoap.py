html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk web sayfam</title>
</head>
<body>
<h1 id="header">Python Kursu-HTML </h1>
    <div class="grup-1">
        <h2>Programlama</h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
        <h2>HTML</h2>
        <ul>
            <li>Etiketler</li>
            <li>DOCTYPE</li>
        </ul>
</div>
        <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>,
        <a class="sister" href="http://example2.com/lacie" id="link2">Lacie</a>,
        <a class="sister" href="http://example3.com/tillie" id="link3">Tillie</a>
</body>
</html>
        """

from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,'html.parser')
result=soup.prettify()
result=soup.title
result=soup.head
result=soup.h1
result=soup.h1.string
result=soup.find_all('h2')[1] #h2 etiketlerinin hepsini getirir, normalde sadece ilkini getirilmişti
result=soup.find_all('div')[0]
# result=soup.div.findChildren()
result=soup.find_all('a')
for link in result:
    print(link.get('href')) #attribute'lara erişim
# print(result)
















