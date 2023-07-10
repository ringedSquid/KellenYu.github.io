import bottle

def start():
    bottle.run(debug=True, reloader=True, port=8000)

if __name__ == "__main__":
    start()
