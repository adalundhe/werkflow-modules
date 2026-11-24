from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class KendraSuggestableConfig(BaseModel):
    AttributeName: StrictStr | None = None
    Suggestable: StrictBool | None = None
