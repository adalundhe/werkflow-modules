from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_applicable_to import QuickSightApplicableTo


class QuickSightCreateApprovalPolicyRequest(BaseModel):
    PolicyId: StrictStr
    Name: StrictStr
    Actions: list[Literal['SHARE', 'PUBLISH']]
    AssetTypes: list[Literal['AGENT', 'SPACE', 'KNOWLEDGE_BASE', 'FLOW']]
    ApplicableTo: QuickSightApplicableTo
    ApprovalGroups: list[StrictStr]
    Description: StrictStr | None = None
