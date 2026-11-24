from __future__ import annotations
from pydantic import BaseModel
from .event_bridge_aws_vpc_configuration import EventBridgeAwsVpcConfiguration


class EventBridgeNetworkConfiguration(BaseModel):
    awsvpcConfiguration: EventBridgeAwsVpcConfiguration | None = None
