from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_resource_target_definition import CloudFormationResourceTargetDefinition


class CloudFormationResourceChangeDetail(BaseModel):
    Target: CloudFormationResourceTargetDefinition | None = None
    Evaluation: StrictStr | None = None
    ChangeSource: StrictStr | None = None
    CausingEntity: StrictStr | None = None
