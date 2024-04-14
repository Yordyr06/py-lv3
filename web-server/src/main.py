import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
  return [1, 2, 3, 4, 5]

@app.get('/contact', response_class = HTMLResponse)
async def get_contact():
  return '''
    <html>
      <head>
        <title>Contact</title>
      </head>
      <body>
        <h1>Contact</h1>
        <p>Send us an email</p>
    </html>
  '''

def run():
  store.get_data('https://api.escuelajs.co/api/v1/categories')

if __name__ == '__main__':
  run()