from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .field_association_scheme_links import FieldAssociationSchemeLinks


class GetFieldAssociationSchemeByIdResponse(BaseModel):
    description: StrictStr | None = None
    fieldsCount: StrictInt | None = None
    id: StrictStr | None = None
    isDefault: StrictBool | None = None
    links: FieldAssociationSchemeLinks | None = None
    name: StrictStr | None = None
