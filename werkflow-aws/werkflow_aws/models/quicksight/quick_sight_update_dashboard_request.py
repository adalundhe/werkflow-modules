from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_dashboard_publish_options import QuickSightDashboardPublishOptions
from .quick_sight_dashboard_source_entity import QuickSightDashboardSourceEntity
from .quick_sight_dashboard_version_definition import QuickSightDashboardVersionDefinition
from .quick_sight_parameters import QuickSightParameters
from .quick_sight_validation_strategy import QuickSightValidationStrategy


class QuickSightUpdateDashboardRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    Name: StrictStr
    SourceEntity: QuickSightDashboardSourceEntity | None = None
    Parameters: QuickSightParameters | None = None
    VersionDescription: StrictStr | None = None
    DashboardPublishOptions: QuickSightDashboardPublishOptions | None = None
    ThemeArn: StrictStr | None = None
    Definition: QuickSightDashboardVersionDefinition | None = None
    ValidationStrategy: QuickSightValidationStrategy | None = None
