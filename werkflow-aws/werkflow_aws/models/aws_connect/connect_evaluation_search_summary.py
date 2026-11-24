from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_evaluation_search_metadata import ConnectEvaluationSearchMetadata


class ConnectEvaluationSearchSummary(BaseModel):
    EvaluationId: StrictStr | None = None
    EvaluationArn: StrictStr | None = None
    EvaluationFormId: StrictStr | None = None
    EvaluationFormVersion: StrictInt | None = None
    EvaluationFormTitle: StrictStr | None = None
    Metadata: ConnectEvaluationSearchMetadata | None = None
    Status: StrictStr | None = None
    EvaluationType: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
