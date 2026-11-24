from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectContactEvaluation(BaseModel):
    FormId: StrictStr | None = None
    EvaluationArn: StrictStr | None = None
    Status: StrictStr | None = None
    StartTimestamp: datetime.datetime | StrictStr | None = None
    EndTimestamp: datetime.datetime | StrictStr | None = None
    DeleteTimestamp: datetime.datetime | StrictStr | None = None
    ExportLocation: StrictStr | None = None
