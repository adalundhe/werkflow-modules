from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_activity_window import GuardDutyActivityWindow
from .guard_duty_enrichment import GuardDutyEnrichment
from .guard_duty_investigation_actor import GuardDutyInvestigationActor


class GuardDutyS3Activity(BaseModel):
    Api: StrictStr | None = None
    AffectedBucket: StrictStr | None = None
    OtherS3Activity: StrictStr | None = None
    NonS3Activity: StrictStr | None = None
    SessionAssessment: StrictStr | None = None
    EventCount: StrictInt | None = None
    Actor: GuardDutyInvestigationActor | None = None
    SourceIp: StrictStr | None = None
    Enrichment: GuardDutyEnrichment | None = None
    ActivityWindow: GuardDutyActivityWindow | None = None
