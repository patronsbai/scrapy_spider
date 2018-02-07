import urllib.request

def load_data():

    URL = "http://www.baidu.com"
    response = urllib.request.urlopen(URL)
    data = response.read()

    # print(data)
    return data   #返回的是byte

def write_data(data):
    with open("03baidu.html", "w") as f:
        f.write(data)

if __name__ == '__main__':

    data = load_data()
    decode_data = data.decode()   #转化成unicode
    write_data((decode_data))




