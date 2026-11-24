from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_child_block import ComprehendChildBlock


class ComprehendBlockReference(BaseModel):
    BlockId: StrictStr | None = None
    BeginOffset: StrictInt | None = None
    EndOffset: StrictInt | None = None
    ChildBlocks: list[ComprehendChildBlock] | None = None
