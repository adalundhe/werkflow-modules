from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_applicable_to import QuickSightApplicableTo


class QuickSightUpdateApprovalPolicyRequest(BaseModel):
    PolicyId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Actions: list[Literal['SHARE', 'PUBLISH']] | None = None
    AssetTypes: list[Literal['AGENT', 'SPACE', 'KNOWLEDGE_BASE', 'FLOW']] | None = None
    ApplicableTo: QuickSightApplicableTo | None = None
    ApprovalGroups: list[StrictStr] | None = None
