from googlesearch import search

busca = input("digite sua busca: ")

for i in search(busca, tld = "com", num = 10, stop = 10, pause =2):
    print(i)
