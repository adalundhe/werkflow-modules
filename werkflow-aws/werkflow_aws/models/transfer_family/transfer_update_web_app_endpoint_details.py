from __future__ import annotations
from pydantic import BaseModel
from .transfer_update_web_app_vpc_config import TransferUpdateWebAppVpcConfig


class TransferUpdateWebAppEndpointDetails(BaseModel):
    Vpc: TransferUpdateWebAppVpcConfig | None = None
