from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Campaign(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="campaigns",
                                verbose_name="Рекламируемая услуга")
    channel = models.CharField(max_length=255, verbose_name="Канал продвижения")
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Бюджет")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рекламная кампания"
        verbose_name_plural = "Рекламные кампании"


class Lead(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Ф.И.О.")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True, related_name="leads",
                                 verbose_name="Рекламная кампания")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Потенциальный клиент"
        verbose_name_plural = "Потенциальные клиенты"


class Contract(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="contracts",
                                verbose_name="Предоставляемая услуга")
    document = models.FileField(upload_to='contracts/', verbose_name="Файл с документом")
    date_signed = models.DateField(verbose_name="Дата заключения")
    duration = models.CharField(max_length=100, verbose_name="Период действия")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"


class ActiveClient(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, related_name="active_client",
                                verbose_name="Потенциальный клиент")
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name="active_client",
                                    verbose_name="Контракт")

    def __str__(self):
        return f"Активный клиент: {self.lead.full_name}"

    class Meta:
        verbose_name = "Активный клиент"
        verbose_name_plural = "Активные клиенты"



from django.db import models

# Create your models here.
