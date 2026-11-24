from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_lake_data_lake_resource import SecurityLakeDataLakeResource


class SecurityLakeListDataLakesResponse(BaseModel):
    dataLakes: list[SecurityLakeDataLakeResource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
