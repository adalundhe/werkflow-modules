from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .create_field_association_scheme_links_bean import CreateFieldAssociationSchemeLinksBean


class CreateFieldAssociationSchemeResponse(BaseModel):
    description: StrictStr | None = None
    id: StrictInt | None = None
    links: CreateFieldAssociationSchemeLinksBean | None = None
    name: StrictStr | None = None
