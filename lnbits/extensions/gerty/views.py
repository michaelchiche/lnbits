import json
from http import HTTPStatus

from fastapi import Request
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from loguru import logger
from starlette.exceptions import HTTPException
from starlette.responses import HTMLResponse

from lnbits.core.models import User
from lnbits.decorators import check_user_exists
from lnbits.settings import LNBITS_CUSTOM_LOGO, LNBITS_SITE_TITLE

from . import gerty_ext, gerty_renderer
from .crud import get_gerty
from .views_api import api_gerty_json

templates = Jinja2Templates(directory="templates")


@gerty_ext.get("/", response_class=HTMLResponse)
async def index(request: Request, user: User = Depends(check_user_exists)):
    return gerty_renderer().TemplateResponse(
        "gerty/index.html", {"request": request, "user": user.dict()}
    )


@gerty_ext.get("/{gerty_id}", response_class=HTMLResponse)
async def display(request: Request, gerty_id):
    gerty = await get_gerty(gerty_id)
    if not gerty:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Gerty does not exist."
        )
    gertyData = await api_gerty_json(gerty_id)
    return gerty_renderer().TemplateResponse(
        "gerty/gerty.html", {"request": request, "gerty": gertyData}
    )