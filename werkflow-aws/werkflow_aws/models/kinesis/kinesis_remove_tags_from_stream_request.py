from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisRemoveTagsFromStreamRequest(BaseModel):
    TagKeys: list[StrictStr]
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
