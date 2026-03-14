import google.generativeai as genai

genai.configure(api_key="AIzaSyAfJ53SslReHw6AJf667KhWsAOsgrwxsb0")

models = genai.list_models()

for model in models:
    print(model.name)