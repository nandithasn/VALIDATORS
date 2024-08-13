from typing import Any
from django import forms
def name_length(value):
    if len(value)<5:
        raise forms.ValidationError('name shud be more than 5 chracters')
#1.normal function:
# normal function used for validating the submitted data.we can validate only one input element at a time so we will give one argument
    
class StudentForm(forms.Form):
    sid=forms.IntegerField()
    sname=forms.CharField(max_length=100,validators=[name_length])
    sage=forms.IntegerField()
    semail=forms.EmailField()
    remail=forms.EmailField()
    bot=forms.CharField(widget=forms.HiddenInput,required=False)
    #forms.hiddeninput is used make the hide the element in frontend
    #by default for all elements required is True which make elements mandatory to make it non mandatory element
    #we will make required= False

    #we can create validators to validate the submitted data from the form by using 
    #1.normal function
    #2.form object class method

    #2.form object class method 
    # in this method we will have all the data of a form
    #there are two methods
        #1.clean method
            #this method is used to validate multiple data
            #this is a class method so it takes one mandatory argument self
        #2.clean_element:
            #this method is used for validating one element
            #for validating the data this method makes the value into None
            #the main purpose of clean_element is for bot catching



    def clean(self):
        em=self.cleaned_data['semail']
        rem=self.cleaned_data['remail']
        if em!=rem:
            raise forms.ValidationError('email is not matching')
    

    def clean_bot(self):
        BC=self.cleaned_data['bot']
        if len(BC)>0:
            raise forms.ValidationError('there is a bug')
