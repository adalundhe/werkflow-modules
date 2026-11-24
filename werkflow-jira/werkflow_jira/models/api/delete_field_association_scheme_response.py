from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DeleteFieldAssociationSchemeResponse(BaseModel):
    deleted: StrictBool | None = None
    id: StrictStr | None = None
