from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationLFTag(BaseModel):
    TagKey: StrictStr | None = None
    TagValues: list[StrictStr] | None = None
