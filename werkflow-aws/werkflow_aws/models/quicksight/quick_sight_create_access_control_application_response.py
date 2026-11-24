from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_quick_authentication_config_create_output import QuickSightQuickAuthenticationConfigCreateOutput


class QuickSightCreateAccessControlApplicationResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ApplicationId: StrictStr | None = None
    Arn: StrictStr | None = None
    AccessControlApplicationStatus: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    TenantUrl: StrictStr | None = None
    IdcApplicationArn: StrictStr | None = None
    QuickAuthenticationConfiguration: QuickSightQuickAuthenticationConfigCreateOutput | None = None
    ResponseMetadata: dict[str, Any] | None = None
