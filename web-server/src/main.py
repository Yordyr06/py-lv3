import store

def run():
  store.get_data('https://api.escuelajs.co/api/v1/categories')

if __name__ == '__main__':
  run()