from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppRunnerListOperationsRequest(BaseModel):
    ServiceArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
