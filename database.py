import pymongo

client=pymongo.MongoClient()

mydb = client['Shopee']

mycollection = mydb['sales']

#modify this list as you wish, as long as you keep its keys ("seller_name, customer_name, sale_date, item_name and price")
sales_list = [
    {
        'seller_name': 'Singapore',
        'customer_name': 'José',
        'sale_date': '2021-03-20',
        'item_name': 'Calça Jeans Sarja Masculina Skinny Slim',
        'price': 41.90
    },
    {
        'seller_name': 'Indonesia',
        'customer_name': 'Maria',
        'sale_date': '2020-20-11',
        'item_name': 'Tenis Infantil Club Happy várias cores',
        'price': 39.54
    },
    {
        'seller_name': 'Singapore',
        'customer_name': 'Caio',
        'sale_date': '2019-03-20',
        'item_name': 'Ring Light Led Mesa Iluminador Pequena Tripé 6 Polegada 16cm',
        'price': 25.88
    },
    {
        'seller_name': 'Malaysia',
        'customer_name': 'Marcos',
        'sale_date': '2021-01-15',
        'item_name': 'Meias Cano Alto UNISSEX KIT 12 PARES Muito Barato Promoção Atacado Revenda Oferta',
        'price': 22.99
    },
    {
        'seller_name': 'Thailand',
        'customer_name': 'Bruna',
        'sale_date': '2021-04-02',
        'item_name': 'Máscara Descartável De Proteção Facial Tripla Cx C/ 50 Pçs',
        'price': 10.00
    },
    {
        'seller_name': 'Brazil',
        'customer_name': 'Daniela',
        'sale_date': '2021-05-11',
        'item_name': 'Calça Moletom Slim Unissex Liso Sem Estampa Atacado',
        'price': 54.99
    },
    {
        'seller_name': 'Malaysia',
        'customer_name': 'Mariana',
        'sale_date': '2021-05-15',
        'item_name': 'Raquete Elétrica Bivolt 110v~220v Mata Mosquito Dengue Insetos Recarregável ECENS BBSL006A',
        'price': 16.99
    },
    {
        'seller_name': 'Brazil',
        'customer_name': 'Vinicius',
        'sale_date': '2021-01-11',
        'item_name': 'Bomba Elétrica Universal com Carregamento USB para Galão/Garrafão de Água',
        'price': 16.88
    },
    {
        'seller_name': 'Thailand',
        'customer_name': 'Vitor',
        'sale_date': '2015-04-02',
        'item_name': 'Mini Triturador de Cebola Alho Alimentos Mini Food Chopper',
        'price': 14.90
    },
    {
        'seller_name': 'Indonesia',
        'customer_name': 'Juliana',
        'sale_date': '2019-12-11',
        'item_name': 'Blusa Moletom Unissex Gola Redonda Liso em Algodão Casual',
        'price': 59.90
    },
    {
        'seller_name': 'Singapore',
        'customer_name': 'Pedro',
        'sale_date': '2020-04-01',
        'item_name': 'Lampada Bluetooth De Led Caixa De Som C Controle 12w Rgb',
        'price': 26.545
    },
    {
        'seller_name': 'Indonesia',
        'customer_name': 'Rodrigo',
        'sale_date': '2018-08-17',
        'item_name': 'Bolinhas Cravo Anti Stress Pet Atacado e Varejos',
        'price': 1.90
    },
]

old_item = {
        'seller_name': 'Brazil',
        'customer_name': 'Rodrigo',
        'sale_date': '2018-08-17',
        'item_name': 'Bolinhas Cravo Anti Stress Pet Atacado e Varejos',
        'price': 1.90
    }



#uncomment the line below to add the items in your database
# mycollection.insert_many(sales_list)
