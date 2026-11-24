from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_tag import SESTag
from .ses_tenant_suppression_attributes import SESTenantSuppressionAttributes


class SESCreateTenantResponse(BaseModel):
    TenantName: StrictStr | None = None
    TenantId: StrictStr | None = None
    TenantArn: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    Tags: list[SESTag] | None = None
    SendingStatus: StrictStr | None = None
    SuppressionAttributes: SESTenantSuppressionAttributes | None = None
    ResponseMetadata: dict[str, Any] | None = None
