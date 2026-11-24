from __future__ import annotations
from pydantic import BaseModel
from .transfer_described_web_app_vpc_config import TransferDescribedWebAppVpcConfig


class TransferDescribedWebAppEndpointDetails(BaseModel):
    Vpc: TransferDescribedWebAppVpcConfig | None = None
