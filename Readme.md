Hello, This Project is made to report a suspicious bug to Django.

In the admin page the Column will dupulicate.

Config
```py
# models.py
class Parts(models.Model):
    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'

    part_id = models.UUIDField(verbose_name='PartID', primary_key=True, unique=True, default=uuid.uuid4, max_length=40)
    part_name = models.CharField(verbose_name='PartName', unique=False, default=1, max_length=40, blank=True, null=True)

    def __str__(self):
        return self.part_name

# admin.py
list_editable = 'Primary_key=True Field'
```
This is the screenshot for it
<img width="1585" alt="スクリーンショット 2021-05-07 18 54 46" src="https://user-images.githubusercontent.com/66260097/117432937-e0065080-af65-11eb-9f69-a3046ee579e4.png">
