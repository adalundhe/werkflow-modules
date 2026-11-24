from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_lake_data_lake_exception import SecurityLakeDataLakeException


class SecurityLakeListDataLakeExceptionsResponse(BaseModel):
    exceptions: list[SecurityLakeDataLakeException] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
