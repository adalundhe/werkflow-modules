from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_resource_mapping import CloudFormationResourceMapping
from .cloud_formation_tag import CloudFormationTag


class CloudFormationStackRefactorAction(BaseModel):
    Action: StrictStr | None = None
    Entity: StrictStr | None = None
    PhysicalResourceId: StrictStr | None = None
    ResourceIdentifier: StrictStr | None = None
    Description: StrictStr | None = None
    Detection: StrictStr | None = None
    DetectionReason: StrictStr | None = None
    TagResources: list[CloudFormationTag] | None = None
    UntagResources: list[StrictStr] | None = None
    ResourceMapping: CloudFormationResourceMapping | None = None
