from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .guard_duty_resource import GuardDutyResource
from .guard_duty_service import GuardDutyService


class GuardDutyFinding(BaseModel):
    AccountId: StrictStr | None = None
    Arn: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
    CreatedAt: StrictStr | None = None
    Description: StrictStr | None = None
    Id: StrictStr | None = None
    Partition: StrictStr | None = None
    Region: StrictStr | None = None
    Resource: GuardDutyResource | None = None
    SchemaVersion: StrictStr | None = None
    Service: GuardDutyService | None = None
    Severity: StrictFloat | StrictInt | None = None
    Title: StrictStr | None = None
    Type: StrictStr | None = None
    UpdatedAt: StrictStr | None = None
    AssociatedAttackSequenceArn: StrictStr | None = None
    CustomDetectionRuleName: StrictStr | None = None
