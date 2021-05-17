from database import mycollection

sales_list = []

for i in mycollection.find():
    sales_list.append(i)

sellers = ['Singapore', 'Indonesia', 'Malaysia', 'Thailand', 'Brazil']