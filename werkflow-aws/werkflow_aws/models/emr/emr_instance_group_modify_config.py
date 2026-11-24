from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .emr_configuration import EMRConfiguration
from .emr_shrink_policy import EMRShrinkPolicy


class EMRInstanceGroupModifyConfig(BaseModel):
    InstanceGroupId: StrictStr
    InstanceCount: StrictInt | None = None
    EC2InstanceIdsToTerminate: list[StrictStr] | None = None
    ShrinkPolicy: EMRShrinkPolicy | None = None
    ReconfigurationType: Literal['OVERWRITE', 'MERGE'] | None = None
    Configurations: list[EMRConfiguration] | None = None
