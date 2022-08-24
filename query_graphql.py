#目標是取得https://www.tcloud.gov.tw/solution 的架上方案數
import requests
import json
import pandas as pd


query_string="query Solutions($limit: Int, $offset: Int, $name: String, $categoryIds: [ID!], $subCategoryIds: [ID!], $zoneIds: [ID!], $ids: [ID!], $sort: SolutionSortEnum) {\n  solutions(\n    limit: $limit\n    offset: $offset\n    name: $name\n    categoryIds: $categoryIds\n    subCategoryIds: $subCategoryIds\n    zoneIds: $zoneIds\n    ids: $ids\n    sort: $sort\n  ) {\n    id\n    items {\n      id\n      name\n      star\n      supplierName\n      serviceImage\n      displayBadge\n      tags {\n        id\n        name\n        __typename\n      }\n      specs {\n        price\n        __typename\n      }\n      zones {\n        id\n        name\n        __typename\n      }\n      categories {\n        id\n        name\n        subCategories {\n          name\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    total\n    __typename\n  }\n}\n"
#要請求的url
url = 'https://www.tcloud.gov.tw/graphql'
r = requests.post(url, json={'query': query_string})
print(r.status_code)
#印出抓到的東西
#print(r.text)
#這邊因為respone的內容是一個巢狀的字典結構
json_data = json.loads(r.text).get('data')
jslist = list(json_data.items())
solution_nums=jslist[0][1].get('total')
print(solution_nums)
