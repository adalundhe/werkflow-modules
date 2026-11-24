from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectChatStreamingConfiguration(BaseModel):
    StreamingEndpointArn: StrictStr
