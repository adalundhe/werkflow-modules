from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceConnectorSummary(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    provider: StrictStr | None = None
    tenantIdentifier: StrictStr | None = None
    gcpOrganizationId: StrictStr | None = None
    serviceAccountEmail: StrictStr | None = None
    createdTime: datetime.datetime | StrictStr | None = None
