from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MacieUpdateRetrievalConfiguration(BaseModel):
    retrievalMode: Literal['CALLER_CREDENTIALS', 'ASSUME_ROLE']
    roleName: StrictStr | None = None
