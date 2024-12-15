from main import client
from parsing import parser


def test_iperf(server_ip = "192.168.0.73"):

    result, error = client(server_ip)

    if error:
        print("Помилка:", error)
        return

    result_list = parser(result)

    for value in result_list:
        if value['Transfer'] > 2 and value['Bitrate'] > 20:
            print(value)
