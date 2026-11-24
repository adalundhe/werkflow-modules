from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_live_resource_drift import CloudFormationLiveResourceDrift


class CloudFormationResourceTargetDefinition(BaseModel):
    Attribute: StrictStr | None = None
    Name: StrictStr | None = None
    RequiresRecreation: StrictStr | None = None
    Path: StrictStr | None = None
    BeforeValue: StrictStr | None = None
    AfterValue: StrictStr | None = None
    BeforeValueFrom: StrictStr | None = None
    AfterValueFrom: StrictStr | None = None
    Drift: CloudFormationLiveResourceDrift | None = None
    AttributeChangeType: StrictStr | None = None
