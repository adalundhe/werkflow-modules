from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerBatchDeleteDelegationByAssessmentRequest(BaseModel):
    delegationIds: list[StrictStr]
    assessmentId: StrictStr
