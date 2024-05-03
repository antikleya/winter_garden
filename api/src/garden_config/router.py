from fastapi import APIRouter, Depends, status
from .schemas.garden_config import GardenConfig, GardenConfigUpdate
from .service import GardenConfigService
from src.auth.router import current_user
from .dependencies import valid_config


router = APIRouter()


@router.get(
    '',
    response_model=GardenConfig,
    status_code=status.HTTP_200_OK,
)
def get_config(
    service: GardenConfigService = Depends(GardenConfig)
):
    return service.get()


@router.put(
    '',
    response_model=GardenConfig,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(current_user)]
)
def get_config(
    new_config: GardenConfigUpdate = Depends(valid_config),
    service: GardenConfigService = Depends(GardenConfig)
):
    return service.update(new_config)
