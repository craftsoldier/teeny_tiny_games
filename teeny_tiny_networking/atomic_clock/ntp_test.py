import ntplib
from time import ctime

def get_network_time():
    ntp_client = ntplib.NTPClient()
    ntp_server = 'time.nist.gov'

    try:
        response = ntp_client.request(ntp_server, version=3)
        network_time = ctime(response.tx_time)
        print(response.offset)
        print(response.delay)
        print(network_time)
    except Exception as e:
        print(f"didn't work: {e}")

get_network_time()


