from django.db import models

from products.models import Product

from django.contrib.auth import get_user_model
User = get_user_model()


class Order(models.Model):
    KUTILMOQDA = 'KUTILMOQDA'
    TAYYORLANMOQDA = 'TAYYORLANMOQDA'
    KURYERDA = 'KURYERDA'
    YETKAZILDI = 'YETKAZILDI'
    BEKORQILINDI = 'BEKORQILINDI'

    STATUS_CHOICES = [
        (KUTILMOQDA, 'KUTILMOQDA'),
        (TAYYORLANMOQDA, 'TAYYORLANMOQDA'),
        (KURYERDA, 'KURYERDA'),
        (YETKAZILDI, 'YETKAZILDI'),
        (BEKORQILINDI, 'BEKORQILINDI')
    ]

    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cafe = models.ForeignKey('Cafe', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=KUTILMOQDA)


# buryurtma statusini tekshirish
    def set_status(self, new_status):
        valid_statuses = [choice[0] for choice in self.STATUS_CHOICES]
        if new_status not in valid_statuses:
            raise ValueError('Invalid status')
        self.status = new_status
        self.save()

# to'g'ri tranzaksiya qilish
    def is_transitions(self, new_status):
        allowed_transitions ={
            self.KUTILMOQDA: [self.TAYYORLANMOQDA, self.BEKORQILINDI],
            self.TAYYORLANMOQDA:  [self.KURYERDA],
            self.KURYERDA: [self.YETKAZILDI]
        }
        return new_status in allowed_transitions.get(self.status, []) or []

    def calculate_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()  # Narxni yangilaymiz
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} by  {self.customer.username}"


class OrderItem(models.Model): #Zakas tarkibi
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


