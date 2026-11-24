from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictStr


class ChangeDetails(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    field: StrictStr | None = None
    fieldId: StrictStr | None = None
    fieldtype: StrictStr | None = None
    from_: StrictStr | None = PydanticField(default=None, alias='from')
    fromString: StrictStr | None = None
    to: StrictStr | None = None
    toString: StrictStr | None = None
