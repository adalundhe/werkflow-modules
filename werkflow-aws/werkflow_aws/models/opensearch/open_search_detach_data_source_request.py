from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDetachDataSourceRequest(BaseModel):
    id: StrictStr
    dataSourceArn: StrictStr
