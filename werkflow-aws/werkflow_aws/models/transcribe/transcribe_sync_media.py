from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class TranscribeSyncMedia(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    MediaBytes: StrictBytes | BinaryIO | StrictStr | None = None
    MediaFileUri: StrictStr | None = None
