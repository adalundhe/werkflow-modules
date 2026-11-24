from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListClusterExtensionVersionsRequest(BaseModel):
    ExtensionName: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
