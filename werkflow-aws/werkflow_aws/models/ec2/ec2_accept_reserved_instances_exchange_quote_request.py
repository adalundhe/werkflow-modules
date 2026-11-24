from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_target_configuration_request import EC2TargetConfigurationRequest


class EC2AcceptReservedInstancesExchangeQuoteRequest(BaseModel):
    ReservedInstanceIds: list[StrictStr]
    DryRun: StrictBool | None = None
    TargetConfigurations: list[EC2TargetConfigurationRequest] | None = None
