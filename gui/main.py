import eel

# Set web files folder
eel.init('web')

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)




say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

eel.start('page5.html', size=(1280, 832))  # Start