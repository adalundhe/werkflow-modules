from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_guru_metrics_summary import CodeGuruMetricsSummary
from .code_guru_source_code_type import CodeGuruSourceCodeType


class CodeGuruCodeReviewSummary(BaseModel):
    Name: StrictStr | None = None
    CodeReviewArn: StrictStr | None = None
    RepositoryName: StrictStr | None = None
    Owner: StrictStr | None = None
    ProviderType: StrictStr | None = None
    State: StrictStr | None = None
    CreatedTimeStamp: datetime.datetime | StrictStr | None = None
    LastUpdatedTimeStamp: datetime.datetime | StrictStr | None = None
    Type: StrictStr | None = None
    PullRequestId: StrictStr | None = None
    MetricsSummary: CodeGuruMetricsSummary | None = None
    SourceCodeType: CodeGuruSourceCodeType | None = None
