from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_dashboard_error import QuickSightDashboardError
from .quick_sight_dashboard_publish_options import QuickSightDashboardPublishOptions
from .quick_sight_dashboard_version_definition import QuickSightDashboardVersionDefinition


class QuickSightDescribeDashboardDefinitionResponse(BaseModel):
    DashboardId: StrictStr | None = None
    Errors: list[QuickSightDashboardError] | None = None
    Name: StrictStr | None = None
    ResourceStatus: StrictStr | None = None
    ThemeArn: StrictStr | None = None
    Definition: QuickSightDashboardVersionDefinition | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    DashboardPublishOptions: QuickSightDashboardPublishOptions | None = None
    ResponseMetadata: dict[str, Any] | None = None
