from web3 import Web3
import json

class TransactionService:
    def setup_blockchain_connection(self):
        global current_acc, web3
        url = "HTTP://127.0.0.1:7545"
        web3 = Web3(Web3.HTTPProvider(url))
        
        
        current_acc = web3.eth.accounts[0]
        web3.eth.defaultAccount = current_acc  

    def setup_contract(self,current_link):
        global current_user, contract
        current_user = current_link

        if current_user == "producer":
            abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"id","type":"uint16"},{"indexed":false,"internalType":"string","name":"data","type":"string"}],"name":"ProducerEvent","type":"event"},{"constant":false,"inputs":[{"internalType":"uint16","name":"_prodId","type":"uint16"},{"internalType":"string","name":"_data","type":"string"}],"name":"addProducer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"uint16","name":"_prodId","type":"uint16"}],"name":"getTransactionByProdId","outputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"producersAccts","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]')
            address = "0x89ADCA33c8a0334DAA1e61Dd28819d47f929497B"
        elif current_user == "shipper":
            abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"id","type":"uint16"},{"indexed":false,"internalType":"string","name":"data","type":"string"}],"name":"ShipperEvent","type":"event"},{"constant":false,"inputs":[{"internalType":"uint16","name":"_id","type":"uint16"},{"internalType":"string","name":"_data","type":"string"}],"name":"addShipper","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint16","name":"_id","type":"uint16"}],"name":"getShipper","outputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"shippersAccts","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"payable":false,"stateMutability":"view","type":"function"}]')
            address = "0x7067eF7CA3259E4D6741993489439A5c94A950dE"
        elif current_user == "wholesaler":
            abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"id","type":"uint16"},{"indexed":false,"internalType":"string","name":"data","type":"string"}],"name":"WholesalerEvent","type":"event"},{"constant":false,"inputs":[{"internalType":"uint16","name":"_id","type":"uint16"},{"internalType":"string","name":"_data","type":"string"}],"name":"addWholesaler","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint16","name":"_id","type":"uint16"}],"name":"getWholesaler","outputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"wholesalersAccts","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"payable":false,"stateMutability":"view","type":"function"}]')
            address = "0x1Fd9E44282399FADB7449eb4709e3F5F3a735C47"
        elif current_user == "detailer":
            abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"id","type":"uint16"},{"indexed":false,"internalType":"string","name":"data","type":"string"}],"name":"DetailerrEvent","type":"event"},{"constant":false,"inputs":[{"internalType":"uint16","name":"_id","type":"uint16"},{"internalType":"string","name":"_data","type":"string"}],"name":"addDetailer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"detailersAccts","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint16","name":"_id","type":"uint16"}],"name":"getDetailer","outputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')
            address = "0xd5506A5c6A9711093F1d25291099DFe80369Cd39"

        contract = web3.eth.contract(abi = abi, address = address)

    def add_link(self,form):
        #wait until Solidity will alllow passing and returing structs
        if current_user == "producer":
            return contract.functions.addProducer(form.cleaned_data.get("product_id"),form.cleaned_data.get("common_name")).transact()
        elif current_user == "shipper":
            return contract.functions.add_link(form.cleaned_data.get("product_id"),form.cleaned_data.get("common_name")).transact()
        elif current_user == "wholesaler":
            return contract.functions.add_link(form.cleaned_data.get("product_id"),form.cleaned_data.get("common_name")).transact()
        elif current_user == "detailer":
            return contract.functions.add_link(form.cleaned_data.get("product_id"),form.cleaned_data.get("common_name")).transact()

    def get_link_by_id(self,id):
        return contract.functions.getTransactionByProdId(current_acc,int(id)).call()
            

         