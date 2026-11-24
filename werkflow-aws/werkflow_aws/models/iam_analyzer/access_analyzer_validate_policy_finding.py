from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_location import AccessAnalyzerLocation


class AccessAnalyzerValidatePolicyFinding(BaseModel):
    findingDetails: StrictStr | None = None
    findingType: StrictStr | None = None
    issueCode: StrictStr | None = None
    learnMoreLink: StrictStr | None = None
    locations: list[AccessAnalyzerLocation] | None = None
