def validorder(order):
    invoiced = Decimal('0')
    received = Decimal('0')
    maxDecimal = 99999999999

    for item in order.items:
        if item.type == 'payment':
            if abs(item.amount) >= maxDecimal:
                return "maxDecimal reached for payment %s" % item.description
            else:
                received += Decimal(str(item.amount))
            if received >= maxDecimal:
                return "maxDecimal reached for received"
        elif item.type == 'product':
            if abs(item.amount) >= maxDecimal:
                return "maxDecimal reached for product %s" % item.description
            elif item.quantity != int(item.quantity):
                return "non-integer quantity for product %s" % item.description
            elif abs(item.amount) * abs(item.quantity) >= maxDecimal:
                return "maxDecimal reached for product %s" % item.description
            else:
                invoiced += Decimal(str(item.amount)) * Decimal(str(item.quantity))
            if invoiced > maxDecimal:
                return "maxDecimal exceeded for total invoiced"
        else:
            return "Invalid item type: %s" % item.type

    if invoiced == received:
        return "Order ID: %s - Full payment received!" % order.id
    else:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, received - invoiced)
