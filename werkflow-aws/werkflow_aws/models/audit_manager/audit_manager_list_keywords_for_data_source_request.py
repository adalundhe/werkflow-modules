from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerListKeywordsForDataSourceRequest(BaseModel):
    source: Literal['AWS_Cloudtrail', 'AWS_Config', 'AWS_Security_Hub', 'AWS_API_Call', 'MANUAL']
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
