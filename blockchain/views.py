from django.shortcuts import render,redirect
from .forms import ProducerForm,ShipperForm,DetailerForm,WholesalerForm
from .models import Transaction
from django.contrib import messages
from rest_framework import generics,mixins
from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import BlockSerializer
from rest_framework.views import APIView
from django.db import models
from web3 import Web3
import json




url = "HTTP://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(url))
abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"id","type":"uint16"},{"indexed":false,"internalType":"string","name":"data","type":"string"}],"name":"ProducerEvent","type":"event"},{"constant":false,"inputs":[{"internalType":"string","name":"_data","type":"string"}],"name":"addProducer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint16","name":"_id","type":"uint16"}],"name":"getProducer","outputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')
address = "0x6C8612bE27Bc03c3146ccb9f3FF3e953e382eE56"
contract = web3.eth.contract(abi = abi, address = address)
web3.eth.defaultAccount = web3.eth.accounts[0]


def home(request):
    if request.method == 'POST':
        if request.user.widget == "producer":
            form = ProducerForm(data=request.POST)
        elif request.user.widget == "shipper":
            form = ShipperForm(data=request.POST)
        elif request.user.widget == "wholesaler":
            form = WholesalerForm(data=request.POST)
        elif request.user.widget == "detailer":
            form = DetailerForm(data=request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            contract.functions.addProducer(form.cleaned_data.get("common_name")).transact()

            print("Form posted correctly!")
            print("Index: ",form.cleaned_data.get("index"))
            print("Common name: ", form.cleaned_data.get("common_name"))
            messages.success(request, 'You posted a form successfully')
            return redirect('blockchain-home')

    else:
        if request.user.widget == "producer":
            form = ProducerForm()
        elif request.user.widget == "shipper":
            form = ShipperForm()
        elif request.user.widget == "wholesaler":
            form = WholesalerForm()
        elif request.user.widget == "detailer":
            form = DetailerForm()


    return render(request,'blockchain/home.html',{'form': form})

def about(request):
    return render(request,'blockchain/about.html',{'title':'About'})
    

     



