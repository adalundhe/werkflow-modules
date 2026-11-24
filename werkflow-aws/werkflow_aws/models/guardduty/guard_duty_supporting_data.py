from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_analysis_record import GuardDutyAnalysisRecord
from .guard_duty_fetch_record import GuardDutyFetchRecord
from .guard_duty_metadata_record import GuardDutyMetadataRecord
from .guard_duty_observation_record import GuardDutyObservationRecord


class GuardDutySupportingData(BaseModel):
    Fetch: GuardDutyFetchRecord | None = None
    Analysis: GuardDutyAnalysisRecord | None = None
    Observation: GuardDutyObservationRecord | None = None
    Metadata: GuardDutyMetadataRecord | None = None
