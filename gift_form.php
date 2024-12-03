<!DOCTYPE html>
<html>
    <head>
        <title>Gift Selection Form</title>
    </head>
    <body>
        <h1>Select Gifts</h1>
        <form action="gift_selector.py" method="get">
            <label>Select gifts:</label><br>
            <select name="gifts" multiple size="10">
                <option value="0">Book</option>
                <option value="1">Toy</option>
                <option value="2">Gadget</option>
                <option value="3">Video Game</option>
                <option value="4">Headphones</option>
                <option value="5">Smartphone</option>
                <option value="6">Laptop</option>
                <option value="7">Watch</option>
                <option value="8">Shoes</option>
                <option value="9">Wallet</option>
                <option value="10">Headset</option>
                <option value="11">Camera</option>
                <option value="12">Drone</option>
                <option value="13">Smart Watch</option>
                <option value="14">Bluetooth Speaker</option>
            </select><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
