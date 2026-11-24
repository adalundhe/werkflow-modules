from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .support_recent_case_communications import SupportRecentCaseCommunications


class SupportCaseDetails(BaseModel):
    caseId: StrictStr | None = None
    displayId: StrictStr | None = None
    subject: StrictStr | None = None
    status: StrictStr | None = None
    serviceCode: StrictStr | None = None
    categoryCode: StrictStr | None = None
    severityCode: StrictStr | None = None
    submittedBy: StrictStr | None = None
    timeCreated: StrictStr | None = None
    recentCommunications: SupportRecentCaseCommunications | None = None
    ccEmailAddresses: list[StrictStr] | None = None
    language: StrictStr | None = None
