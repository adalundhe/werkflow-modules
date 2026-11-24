from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .field_association_scheme_links_bean import FieldAssociationSchemeLinksBean
from .field_association_scheme_matched_filters import FieldAssociationSchemeMatchedFilters


class GetFieldAssociationSchemeResponse(BaseModel):
    description: StrictStr | None = None
    fieldsCount: StrictInt | None = None
    id: StrictInt | None = None
    isDefault: StrictBool | None = None
    links: FieldAssociationSchemeLinksBean | None = None
    matchedFilters: FieldAssociationSchemeMatchedFilters | None = None
    name: StrictStr | None = None
