from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchGetDirectQueryDataSourceRequest(BaseModel):
    DataSourceName: StrictStr
