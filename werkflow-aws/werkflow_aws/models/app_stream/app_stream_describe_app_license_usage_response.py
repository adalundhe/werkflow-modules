from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_admin_app_license_usage_record import AppStreamAdminAppLicenseUsageRecord


class AppStreamDescribeAppLicenseUsageResponse(BaseModel):
    AppLicenseUsages: list[AppStreamAdminAppLicenseUsageRecord] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
