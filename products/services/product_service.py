from products.models.product_model import Product


def get_products():
    return Product.objects(category={"$exists": True})


def get_product_by_id(_id):
    return Product.objects(id=_id).first()


def get_products_by_category(category):
    return Product.objects(category=category)


def get_random_product():
    return Product.objects().first()


def get_products_with_discount():
    return Product.objects(discount=True)


def get_image_by_id(_id):
    return Product.objects(id=_id).first().image


def get_products_by_criteria(
    qtd=1, category={"$exists": True}, discount={"$exists": True}
):
    return Product.objects(category=category, discount=discount).limit(int(qtd))


def insert_product(body: dict, image):
    product = Product(**body)
    product.image.put(image, content_type="image/jpeg")
    product.save()
    return str(product.id)
