from __future__ import annotations
from pydantic import BaseModel, StrictInt


class NetworkManagerBandwidth(BaseModel):
    UploadSpeed: StrictInt | None = None
    DownloadSpeed: StrictInt | None = None
