from django import forms
from .models import team_table
from pokewiki.models import f_table, s_table, a_table, a_relation, m_table, m_relation
# from pokewiki.models import p_table


class teamform(forms.ModelForm):

    class Meta:
        model = team_table
        fields = ('team_name', 'description', 'team_comp')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['p1'].queryset = f_table.objects.all()
        self.fields['p2'].queryset = f_table.objects.none()
        self.fields['p3'].queryset = f_table.objects.none()
        self.fields['p4'].queryset = f_table.objects.none()
        self.fields['p5'].queryset = f_table.objects.none()
        self.fields['p6'].queryset = f_table.objects.none()

    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    team_comp = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40, 'style':"display:none;"}))
    p1 = forms.CharField()
    p2 = forms.CharField()
    p3 = forms.CharField()
    p4 = forms.CharField()
    p5 = forms.CharField()
    p6 = forms.CharField()
