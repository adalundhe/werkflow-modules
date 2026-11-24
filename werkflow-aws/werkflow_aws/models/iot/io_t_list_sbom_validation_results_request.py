from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListSbomValidationResultsRequest(BaseModel):
    packageName: StrictStr
    versionName: StrictStr
    validationResult: Literal['FAILED', 'SUCCEEDED'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
