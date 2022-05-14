from django.http import response
from django.shortcuts import get_object_or_404, render


from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from store.models import Product
from .basket import Basket

def basket_summary(request):
    basket = Basket(request)
   # print(basket)
    return render(request, 'store/basket/summary.html', {'basket':basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product , qty= product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty':basketqty})   #({'qty': basketqty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        #basketqty = basket.__len__()
        #baskettotal = basket.get_total_price()
        response = JsonResponse({'success': True })
        return response