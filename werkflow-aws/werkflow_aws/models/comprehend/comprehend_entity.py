from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .comprehend_block_reference import ComprehendBlockReference


class ComprehendEntity(BaseModel):
    Score: StrictFloat | StrictInt | None = None
    Type: StrictStr | None = None
    Text: StrictStr | None = None
    BeginOffset: StrictInt | None = None
    EndOffset: StrictInt | None = None
    BlockReferences: list[ComprehendBlockReference] | None = None
