from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .fms_compliance_violator import FMSComplianceViolator


class FMSPolicyComplianceDetail(BaseModel):
    PolicyOwner: StrictStr | None = None
    PolicyId: StrictStr | None = None
    MemberAccount: StrictStr | None = None
    Violators: list[FMSComplianceViolator] | None = None
    EvaluationLimitExceeded: StrictBool | None = None
    ExpiredAt: datetime.datetime | StrictStr | None = None
    IssueInfoMap: dict[StrictStr, StrictStr] | None = None
