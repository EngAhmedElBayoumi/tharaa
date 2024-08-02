#import render
from django.shortcuts import render



def render_to_pdf(request,template_src, context_dict):
    return render(request,template_src, context_dict)