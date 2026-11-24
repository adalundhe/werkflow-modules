from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class TimestreamQueryPrepareQueryRequest(BaseModel):
    QueryString: StrictStr
    ValidateOnly: StrictBool | None = None
