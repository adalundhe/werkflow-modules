from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_media_concurrency import ConnectMediaConcurrency


class ConnectUpdateRoutingProfileConcurrencyRequest(BaseModel):
    InstanceId: StrictStr
    RoutingProfileId: StrictStr
    MediaConcurrencies: list[ConnectMediaConcurrency]
