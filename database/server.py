

from sanic import Blueprint, response
from sanic.request import Request
from sanic.response import HTTPResponse

routes_bp = Blueprint('routes_bp', url_prefix="/cron_service")

@routes_bp.route("/server", methods=["POST"])
async def server_route(request: Request):
    print("hello from server")
    return response.json({"msg": "message from server file"}, status=200, content_type="application/json")
