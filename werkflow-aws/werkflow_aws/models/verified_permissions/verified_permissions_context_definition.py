from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_attribute_value import VerifiedPermissionsAttributeValue


class VerifiedPermissionsContextDefinition(BaseModel):
    contextMap: dict[StrictStr, VerifiedPermissionsAttributeValue] | None = None
    cedarJson: StrictStr | None = None
