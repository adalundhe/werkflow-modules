from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AppFlowSAPODataPaginationConfig(BaseModel):
    maxPageSize: StrictInt | None = None
