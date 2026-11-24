from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_data_source import QBusinessDataSource


class QBusinessListDataSourcesResponse(BaseModel):
    dataSources: list[QBusinessDataSource] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
