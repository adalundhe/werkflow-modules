from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceScope(BaseModel):
    ComplianceResourceTypes: list[StrictStr] | None = None
    TagKey: StrictStr | None = None
    TagValue: StrictStr | None = None
    ComplianceResourceId: StrictStr | None = None
    ServicePrincipals: list[StrictStr] | None = None
