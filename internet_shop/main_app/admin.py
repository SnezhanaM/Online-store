from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.utils.safestring import mark_safe

from .models import *

from PIL import Image


class SmartphoneAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe("""<span style="color:red; font-size:14px;">Минимальное разрешение изображения: {}x{}</span>""".format(*Product.MIN_RESOLUTION))

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер загруженного изображения не должен превышать 3 Мб')
        if img.width < min_width or img.height < min_height:
            raise ValidationError('Разрешение загруженного изображения меньше минимального')
        if img.width > max_width or img.height > max_height:
            raise ValidationError('Разрешение загруженного изображения больше максимального')
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
admin.site.register(Order)
