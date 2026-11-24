from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyFindingTypeDocumentation(BaseModel):
    Description: StrictStr | None = None
    Severity: StrictStr | None = None
    Feature: StrictStr | None = None
    FullDescription: StrictStr | None = None
    Remediation: StrictStr | None = None
    LearnMoreLinks: list[StrictStr] | None = None
