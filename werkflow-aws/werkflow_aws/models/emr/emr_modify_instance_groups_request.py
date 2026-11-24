from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_instance_group_modify_config import EMRInstanceGroupModifyConfig


class EMRModifyInstanceGroupsRequest(BaseModel):
    ClusterId: StrictStr | None = None
    InstanceGroups: list[EMRInstanceGroupModifyConfig] | None = None
