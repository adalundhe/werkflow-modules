from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueOption(BaseModel):
    Value: StrictStr | None = None
    Label: StrictStr | None = None
    Description: StrictStr | None = None
