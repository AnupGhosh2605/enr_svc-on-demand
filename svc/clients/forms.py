from django import forms
from accounts.models import TopicList, TopicDetailList, AssetsDetailList, ReviewList

class JobPostForm(forms.ModelForm):

    class Meta:
        model = TopicList
        fields = '__all__'  # ('TopicName',)
        exclude = ('UpdatedDate', 'CloseDate', 'User', 'ForceCloseReason', 'SMSText', 'WhatsAppText', 'CloseBy_id', 'ForceCloseCategory', 'UpdatedBy', 'AddedBy', 'CloseBy', 'IsClose', 'IsActive')

class JobUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobUpdateForm, self).__init__(*args, **kwargs)
        self.fields['ForceCloseReason'].required = False
        self.fields['ForceCloseCategory'].required = False
        self.fields['Category'].required = False
        self.fields['SubCategory'].required = False
        self.fields['IsActive'].required = False
        self.fields['IsClose'].required = False
        self.fields['CloseBy'].required = False
        self.fields['IsNotification'].required = False
        self.fields['SMSText'].required = False
        self.fields['WhatsAppText'].required = False

    class Meta:
        model = TopicList
        fields = '__all__'
        exclude = ('UpdatedDate', 'CloseDate', 'User', 'ForceCloseReason', 'CloseBy_id', 'ForceCloseCategory', 'AddedBy', 'UpdatedBy', 'CloseBy', 'IsActive')


class AssetsForm(forms.ModelForm):
    class Meta:
        model = AssetsDetailList
        fields = ['FileName']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewList
        fields = '__all__'