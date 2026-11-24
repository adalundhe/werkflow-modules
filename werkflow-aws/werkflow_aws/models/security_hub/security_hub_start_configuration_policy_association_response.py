from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class SecurityHubStartConfigurationPolicyAssociationResponse(BaseModel):
    ConfigurationPolicyId: StrictStr | None = None
    TargetId: StrictStr | None = None
    TargetType: StrictStr | None = None
    AssociationType: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    AssociationStatus: StrictStr | None = None
    AssociationStatusMessage: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
