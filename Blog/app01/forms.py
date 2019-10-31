from django.forms import ModelForm
from . import models
from django import forms

''' 自己刻 後來失敗ＸＤ
# class DateInput(forms.widgets.DateInput):
#     input_type = 'date'

    # def get_context(self, name, value, attrs):
    #     context = super().get_context(name, value, attrs)
    #     context['widget'].update( {
    #         'value': '2019/09/09',
    #
    #     })
    #     return context

'''


class ShopForm(ModelForm):

    # name = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'style': 'color',
    #     : blue', 'data-id': 'adskjkjdsndas'}),
    #     label='店家名稱')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.Shop
        fields = '__all__'


class OrderForm(ModelForm):
    # release_date = forms.DateField()

    def clean_release_date(self):
        obj = self.cleaned_data.get("release_date")
        return obj

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields.frelease_date.widget.render('name','2019/09/09')

    class Meta:
        model = models.Order
        fields = '__all__'


class OrderdetailForm(ModelForm):

    # number = forms.ChoiceField(forms.Select(choices=models.Orderdetail.objects.filter(id=1)))

    def __init__(self, pk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(pk)
        print(self)
        # self.number = forms.ModelChoiceField(queryset=models.Orderdetail.objects.filter(id=pk))
        # obj = self.fields.get('number')
        # obj.queryset = obj.queryset.filter(id=pk)
        # self.fields.update({'number': obj})

        o = OrderdetailForm.objects.get('number')


    class Meta:
        model = models.Orderdetail
        fields = '__all__'


class MenuForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Orderitem
        fields = '__all__'
