from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IAMContextEntry(BaseModel):
    ContextKeyName: StrictStr | None = None
    ContextKeyValues: list[StrictStr] | None = None
    ContextKeyType: Literal['string', 'stringList', 'numeric', 'numericList', 'boolean', 'booleanList', 'ip', 'ipList', 'binary', 'binaryList', 'date', 'dateList'] | None = None
