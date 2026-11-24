from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_change_set_hook_target_details import CloudFormationChangeSetHookTargetDetails


class CloudFormationChangeSetHook(BaseModel):
    InvocationPoint: StrictStr | None = None
    FailureMode: StrictStr | None = None
    TypeName: StrictStr | None = None
    TypeVersionId: StrictStr | None = None
    TypeConfigurationVersionId: StrictStr | None = None
    TargetDetails: CloudFormationChangeSetHookTargetDetails | None = None
