from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm
from app.v1.schema import ingresos_schema
from app.v1.service import Tablaingresos_services
from app.v1.service import Tablaingresos_services
from app.v1.schema.ingresos_schema import Ingresos_Schema
from app.v1.utils.db import get_db


router = APIRouter(
    prefix="/api/v1/ingresos",
    
    tags=["Ingresos"]
)

@router.post(
    "/Ingresos/",
    status_code=status.HTTP_201_CREATED,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Crea un nuevo ingreso"
)
def create_ingresos(ingresos: ingresos_schema.Ingresos_Schema = Body(...)):

    return Tablaingresos_services.save_services(ingresos)

@router.delete(
    "/Delete/",
    status_code=status.HTTP_200_OK,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Elimina el ingreso creado anteriormente"
)
def delete_ingresos(ID:int):

    return Tablaingresos_services.delete_services(ID)

@router.put(
    "/Actualizar/",
    status_code=status.HTTP_200_OK,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Actualiza el ingreso"
)
def put_ingresos(ID:int,ingresos: ingresos_schema.Ingresos_Schema = Body(...)):

    return Tablaingresos_services.update_services(ingresos,ID)

@router.get(
    "/SeleccionarporID/",
    status_code=status.HTTP_200_OK,
    response_model=list,
    dependencies=[Depends(get_db)],
    summary="selecciona por Usuario"
)
def seleccionarporusuario(ID:int):

    return Tablaingresos_services.seleccionarporusuario(ID)