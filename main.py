from sanic import Sanic
from sanic.response import text
from database.server import routes_bp

app = Sanic("MyHelloWorldApp")
app.blueprint(routes_bp)

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")

# if __name__ == "__main__":

   

#     # app = create_app()
#     app.run(host="0.0.0.0", port=port, debug=True, access_log=False)



# debug logs enabled with debug = True
app.run(host ="0.0.0.0", port = 6000)
