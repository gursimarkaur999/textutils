# this file is created by Gursimar Kaur
from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def analyzetext(request):
    textString = request.POST.get('text') #video 17 get into post
    rempunc = request.POST.get('removepunc', 'off')
    uc = request.POST.get('uppercase', 'off')
    lc = request.POST.get('lowercase', 'off')
    cf = request.POST.get('capfirst', 'off')
    nlr = request.POST.get('newlineremove', 'off')
    sr = request.POST.get('spaceremove', 'off')
    esr = request.POST.get('extraspaceremove', 'off')
    cc = request.POST.get('charcount', 'off')
    punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
    if textString != "":
        analyzed = ""
        if rempunc == 'on':
            analyzed = ""
            for char in textString:
                if char not in punctuations:
                    analyzed = analyzed + char
            textString = analyzed

        if uc == 'on':
            analyzed = ""
            for char in textString:
                analyzed = analyzed + char.upper()
            textString = analyzed

        if lc == 'on':
            analyzed = ""
            if textString == "":
                textString = "No text entered."
            for char in textString:
                analyzed = analyzed + char.lower()
            textString = analyzed

        if cf == 'on':
            analyzed = ""
            for index, char in enumerate(textString):
                if index == 0:
                    analyzed = analyzed + char.upper()
                elif (textString[index-2] == '.' and textString[index-1] == ' ') or (textString[index-2] == '!' and textString[index-1] == ' ') or (textString[index-2] == '?' and textString[index-1] == ' '):
                    analyzed = analyzed + char.upper()
                else:
                    analyzed = analyzed + char
            textString = analyzed

        if nlr == 'on':
            analyzed = ""
            for char in textString:
                if char != '\n':
                    analyzed = analyzed + char
            textString = analyzed

        if sr == 'on':
            analyzed = ""
            for char in textString:
                if char != " ":
                    analyzed = analyzed + char
            textString = analyzed

        if esr == 'on':
            analyzed = ""
            for index, char in enumerate(textString):
                if not(textString[index] == " " and textString[index + 1] == " "):
                    analyzed = analyzed + char
            textString = analyzed

        if cc == 'on':
            analyzed = textString + "\n" + str(len(textString) - textString.count('\n'))

        if analyzed == "":
            return HttpResponse("Error")
        else:
            params = {'textString': analyzed}
    else:
        params = {'textString': 'No text entered'}
    return render(request, 'analyze.html', params)
