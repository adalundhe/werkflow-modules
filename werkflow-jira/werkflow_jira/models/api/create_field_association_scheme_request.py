from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CreateFieldAssociationSchemeRequest(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
