from django.shortcuts import render,redirect
from .forms import ProducerForm,ShipperForm,DetailerForm,WholesalerForm,LinksMultiForm
from .models import ProducerModel,ShipperModel,DetailerModel,WholesalerModel
from django.contrib import messages
from rest_framework import generics,mixins
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.views import APIView
from django.db import models

from .services import TransactionService
from django.contrib.auth.decorators import login_required


tx_service = TransactionService()


def home(request):

    return render(request,'blockchain/home.html')
@login_required
def add_product(request):
    current_link = request.user.widget.lower()
    tx_service.setup_blockchain_connection()

    if request.method == 'POST':
        form_class = LinksMultiForm(request.POST)
        form_for_link= form_class[current_link]
        print(form_class.is_valid())
        if form_for_link.is_valid():
            tx_service.add_link(form_for_link)
            form_for_link.save(commit=False)
            print("Form posted correctly!")
            print("Index: ",form_for_link.cleaned_data.get("product_id"))
            print("Common name: ", form_for_link.cleaned_data.get("common_name"))
            messages.success(request, 'You posted a form successfully')
            return redirect('blockchain-home')
    else:
        form_class = LinksMultiForm()
        form_for_link= form_class[current_link]

        producer_fields = list(ProducerForm.base_fields)
        shiper_fields = list(ShipperForm.base_fields)
        wholesaler_fields = list(WholesalerForm.base_fields)
        detailer_fields = list(DetailerForm.base_fields)

        request.session['prodcer_fields'] = producer_fields
        request.session['shiper_fields'] = shiper_fields
        request.session['wholesaler_fields'] = wholesaler_fields
        request.session['detailer_fields'] = detailer_fields


    return render(request,'blockchain/add_product.html',{'form': form_for_link})

def about(request):
    return render(request,'blockchain/about.html',{'title':'About'})

def enter_prod_id(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        received_info = tx_service.get_link_by_id(product_id)

        print("Received product id: {}".format(received_info))
        request.session['tracked_product_id'] = received_info
        #request.session['tracked_product_data'] = get_data

        return redirect('/tracking')
    
    return render(request, 'blockchain/enter_prod_id.html')
    
def tracking(request):
    received_info = request.session['tracked_product_id']
    producer_fields= dict(zip(request.session['prodcer_fields'],received_info))

    print(producer_fields)
    shiper_fields = request.session['shiper_fields']
    wholesaler_fields = request.session['wholesaler_fields']
    detailer_fields = request.session['detailer_fields']
    
    tracked_product = {
        'producer_fields': producer_fields,
        'shiper_fields': shiper_fields,
        'wholesaler_fields': wholesaler_fields,
        'detailer_fields': detailer_fields,
    }
    return render(request, 'blockchain/tracking.html', context = tracked_product)
  
