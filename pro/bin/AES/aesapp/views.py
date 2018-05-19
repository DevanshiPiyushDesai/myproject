from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView

import base64
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
from PIL import Image




class HomeView(TemplateView):

	template_																																																																																name="home.html"
	
	def get(self,request,*args,**kwargs):
		context=self.get_context_data(**kwargs)
		

		#print(AES.block_size)
		key=Random.new().read(AES.block_size)
		#print(key)

		iv=Random.new().read(AES.block_size)
		#print(iv)
		s="devanshi"
		#aes_cipher_obj=AES.new(key,AES.MODE_CFB,iv)
		#cipher=aes_cipher_obj.encrypt(s)
        	#print(cipher_text)
		#context['cipher']=cipher
		context['key']=key
		#context['s']=s

		return self.render_to_response(context)
	
