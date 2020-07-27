from django import forms

from .models import Bid, Item

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ('amount',)

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        try:
            item = Item.objects.get(pk=self.instance.pk)
            pamount = item.bid.clean_amount()
        except Item.DoesNotExist:
            # return hb
            raise forms.ValidationError("The item doesn't exist!")
        if not amount > pamount:
            raise forms.ValidationError("An equivalent or higher bet already exists!")
        else:
            item.bid.amount = amount
        return amount