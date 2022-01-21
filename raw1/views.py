# custom filter

from django.http import HttpResponse
from django.shortcuts import render
from . import encoder

def index (request):
	params = {"var1":"hello"}
	return render (request,"index.html",params)
	#return HttpResponse("hello")

def decode (request):
	encoded_text_raw = request.GET.get("encoded",default="default")
	
	for a in encoder.codes:
		encoded_text_raw =encoded_text_raw.replace(encoder.codes[a],a)
	
	params = {"decoded_txt":encoded_text_raw}
	return render (request, "decode.html",params)

def encode (request):
	decoded_text_raw = request.GET.get("decoded",default="default")
	
	for a in encoder.codes:
		decoded_text_raw =decoded_text_raw.replace(a,encoder.codes[a])
	
	params = {"encoded_txt":decoded_text_raw}
	
	return render(request, "encode.html",params)