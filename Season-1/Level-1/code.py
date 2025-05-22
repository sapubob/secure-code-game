def validorder(order):
    invoiced = Decimal('0')
    received = Decimal('0')
    maxDecimal = 99999999999

    for item in order.items:
        if item.type == 'payment':
            received += Decimal(str(item.amount))
            if received >= maxDecimal:
                return "maxDecimal exceeded for total received"
        elif item.type == 'product':
            if item.quantity != int(item.quantity):
                return "non-integer quantity for product %s" % item.description
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
validorder
