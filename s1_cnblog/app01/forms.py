from .models import *
from django.forms import widgets
from django.core.exceptions import NON_FIELD_ERRORS,ValidationError
from django import forms


class RegisterForm(forms.Form):
    user = forms.CharField(min_length=5,
                           error_messages={"required":"用户名不能为空"
                                        },
                           widget=widgets.TextInput(attrs={"class":"form-control","placeholder":"用户名"}))

    pwd = forms.CharField(min_length=8,
                           error_messages={"required": "不能为空",
                                           },
                          widget=widgets.PasswordInput(attrs={"class":"form-control","placeholder":"密码"}))

    repeat_pwd = forms.CharField(min_length=8,

                           error_messages={"required": "不能为空",
                                            },
                                 widget=widgets.PasswordInput(attrs={"class":"form-control","placeholder":"确认密码"}))

    email = forms.EmailField(
                                 error_messages={"required": "不能为空",
                                                 "invalid":"格式错误"
                                                 },
                                widget=widgets.EmailInput(attrs={"class":"form-control","placeholder":"邮箱"}))


    def clean_user(self):

        val = self.cleaned_data.get("user")             #cleaned_data
        user =  UserInfo.objects.filter(username=val)
        if not user:
            return val
        else:

            raise ValidationError("用户已存在!")

    def clean(self):
        pwd = self.cleaned_data.get("pwd")
        repeat_pwd = self.cleaned_data.get("repeat_pwd")
        if pwd and repeat_pwd:
            if pwd == repeat_pwd:
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致")
        else:
            return self.cleaned_data