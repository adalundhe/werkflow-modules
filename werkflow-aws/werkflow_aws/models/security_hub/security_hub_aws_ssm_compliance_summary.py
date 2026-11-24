from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsSsmComplianceSummary(BaseModel):
    Status: StrictStr | None = None
    CompliantCriticalCount: StrictInt | None = None
    CompliantHighCount: StrictInt | None = None
    CompliantMediumCount: StrictInt | None = None
    ExecutionType: StrictStr | None = None
    NonCompliantCriticalCount: StrictInt | None = None
    CompliantInformationalCount: StrictInt | None = None
    NonCompliantInformationalCount: StrictInt | None = None
    CompliantUnspecifiedCount: StrictInt | None = None
    NonCompliantLowCount: StrictInt | None = None
    NonCompliantHighCount: StrictInt | None = None
    CompliantLowCount: StrictInt | None = None
    ComplianceType: StrictStr | None = None
    PatchBaselineId: StrictStr | None = None
    OverallSeverity: StrictStr | None = None
    NonCompliantMediumCount: StrictInt | None = None
    NonCompliantUnspecifiedCount: StrictInt | None = None
    PatchGroup: StrictStr | None = None
