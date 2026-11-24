from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectEvaluationReviewRequestComment(BaseModel):
    Comment: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
