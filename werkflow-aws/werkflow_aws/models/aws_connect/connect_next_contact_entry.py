from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_next_contact_metadata import ConnectNextContactMetadata


class ConnectNextContactEntry(BaseModel):
    Type: StrictStr | None = None
    NextContactMetadata: ConnectNextContactMetadata | None = None
