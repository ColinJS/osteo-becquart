from django.db import models


class Picture(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    url = models.URLField(max_length=300)
    state = models.BooleanField(default= True)
    order = models.SmallIntegerField(default=0) # Not null, unique, auto_order

    def change_order_all(self, new_order):
        all_objects = Picture.objects.exclude(pk=self.pk).order_by('order')
        i = 0
        for obj in all_objects:
            if i == new_order:
                i += 1
            obj.order = i
            obj.save(False)
            i += 1

    def save(self, order_check=True, *args, **kwargs):
        if order_check:
            old = Picture.objects.filter(pk=self.pk).first()
            if old and old.order != self.order:
                objects_count = Picture.objects.all().count()
                if self.order >= objects_count:
                    self.order = objects_count-1
                self.change_order_all(self.order)
        super().save()

        class Meta:
            ordering = ["order"]

