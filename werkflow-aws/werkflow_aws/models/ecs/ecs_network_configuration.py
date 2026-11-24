from __future__ import annotations
from pydantic import BaseModel
from .ecs_aws_vpc_configuration import ECSAwsVpcConfiguration


class ECSNetworkConfiguration(BaseModel):
    awsvpcConfiguration: ECSAwsVpcConfiguration | None = None
