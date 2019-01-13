import json
import requests

total_orders = -1
fetched_orders = 0
last_order_id = ''
total_order_amt = 0
delivered_orders = 0

cookies = {
    #swiggy cookies
}

headers = {
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    '__fetch_req__': 'true',
    'Accept-Language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'Referer': 'https://www.swiggy.com/my-account',
    'Connection': 'keep-alive',
}


while(total_orders == -1 or fetched_orders < total_orders-1):
    params = (
        ('order_id', last_order_id),
    )

    response = requests.get('https://www.swiggy.com/dapi/order/all', headers=headers,
                            params=params, cookies=cookies)


    data = json.loads(response.text)

    if data["statusCode"] != 0:
        print data["statusMessage"]
        exit()
    # print data;
    if total_orders == -1:
        total_orders = data["data"]["total_orders"]
    current_orders = data["data"]["orders"]
    fetched_orders += len(current_orders)
    last_order_id = current_orders[-1]["order_id"]

    for order in current_orders:
        print order["order_id"], order["order_status"]
        if order["order_status"] == "Delivered":
            total_order_amt += order["order_total"]
            delivered_orders += 1

    print last_order_id
    print fetched_orders

print total_order_amt
print delivered_orders
