import dearpygui.dearpygui as dpg
import requests

# vars 
phrases = ['BTC-CLP', 'BTC-COP',  'BTC-USDC', 'USDC-ARS',
           'USDC-PEN', 'USDC-COP', 'USDC-CLP', 'LTC-ARS', 'LTC-PEN',
           'LTC-COP', 'LTC-CLP', 'LTC-BTC', 'BCH-ARS', 'ETH-ARS', 'BTC-ARS',
           'BCH-PEN', 'BCH-COP', 'BCH-CLP', 'BCH-BTC', 'ETH-COP', 'ETH-PEN',
           'BTC-PEN', 'ETH-BTC', 'ETH-CLP']

data_page = 'https://www.buda.com/api/v2/markets/'


# Functions
def send_info_bitcoin():
    try:
        response = dpg.get_value(input_user)
        if response in phrases:
            url = f'{data_page}{response}'
            page = requests.get(url)
            result = page.json()
            content = result['market']
            return dpg.set_value(response_text, content)
        
        elif response is not phrases:
            return dpg.set_value(response_text, 'Please try again')
 
    except:
        return dpg.set_value(response_text, 'We are working for you, comming soon we fix this')

    
def print_help():
    try:
        return dpg.set_value(help_text, phrases)
    except:
        return dpg.set_value(help_text, 'something goes wrong')
    

def clean():
    try:
        dpg.set_value(help_text, '')
        dpg.set_value(response_text, '')
    except:
        dpg.set_value(help_text,'it was imposible to solve')

# create context app

dpg.create_context()

with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("NotoSerifCJKjp-Medium.otf", 18)
    second_font = dpg.add_font("NotoSerifCJKjp-Medium.otf", 18)

with dpg.value_registry():
    dpg.add_string_value(default_value="", tag="string_value")

with dpg.window(tag='index',label="Bitcoins data", autosize=True, width=400, height=400):
    welcome_text = dpg.add_text(f'Hello user',wrap=350)
    input_user = dpg.add_input_text(label="Bitcoin", source="string_value")
    dpg.add_button(label='submit', before=0, callback=send_info_bitcoin)
    dpg.add_button(label='help' , callback=print_help)
    dpg.add_button(label='clean' , callback=clean)

    help_text = dpg.add_text(f'',wrap=350)
    response_text = dpg.add_text(f'', wrap=180)


dpg.create_viewport(title='Bitcoins Buda', min_width=400, min_height=400,
                    width=400, height=400, max_width=400, max_height=400)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('index', True)
dpg.start_dearpygui()
dpg.destroy_context()
