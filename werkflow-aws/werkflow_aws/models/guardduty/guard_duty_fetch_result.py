from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_finding_type_documentation import GuardDutyFindingTypeDocumentation
from .guard_duty_investigation_detector_feature_configuration import GuardDutyInvestigationDetectorFeatureConfiguration


class GuardDutyFetchResult(BaseModel):
    ItemIds: list[StrictStr] | None = None
    TotalCount: StrictInt | None = None
    Features: list[GuardDutyInvestigationDetectorFeatureConfiguration] | None = None
    Verdict: StrictStr | None = None
    Documentation: GuardDutyFindingTypeDocumentation | None = None
