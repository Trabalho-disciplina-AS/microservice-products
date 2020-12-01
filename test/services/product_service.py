from products.models.product_model import Product


def get_random_product():
    pass


def get_products_with_discount():
    pass


def insert_product(body: dict, image):
    product = Product(**body).save()
    product.image.put(image, content_type='image/jpeg')
    return str(product.id)
