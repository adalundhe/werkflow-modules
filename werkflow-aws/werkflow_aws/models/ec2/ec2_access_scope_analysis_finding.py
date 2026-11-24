from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_path_component import EC2PathComponent


class EC2AccessScopeAnalysisFinding(BaseModel):
    NetworkInsightsAccessScopeAnalysisId: StrictStr | None = None
    NetworkInsightsAccessScopeId: StrictStr | None = None
    FindingId: StrictStr | None = None
    FindingComponents: list[EC2PathComponent] | None = None
