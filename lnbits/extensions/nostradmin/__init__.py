from fastapi import APIRouter
from starlette.staticfiles import StaticFiles

from lnbits.db import Database
from lnbits.helpers import template_renderer
from lnbits.tasks import catch_everything_and_restart

db = Database("ext_nostradmin")

nostradmin_static_files = [
    {
        "path": "/nostradmin/static",
        "app": StaticFiles(directory="lnbits/extensions/nostradmin/static"),
        "name": "nostradmin_static",
    }
]

nostradmin_ext: APIRouter = APIRouter(prefix="/nostradmin", tags=["nostradmin"])


def nostr_renderer():
    return template_renderer(["lnbits/extensions/nostradmin/templates"])


from .views import *  # noqa
from .views_api import *  # noqa

from .tasks import init_relays, subscribe_events


def nostradmin_start():
    loop = asyncio.get_event_loop()
    loop.create_task(catch_everything_and_restart(init_relays))
    # loop.create_task(catch_everything_and_restart(send_data))
    # loop.create_task(catch_everything_and_restart(receive_data))
    loop.create_task(catch_everything_and_restart(subscribe_events))
