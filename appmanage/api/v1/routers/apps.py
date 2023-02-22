from typing import Optional, List

from fastapi import APIRouter, status, Depends
from pydantic import BaseModel
from starlette.responses import JSONResponse
import os, io, sys, platform, shutil, time, subprocess, json, datetime

from api.model.app import App
from api.service import manage
from api.utils import shell_execute

router = APIRouter()

@router.get("")
def list_my_apps():
    list = manage.get_my_app()
    return JSONResponse(content=list)

@router.get("/create")
def start_app(app_name: Optional[str] = None):

    return {}

@router.get("/start")
def start_app(app_name: Optional[str] = None):

    return {}
