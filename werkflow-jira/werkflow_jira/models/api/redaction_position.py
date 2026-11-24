from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictInt, StrictStr


class RedactionPosition(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    adfPointer: StrictStr | None = None
    expectedText: StrictStr | None = None
    from_: StrictInt | None = PydanticField(default=None, alias='from')
    to: StrictInt | None = None
