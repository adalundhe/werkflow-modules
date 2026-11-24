from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_access_control_configuration import QuickSightAccessControlConfiguration
from .quick_sight_knowledge_base_configuration import QuickSightKnowledgeBaseConfiguration
from .quick_sight_media_extraction_configuration import QuickSightMediaExtractionConfiguration
from .quick_sight_resource_permission import QuickSightResourcePermission
from .quick_sight_tag import QuickSightTag


class QuickSightCreateKnowledgeBaseRequest(BaseModel):
    AwsAccountId: StrictStr
    KnowledgeBaseId: StrictStr
    Name: StrictStr
    DataSourceArn: StrictStr
    KnowledgeBaseConfiguration: QuickSightKnowledgeBaseConfiguration
    Description: StrictStr | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    MediaExtractionConfiguration: QuickSightMediaExtractionConfiguration | None = None
    AccessControlConfiguration: QuickSightAccessControlConfiguration | None = None
    PrimaryOwnerArn: StrictStr | None = None
    Tags: list[QuickSightTag] | None = None
