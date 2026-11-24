from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMValidateCloudConnectorRequest(BaseModel):
    CloudConnectorId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
