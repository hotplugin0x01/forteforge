from django.forms import ModelForm
from django import forms
from .models import Student, User, Enterprise


# Create the form class.
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
    
    def save(self, commit=False):
        user = User.objects.create(
            username = self.cleaned_data["email"].split('@')[0],
            first_name = self.cleaned_data["first_name"],
            last_name = self.cleaned_data["last_name"],
            email = self.cleaned_data["email"],
            password = self.cleaned_data["email"],
        )

        return user

class ProfileForm(ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['dob', 'postal_code', 'street_name', 'city', 'state', 'country', 'portfolio']
    def save(self, user, commit=False):
        student = Student.objects.create(
            user = user,
            dob = self.cleaned_data["dob"],
            postal_code = self.cleaned_data["postal_code"],
            street_name = self.cleaned_data["street_name"],
            city = self.cleaned_data["city"],
            state = self.cleaned_data["state"],
            country = self.cleaned_data["country"],
            portfolio = self.cleaned_data["portfolio"]
        )
        return student

class EnterpriseForm(ModelForm):
    req_choices = [('Tasks','Task'),('Projects','Projects'),('Operations', 'Operations')]
    requirement = forms.CharField(label='Requirement', required=False, widget=forms.RadioSelect(choices=req_choices))

    type_choices = [('Interns','Interns'),('Apprentices','Apprentices'),('Expert', 'Expert')]
    type = forms.CharField(label='Type',required=False, widget=forms.RadioSelect(choices=type_choices))

    freq_choices = [('1 off','1 off'),('Projects','Projects'),('Operations', 'Operations')]
    frequency = forms.CharField(label='Frequenct',required=False, widget=forms.RadioSelect(choices=freq_choices))

    facilitation_choices = [('Events','Events'),('Webiner','Webiner'),('Proof of Concept','Proof of Concept'),('Classes', 'Classes')]
    facilitation = forms.CharField(label='Facilitation',required=False, widget=forms.RadioSelect(choices=facilitation_choices))

    attendance_choices = [('Events','Events'),('Webiner','Webiner'),('Proof of Concept Classes', 'Proof of Concept Classes')]
    attendance = forms.CharField(label='Attendance',required=False, widget=forms.RadioSelect(choices=attendance_choices))
    class Meta:
        model = Enterprise
        # fields = '__all__'
        fields = ['requirement_deadline','company_name','title','function','work_email','postal_code', 'street_name', 'city', 'state', 'country']

    def save(self, user, commit=False):
        enterprise = Enterprise.objects.create(
            user = user,
            company_name = self.cleaned_data["company_name"],
            title = self.cleaned_data["title"],
            function = self.cleaned_data["function"],
            work_email = self.cleaned_data["work_email"],
            postal_code = self.cleaned_data["postal_code"],
            street_name = self.cleaned_data["street_name"],
            city = self.cleaned_data["city"],
            state = self.cleaned_data["state"],
            country = self.cleaned_data["country"],
            requirement = self.cleaned_data["requirement"],
            type = self.cleaned_data["type"],
            frequency = self.cleaned_data["frequency"],
            requirement_deadline = self.cleaned_data["requirement_deadline"],
            facilitation = self.cleaned_data["facilitation"],
            attendance = self.cleaned_data["attendance"]
        )
        return enterprise