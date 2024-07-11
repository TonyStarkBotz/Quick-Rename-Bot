# Don't Remove Credit 😔
# Telegram Channel @TonyStark_Botz & @MovieTimesTV
# Developer @Tony_Stark_75
# Update Channel @TonyStark_Botz & @TonyStarkBotzXSupport

from aiohttp import web

tony_FileRenameBot = web.RouteTableDef()

@tony_FileRenameBot.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("tonystarkbotz")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(Quick_FileRenameBot)
    return web_app

# Don't Remove Credit 😔
# Telegram Channel @TonyStark_Botz & @MovieTimesTV
# Developer @Tony_Stark_75
# Update Channel @TonyStark_Botz & @TonyStarkBotzXSupport
