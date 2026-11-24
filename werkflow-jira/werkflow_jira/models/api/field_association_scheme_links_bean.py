from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FieldAssociationSchemeLinksBean(BaseModel):
    associations: StrictStr | None = None
    projects: StrictStr | None = None
