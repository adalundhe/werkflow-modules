from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_alternate_path_hint import EC2AlternatePathHint
from .ec2_explanation import EC2Explanation
from .ec2_path_component import EC2PathComponent
from .ec2_tag_model import EC2TagModel


class EC2NetworkInsightsAnalysis(BaseModel):
    NetworkInsightsAnalysisId: StrictStr | None = None
    NetworkInsightsAnalysisArn: StrictStr | None = None
    NetworkInsightsPathId: StrictStr | None = None
    AdditionalAccounts: list[StrictStr] | None = None
    FilterInArns: list[StrictStr] | None = None
    FilterOutArns: list[StrictStr] | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    WarningMessage: StrictStr | None = None
    NetworkPathFound: StrictBool | None = None
    ForwardPathComponents: list[EC2PathComponent] | None = None
    ReturnPathComponents: list[EC2PathComponent] | None = None
    Explanations: list[EC2Explanation] | None = None
    AlternatePathHints: list[EC2AlternatePathHint] | None = None
    SuggestedAccounts: list[StrictStr] | None = None
    Tags: list[EC2TagModel] | None = None
