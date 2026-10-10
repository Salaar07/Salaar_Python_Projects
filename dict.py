import json
dic[] = input()
dic = {
    "name":'M.Salaar',
    "mark" :323,
    "subject":'Python',
    "age": 18,
    "address":'House no. 4'
}
print(dic)
with open("f:\\Python codes\\dict.json",'w') as store :
    json.dump(dic,store)
