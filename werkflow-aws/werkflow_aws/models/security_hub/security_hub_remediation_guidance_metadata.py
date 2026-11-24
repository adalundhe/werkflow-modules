from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubRemediationGuidanceMetadata(BaseModel):
    ResourceType: StrictStr | None = None
    ExposureType: StrictStr | None = None
    TraitTitles: list[StrictStr] | None = None
    Reversibility: StrictStr | None = None
    FixEffect: StrictStr | None = None
    RiskLevel: StrictStr | None = None
    AutomationLevel: StrictStr | None = None
    HumanReviewRequired: StrictBool | None = None
    GeneratedAt: datetime.datetime | StrictStr | None = None
    VerificationStatus: StrictStr | None = None
