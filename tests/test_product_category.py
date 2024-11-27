from unicodedata import category


def test_product_creation(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

def test_product_creation_2(product2):
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8


def test_product_creation_3(product3):
    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.description == "1024GB, Синий"
    assert product3.price == 31000.0
    assert product3.quantity ==  14


def test_category_creation_with_products(category1, product1, product2, product3):
    category = category1
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category.products) == 3
    assert category.products[0] == product1
    assert category.products[1] == product2
    assert category.products[2] == product3


def test_category_creation_with_products_2(category2, product4):
    category_2 = category2
    assert category_2.name == "Телевизоры"
    assert category_2.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert len(category2.products) == 1
    assert category_2.products[0] == product4
    assert category_2.category_count == 2
    assert category_2.product_count == 4

