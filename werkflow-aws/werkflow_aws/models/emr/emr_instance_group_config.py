from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .emr_auto_scaling_policy import EMRAutoScalingPolicy
from .emr_configuration import EMRConfiguration
from .emr_ebs_configuration import EMREbsConfiguration


class EMRInstanceGroupConfig(BaseModel):
    InstanceRole: Literal['MASTER', 'CORE', 'TASK']
    InstanceType: StrictStr
    InstanceCount: StrictInt
    Name: StrictStr | None = None
    Market: Literal['ON_DEMAND', 'SPOT'] | None = None
    BidPrice: StrictStr | None = None
    Configurations: list[EMRConfiguration] | None = None
    EbsConfiguration: EMREbsConfiguration | None = None
    AutoScalingPolicy: EMRAutoScalingPolicy | None = None
    CustomAmiId: StrictStr | None = None
