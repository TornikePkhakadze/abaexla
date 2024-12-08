from django.db.models import Sum,Max,Min,Avg,Count
from django.core.management.base import BaseCommand, CommandError
from shop.models import Category, Item,  Tag


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
# AGGREGATE----------------------------------------------------------------------------------------------------
        # categories = Category.objects.filter(name__iexact="food word").aggregate(item_count=Count('items'))
        # print(categories)
# ----------------------------------------------------------------------------------------------------
        # products = Category.objects.aggregate(
        #     Max("items__price"),
        #     Min("items__price"),
        #     Avg("items__price")
        # )
        # print(products)
# ANNOTATE-----------------------------------------------------------------------------------------------------
        # categories=Category.objects.annotate(items_count=Count("items"))
        # for category in categories:
        #     print(f"{category.name} : {category.items_count}")
# ----------------------------------------------------------------------------------------------------
        # categories = Category.objects.annotate(items_price = Sum("items__price"))
        # for category in categories:
        #     print(f"{category.items_price}")
# SELECT_RELATED------------------------------------------------------------------------------------------------
        # e = Item.objects.select_related("category").all()
        # print(e)
#-----------------------------------------------------------------------------------------------------
        # e = Item.objects.select_related("category").all()
        # for helper in e:
        #     print(helper.name)
#PREFEATCH_RELATED----------------------------------------------------------------------------------------------
        # e = Item.objects.prefetch_related("tags").all() 
        # for item in e:  
        #         for tag in item.tags.all():  
        #                 print(f"{item.name}:{tag.name}")  
