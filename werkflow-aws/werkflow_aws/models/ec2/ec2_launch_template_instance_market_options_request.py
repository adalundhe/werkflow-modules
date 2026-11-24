from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .ec2_launch_template_spot_market_options_request import EC2LaunchTemplateSpotMarketOptionsRequest


class EC2LaunchTemplateInstanceMarketOptionsRequest(BaseModel):
    MarketType: Literal['spot', 'capacity-block', 'interruptible-capacity-reservation', 'on-demand'] | None = None
    SpotOptions: EC2LaunchTemplateSpotMarketOptionsRequest | None = None
