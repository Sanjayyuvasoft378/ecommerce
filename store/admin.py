from django.contrib import admin

from store.models import Brand, Color, Discount, Gender, Hotel, Offer, Product, Size, Slider, Staff, SubCategory, User, mainCategory



admin.site.register(Hotel)
admin.site.register(mainCategory)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Offer)
admin.site.register(Discount)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Gender)
admin.site.register(Brand)
admin.site.register(Slider)
admin.site.register(Staff)