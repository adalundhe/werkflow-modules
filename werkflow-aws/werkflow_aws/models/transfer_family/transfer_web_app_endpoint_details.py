from __future__ import annotations
from pydantic import BaseModel
from .transfer_web_app_vpc_config import TransferWebAppVpcConfig


class TransferWebAppEndpointDetails(BaseModel):
    Vpc: TransferWebAppVpcConfig | None = None
