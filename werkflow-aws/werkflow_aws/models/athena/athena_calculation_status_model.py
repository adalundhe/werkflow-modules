from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AthenaCalculationStatusModel(BaseModel):
    SubmissionDateTime: datetime.datetime | StrictStr | None = None
    CompletionDateTime: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    StateChangeReason: StrictStr | None = None
