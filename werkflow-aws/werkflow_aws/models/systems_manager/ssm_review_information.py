from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SSMReviewInformation(BaseModel):
    ReviewedTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Reviewer: StrictStr | None = None
