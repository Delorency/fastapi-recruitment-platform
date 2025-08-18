import os

from fastapi import FastAPI

from app.core.config import configs 



def lifespan(app: FastAPI):
    createStaticDir()
    createLogDir()
    yield


def createStaticDir():
    path = f'{configs.projectcfg.project_path}/{configs.projectcfg.static_dir}'

    if not os.path.exists(path):
        os.mkdir(path)


def createLogDir():
    path = f'{configs.projectcfg.project_path}/{configs.logcfg.logsdir}'

    if not os.path.exists(path):
        os.mkdir(path)


    os.open(f'{path}/{configs.logcfg.apilogfilename}', os.O_CREAT|os.O_APPEND)
    os.open(f'{path}/{configs.logcfg.dblogfilename}', os.O_CREAT|os.O_APPEND)