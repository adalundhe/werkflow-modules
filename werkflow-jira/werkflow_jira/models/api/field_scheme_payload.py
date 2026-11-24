from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .field_association_item_payload import FieldAssociationItemPayload
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class FieldSchemePayload(BaseModel):
    description: StrictStr | None = None
    items: list[FieldAssociationItemPayload] | None = None
    name: StrictStr | None = None
    onConflict: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
