def calculate_total(price, tax_rate=0.25):
    """
    Calculate the total price including tax.
    """
    # MISTAKE: Yaha tax add karna bhool gaye hain. 
    # Function simply wahi price return kar raha hai.
    # Correct code should be: return price + (price * tax_rate)
    return float(price)
