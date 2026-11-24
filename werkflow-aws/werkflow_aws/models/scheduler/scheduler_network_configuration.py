from __future__ import annotations
from pydantic import BaseModel
from .scheduler_aws_vpc_configuration import SchedulerAwsVpcConfiguration


class SchedulerNetworkConfiguration(BaseModel):
    awsvpcConfiguration: SchedulerAwsVpcConfiguration | None = None
