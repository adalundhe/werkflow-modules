from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoMediaSourceConfig(BaseModel):
    MediaUriSecretArn: StrictStr | None = None
    MediaUriType: StrictStr | None = None
