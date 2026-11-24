from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LambdaExecution(BaseModel):
    DurableExecutionArn: StrictStr | None = None
    DurableExecutionName: StrictStr | None = None
    FunctionArn: StrictStr | None = None
    Status: StrictStr | None = None
    StartTimestamp: datetime.datetime | StrictStr | None = None
    EndTimestamp: datetime.datetime | StrictStr | None = None
    KMSKeyArn: StrictStr | None = None
