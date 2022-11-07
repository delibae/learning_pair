import eel
import pandas as pd
import json
from pandas import json_normalize

# Set web files folder
eel.init('web')

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

@eel.expose
def get_file(file):
    print(type(file))
    info = json.loads(file)
    df = json_normalize(info)
    ad_list = df['도로명']
    print(ad_list)

say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

eel.start('/page1.html', size=(1280, 832))  # Start