from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_applicable_to import QuickSightApplicableTo


class QuickSightApprovalPolicy(BaseModel):
    PolicyId: StrictStr | None = None
    PolicyArn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Actions: list[StrictStr] | None = None
    AssetTypes: list[StrictStr] | None = None
    ApplicableTo: QuickSightApplicableTo | None = None
    ApprovalGroups: list[StrictStr] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
