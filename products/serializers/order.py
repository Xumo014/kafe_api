from rest_framework import serializers
from products.models import Order, OrderItem, Product, Cafe


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True) #Zakas ichidagi mahsulotlar
    cafe = serializers.PrimaryKeyRelatedField(queryset=Cafe.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'customer', 'total_price', 'status', 'cafe', 'created_at', 'items']

    def create(self, validated_data):
        request = self.context.get('request')
        customer = request.user



        items_data = validated_data.pop('items')
        cafe = validated_data.pop('cafe')

        order = Order.objects.create(customer=customer, cafe=cafe)

        total_price = 0
        order_items = []

        for item in items_data:
            product = item['product']
            quantity = item['quantity']
            price = product.price * quantity  #Narxni hisoblaymiz

            order_items.append(OrderItem(product=product, quantity=quantity, price=price))
            total_price += price #umumiy narxni hisoblash

        OrderItem.objects.bulk_create(order_items)
        order.total_price = total_price
        order.save()

        return order