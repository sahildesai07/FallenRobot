from flask import Flask
from aiohttp import web

# Flask app
app_flask = Flask(__name__)

@app_flask.route('/')
def hello_world():
    return 'GreyMatters'

# Run Flask app
if __name__ == "__main__":
    app_flask.run()

# aiohttp app
routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("CodeXBotz")

# Run aiohttp app
if __name__ == "__main__":
    app_aiohttp = web.Application()
    app_aiohttp.router.add_routes(routes)
    web.run_app(app_aiohttp)
