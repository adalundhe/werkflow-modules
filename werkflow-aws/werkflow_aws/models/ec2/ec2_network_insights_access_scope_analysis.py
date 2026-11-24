from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2NetworkInsightsAccessScopeAnalysis(BaseModel):
    NetworkInsightsAccessScopeAnalysisId: StrictStr | None = None
    NetworkInsightsAccessScopeAnalysisArn: StrictStr | None = None
    NetworkInsightsAccessScopeId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    WarningMessage: StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    FindingsFound: StrictStr | None = None
    AnalyzedEniCount: StrictInt | None = None
    Tags: list[EC2TagModel] | None = None
