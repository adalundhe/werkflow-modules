from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchListDirectQueryDataSourcesRequest(BaseModel):
    NextToken: StrictStr | None = None
