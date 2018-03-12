from django import form

class question(forms.Form):
    content=models.CharField(max_length=512)
    options1=models.CharField(max_length=51)
    options2=models.CharField(max_length=51)
    options3=models.CharField(max_length=51)
    options4=models.CharField(max_length=51)
  
class Answer(forms.Form):
    options1=models.CharField(max_length=51)
    options2=models.CharField(max_length=51)
    options3=models.CharField(max_length=51)
    options4=models.CharField(max_length=51)

  
