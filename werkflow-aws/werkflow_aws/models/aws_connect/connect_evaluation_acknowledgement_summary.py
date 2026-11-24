from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectEvaluationAcknowledgementSummary(BaseModel):
    AcknowledgedTime: datetime.datetime | StrictStr | None = None
    AcknowledgedBy: StrictStr | None = None
    AcknowledgerComment: StrictStr | None = None
