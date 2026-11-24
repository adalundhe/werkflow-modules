from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_change_set_hook_resource_target_details import CloudFormationChangeSetHookResourceTargetDetails


class CloudFormationChangeSetHookTargetDetails(BaseModel):
    TargetType: StrictStr | None = None
    ResourceTargetDetails: CloudFormationChangeSetHookResourceTargetDetails | None = None
