from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectKinesisStreamConfig(BaseModel):
    StreamArn: StrictStr | None = None
