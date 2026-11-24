from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisVideoListEdgeAgentConfigurationsRequest(BaseModel):
    HubDeviceArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
