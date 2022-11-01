import requests
import json



phrases = ['BTC-CLP', 'BTC-COP', 'BTC-USDC', 'USDC-ARS',
           'USDC-PEN', 'USDC-COP', 'USDC-CLP', 'LTC-ARS', 'LTC-PEN',
           'LTC-COP', 'LTC-CLP', 'LTC-BTC', 'BCH-ARS', 'ETH-ARS', 'BTC-ARS',
           'BCH-PEN', 'BCH-COP', 'BCH-CLP', 'BCH-BTC', 'ETH-COP', 'ETH-PEN',
           'BTC-PEN', 'ETH-BTC', 'ETH-CLP']


def main():
    var_boolean = True
    while var_boolean:
        i = input('Write the option do you want to get [HELP/help] / [Money in bitcoin]:').upper()
        raw = []
        try:
            if i in phrases:
                url = f'https://www.buda.com/api/v2/markets/{i}'
                response = requests.get(url)
                item = response.json()
                raw = json.loads(item)
                for j in raw:
                    value = raw[j]
                    print(f'{j}{value}')

            elif i == 'HELP':
                for item in phrases:
                   print(item)

            elif i == 'EXIT':
                var_boolean = False
                exit()

            else:
                print('Response invalid')

        except:
            print('error')


if __name__ == '__main__':
    main()
