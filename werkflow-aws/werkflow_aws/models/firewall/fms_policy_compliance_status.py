from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .fms_evaluation_result import FMSEvaluationResult


class FMSPolicyComplianceStatus(BaseModel):
    PolicyOwner: StrictStr | None = None
    PolicyId: StrictStr | None = None
    PolicyName: StrictStr | None = None
    MemberAccount: StrictStr | None = None
    EvaluationResults: list[FMSEvaluationResult] | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    IssueInfoMap: dict[StrictStr, StrictStr] | None = None
