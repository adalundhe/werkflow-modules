from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeSyncOutputConfiguration(BaseModel):
    OutputMediaFileUri: StrictStr | None = None
