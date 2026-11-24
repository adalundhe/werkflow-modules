from __future__ import annotations
from pydantic import BaseModel, StrictStr


class UpdateFieldAssociationSchemeLinksBean(BaseModel):
    associations: StrictStr | None = None
    projects: StrictStr | None = None
