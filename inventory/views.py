import json
from datetime import datetime,timedelta
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from inventory import models

def get_product_price(request,product_id):
    try:
        product = models.Product.objects.get(id=product_id)
        current_date = datetime.now().date()
        product_price = models.ProductPriceHistory.objects.get(product=product,date=current_date).price
#        product_price = price_history.filter(date=current_date)[0].price
        product_details = {'product_name':product.name,'product_price':product_price}
        product_details = json.dumps(product_details)
        return HttpResponse(product_details)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()

def update_product_price(request,product_id):
    if request.method == 'POST':
        new_price = int(request.POST.get('price'))
        try:
            product = models.Product.objects.get(id=product_id)
            current_date = datetime.now().date()
            product_price = models.ProductPriceHistory.objects.get(product=product,date=current_date)
            product_price.price = new_price
            product_price.save()
            return HttpResponse("Product Price updated")
        except ObjectDoesNotExist:
            return HttpResponseNotFound()
    else:
        return HttpResponseBadRequest() 
        

def last_month_product_pricing(request,product_id):
    try:
        product = models.Product.objects.get(id=product_id)
        price_history = models.ProductPriceHistory.objects.filter(product=product)
        start_date = datetime.now() - timedelta(weeks=4)
        price_history = price_history.filter(date__gte=start_date)
        price_history_list = []
        for ph in price_history:
            price_detail = {'date':str(ph.date),'price':ph.price}
            price_history_list.append(price_detail)

        price_list_data = json.dumps({'price_history_list':price_history_list})
        return HttpResponse(price_list_data)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
