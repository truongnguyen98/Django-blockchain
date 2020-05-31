from django.shortcuts import render,redirect
from .forms import TransactionForm
from django.contrib import messages
from rest_framework import generics,mixins
from rest_framework import CreateAPIView
from .serializers import BlockSerializer
from rest_framework.views import APIView



def home(request):

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            print("Form posted correctly!")
            print("Index: ",form.cleaned_data.get("index"))
            print("Common name: ", form.cleaned_data.get("common_name"))
            messages.success(request, 'You posted a form successfully')
            return redirect('blockchain-home')

    else:
        form = TransactionForm()

    return render(request,'blockchain/home.html',{'form': form})

def about(request):
    return render(request,'blockchain/about.html',{'title':'About'})

class BlockCreateView(generics.CreateAPIView):
     serializer_class = BlockSerializer
     



