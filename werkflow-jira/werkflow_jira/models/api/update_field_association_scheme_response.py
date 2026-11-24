from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .update_field_association_scheme_links_bean import UpdateFieldAssociationSchemeLinksBean


class UpdateFieldAssociationSchemeResponse(BaseModel):
    description: StrictStr | None = None
    id: StrictInt | None = None
    links: UpdateFieldAssociationSchemeLinksBean | None = None
    name: StrictStr | None = None
