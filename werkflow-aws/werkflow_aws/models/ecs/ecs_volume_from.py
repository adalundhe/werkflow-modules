from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECSVolumeFrom(BaseModel):
    sourceContainer: StrictStr | None = None
    readOnly: StrictBool | None = None
