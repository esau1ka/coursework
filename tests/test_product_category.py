def test_product_creation(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

def test_product_creation_2(product2):
    assert product2.name == "Iphone 15"

def test_product_creation_3(product3):
    assert product3.name == "Xiaomi Redmi Note 11"


def test_category_creation_with_products(category1, product1, product2, product3):
    category = category1
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category.products) == 3
    assert category.products[0] == product1
    assert category.products[1] == product2
    assert category.products[2] == product3
