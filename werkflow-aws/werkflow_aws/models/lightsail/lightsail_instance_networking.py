from __future__ import annotations
from pydantic import BaseModel
from .lightsail_instance_port_info import LightsailInstancePortInfo
from .lightsail_monthly_transfer import LightsailMonthlyTransfer


class LightsailInstanceNetworking(BaseModel):
    monthlyTransfer: LightsailMonthlyTransfer | None = None
    ports: list[LightsailInstancePortInfo] | None = None
