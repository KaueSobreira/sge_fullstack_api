from products.models import Product
from django.utils.formats import number_format
from django.db.models import Sum



def get_product_metrics():
    # MODO NATIVO USANDO PYTHON
    # products = Product.objects.all()
    # total_cost_price = sum(product.cost_price * product.quantity for product in products)
    # total_selling_price = sum(product.selling_price * product.quantity for product in products)
    # total_quatity = sum(product.quantity for product in products)
    # total_profit = total_selling_price - total_cost_price


    total_quantity = Product.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    total_cost_price = Product.objects.aggregate(total_cost_price=Sum('cost_price'))['total_cost_price']
    total_selling_price = Product.objects.aggregate(total_selling_price=Sum('selling_price'))['total_selling_price']
    total_profit = total_selling_price - total_cost_price


    return {
        'total_quantity': total_quantity,
        'total_cost_price': number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        'total_selling_price': number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        'total_profit': number_format(total_profit, decimal_pos=2, force_grouping=True),
    }