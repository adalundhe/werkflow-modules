from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_entity_item import VerifiedPermissionsEntityItem


class VerifiedPermissionsEntitiesDefinition(BaseModel):
    entityList: list[VerifiedPermissionsEntityItem] | None = None
    cedarJson: StrictStr | None = None
