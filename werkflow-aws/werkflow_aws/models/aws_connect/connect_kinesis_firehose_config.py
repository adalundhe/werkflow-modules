from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectKinesisFirehoseConfig(BaseModel):
    FirehoseArn: StrictStr | None = None
