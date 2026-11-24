from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .athena_executors_summary import AthenaExecutorsSummary


class AthenaListExecutorsResponse(BaseModel):
    SessionId: StrictStr | None = None
    NextToken: StrictStr | None = None
    ExecutorsSummary: list[AthenaExecutorsSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
