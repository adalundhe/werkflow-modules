from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class KinesisVideoSingleMasterChannelEndpointConfiguration(BaseModel):
    Protocols: list[Literal['WSS', 'HTTPS', 'WEBRTC']] | None = None
    Role: Literal['MASTER', 'VIEWER'] | None = None
