from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FieldAssociationSchemeProjectSearchResult(BaseModel):
    avatarUrls: dict[StrictStr, StrictStr] | None = None
    deleted: StrictBool | None = None
    id: StrictStr | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
