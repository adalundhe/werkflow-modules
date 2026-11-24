from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SSMGetParameterHistoryRequest(BaseModel):
    Name: StrictStr
    WithDecryption: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
