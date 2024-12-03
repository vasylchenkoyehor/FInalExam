#!/usr/bin/env python3
import cgi

gifts = [
    "Book", "Toy", "Gadget", "Video Game", "Headphones", 
    "Smartphone", "Laptop", "Watch", "Shoes", "Wallet", 
    "Headset", "Camera", "Drone", "Smart Watch", "Bluetooth Speaker"
]

def calculate_gift_code(selected_indices):
    gift_code = 0
    for index in selected_indices:
        gift_code |= (1 << index)  
    return gift_code

def handle_form_submission():
    form = cgi.FieldStorage()
    
    selected_gifts_str = form.getvalue("gifts", "")
    
    selected_indices = [int(x) for x in selected_gifts_str.split(",") if x.strip().isdigit()]
    
    gift_code = calculate_gift_code(selected_indices)
    
    selected_gifts = [gifts[index] for index in selected_indices]
    
    html_output = f"""
    <html>
    <head><title>Gift Selector Result</title></head>
    <body>
        <h1>Selected Gifts</h1>
        <p>Selected Gifts: {', '.join(selected_gifts)}</p>
        <p>Unique Gift Code: {gift_code}</p>
    </body>
    </html>
    """
    
    return html_output

if __name__ == "__main__":
    print("Content-Type: text/html")
    print()
    print(handle_form_submission())
