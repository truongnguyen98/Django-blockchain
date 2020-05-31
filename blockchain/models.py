from django.db import models
from hashlib import sha256
import datetime
import logging
import pytz
from django.urls import reverse
#from .utils import SymmetricEncryption, JsonApi, EncryptionApi

class Block(models.Model):
   
    time_stamp = models.DateTimeField(auto_now_add=False)
    index = models.IntegerField(auto_created=True, blank=True)
    data = models.TextField(blank=True, max_length=255)
    hash = models.CharField(max_length=255, blank=True)
    previous_hash = models.CharField(max_length=255)
    #chain = models.ForeignKey(to='Chain', on_delete=models.CASCADE)
    nonce = models.CharField(max_length=255, default=0, blank=True)

    def __str__(self):
        return "Block " + str(self.index) #+ " on " + self.chain.name

    def __repr__(self):
        return '{}: {}'.format(self.index, str(self.hash)[:6])

    def __hash__(self):
        return sha256(
            u'{}{}{}{}'.format(
                self.index,
                self.data,
                self.previous_hash,
                self.nonce).encode('utf-8')).hexdigest()

    @staticmethod
    def generate_next(latest_block, data):
        block = Block(
            data=data,
            index=latest_block.index + 1,
            time_stamp=datetime.datetime.now(tz=pytz.utc),
            previous_hash=latest_block.hash,
            nonce=SymmetricEncryption.generate_salt(26),
        )
        while not block.valid_hash():
            block.nonce = SymmetricEncryption.generate_salt(26)
        block.hash = block.__hash__()

        # block.save()                # todo: remove

        return block

    def is_valid_block(self, previous_block):
        if self.index != previous_block.index + 1:
            log.warning('%s: Invalid index: %s and %s' % (self.index, self.index, previous_block.index))
            return False
        if self.previous_hash != previous_block.hash:
            log.warning('%s: Invalid previous hash: %s and %s' % (self.index, self.hash, previous_block.hash))
            return False

        if self.__hash__() != self.hash and self.index > 1:
            log.warning('%s: Invalid hash of content: %s and %s' % (self.index, self.hash, self.__hash__()))
            return False
        if not self.valid_hash() and self.index > 1:
            log.warning('%s: Invalid hash value: %s' % (self.index, self.hash))
            return False
        return True

    def valid_hash(self):
        return self.__hash__()[:4] == '0000'

class Transaction (models.Model):
    index = models.IntegerField(auto_created=True, blank=True)
    common_name= models.TextField(blank=True, max_length=255)
   # date = models.DateField
    #region = models.TextField(blank=True, max_length=100)
    #country = models.TextField(blank=True, max_length=50)
    ##company = models.TextField(blank=True, max_length=255)
   # amount = models.TextField(blank=True, max_length=50)
    #file = models.FileField

    def __str__(self):
        return "Transaction " + str(self.index)
