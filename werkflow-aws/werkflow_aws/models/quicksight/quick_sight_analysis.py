from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_analysis_error import QuickSightAnalysisError
from .quick_sight_sheet import QuickSightSheet


class QuickSightAnalysis(BaseModel):
    AnalysisId: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Errors: list[QuickSightAnalysisError] | None = None
    DataSetArns: list[StrictStr] | None = None
    TopicArns: list[StrictStr] | None = None
    ThemeArn: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    Sheets: list[QuickSightSheet] | None = None
