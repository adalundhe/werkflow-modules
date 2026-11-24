from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectPersistentChat(BaseModel):
    RehydrationType: Literal['ENTIRE_PAST_SESSION', 'FROM_SEGMENT'] | None = None
    SourceContactId: StrictStr | None = None
