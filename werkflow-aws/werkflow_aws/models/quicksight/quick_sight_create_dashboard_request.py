from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_dashboard_publish_options import QuickSightDashboardPublishOptions
from .quick_sight_dashboard_source_entity import QuickSightDashboardSourceEntity
from .quick_sight_dashboard_version_definition import QuickSightDashboardVersionDefinition
from .quick_sight_link_sharing_configuration import QuickSightLinkSharingConfiguration
from .quick_sight_parameters import QuickSightParameters
from .quick_sight_resource_permission import QuickSightResourcePermission
from .quick_sight_tag import QuickSightTag
from .quick_sight_validation_strategy import QuickSightValidationStrategy


class QuickSightCreateDashboardRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    Name: StrictStr
    Parameters: QuickSightParameters | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    SourceEntity: QuickSightDashboardSourceEntity | None = None
    Tags: list[QuickSightTag] | None = None
    VersionDescription: StrictStr | None = None
    DashboardPublishOptions: QuickSightDashboardPublishOptions | None = None
    ThemeArn: StrictStr | None = None
    Definition: QuickSightDashboardVersionDefinition | None = None
    ValidationStrategy: QuickSightValidationStrategy | None = None
    FolderArns: list[StrictStr] | None = None
    LinkSharingConfiguration: QuickSightLinkSharingConfiguration | None = None
    LinkEntities: list[StrictStr] | None = None
