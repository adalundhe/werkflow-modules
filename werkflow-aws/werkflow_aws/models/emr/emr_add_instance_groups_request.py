from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_instance_group_config import EMRInstanceGroupConfig


class EMRAddInstanceGroupsRequest(BaseModel):
    InstanceGroups: list[EMRInstanceGroupConfig]
    JobFlowId: StrictStr
