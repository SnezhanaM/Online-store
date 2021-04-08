from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError
from .models import *

from PIL import Image


class SmartphoneAdminForm(ModelForm):

    VALID_RESOLUTION = (400, 400)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Минимальное разрешение изображения: {}x{}'.format(*self.VALID_RESOLUTION)

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = self.VALID_RESOLUTION
        if img.width < min_width or img.height < min_height:
            raise ValidationError('Разрешение загруженного изображения меньше минимального')
        return image


class SmartphoneAdmin(admin.ModelAdmin):

    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AudioAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='audio'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
