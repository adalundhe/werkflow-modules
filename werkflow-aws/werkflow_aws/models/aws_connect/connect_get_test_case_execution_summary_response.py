from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_observation_summary import ConnectObservationSummary


class ConnectGetTestCaseExecutionSummaryResponse(BaseModel):
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    ObservationSummary: ConnectObservationSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
