import http.client
import json

def youp(sheet, start, end, count):
    conn = http.client.HTTPSConnection("www.xiaomiyoupin.com")
    for i in range(start, end):
        payload = "{\"groupName\":\"details\",\"groupParams\":[[\"" + str(i) + "\"]],\"methods\":[],\"version\":\"1.0.0\",\"debug\":false,\"channel\":\"\"}"
        headers = {
          'Content-Type': 'application/json'
        }
        conn.request("POST", "/api/gateway/detail", payload, headers)
        res = conn.getresponse()
        data = res.read()
        json_re = data.decode("utf-8")
        json_str = json.loads(json_re)
        if json_str["message"] == "ok":
            data = json_str["data"]
            goods = data["goods"]
            goods_info = goods["goodsInfo"]
            name = goods_info["name"]
            sheet.write(count, 0, name)
            count = count + 1
            print(count)
    return count


