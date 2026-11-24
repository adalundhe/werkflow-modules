from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class MacieGetAutomatedDiscoveryConfigurationResponse(BaseModel):
    autoEnableOrganizationMembers: StrictStr | None = None
    classificationScopeId: StrictStr | None = None
    disabledAt: datetime.datetime | StrictStr | None = None
    firstEnabledAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    sensitivityInspectionTemplateId: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
