from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueEntity(BaseModel):
    EntityName: StrictStr | None = None
    Label: StrictStr | None = None
    IsParentEntity: StrictBool | None = None
    Description: StrictStr | None = None
    Category: StrictStr | None = None
    CustomProperties: dict[StrictStr, StrictStr] | None = None
