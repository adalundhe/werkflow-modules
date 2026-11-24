from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_launch_template_spot_market_options import EC2LaunchTemplateSpotMarketOptions


class EC2LaunchTemplateInstanceMarketOptions(BaseModel):
    MarketType: StrictStr | None = None
    SpotOptions: EC2LaunchTemplateSpotMarketOptions | None = None
