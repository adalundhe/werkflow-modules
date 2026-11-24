from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_cloud_details import GuardDutyCloudDetails
from .guard_duty_investigation_metadata import GuardDutyInvestigationMetadata
from .guard_duty_investigation_scope import GuardDutyInvestigationScope
from .guard_duty_investigation_summary_data import GuardDutyInvestigationSummaryData


class GuardDutyInvestigation(BaseModel):
    InvestigationId: StrictStr | None = None
    Status: StrictStr | None = None
    TriggerPrompt: StrictStr | None = None
    TriggeredBy: StrictStr | None = None
    Metadata: GuardDutyInvestigationMetadata | None = None
    Cloud: GuardDutyCloudDetails | None = None
    RiskLevel: StrictStr | None = None
    Risk: StrictStr | None = None
    Confidence: StrictStr | None = None
    Summary: StrictStr | None = None
    SummaryData: GuardDutyInvestigationSummaryData | None = None
    Scope: GuardDutyInvestigationScope | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Error: StrictStr | None = None
