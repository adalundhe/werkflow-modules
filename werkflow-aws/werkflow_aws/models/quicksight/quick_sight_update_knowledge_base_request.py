from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_access_control_configuration import QuickSightAccessControlConfiguration
from .quick_sight_knowledge_base_configuration import QuickSightKnowledgeBaseConfiguration
from .quick_sight_media_extraction_configuration import QuickSightMediaExtractionConfiguration


class QuickSightUpdateKnowledgeBaseRequest(BaseModel):
    AwsAccountId: StrictStr
    KnowledgeBaseId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    KnowledgeBaseConfiguration: QuickSightKnowledgeBaseConfiguration | None = None
    MediaExtractionConfiguration: QuickSightMediaExtractionConfiguration | None = None
    IsEmailNotificationOptedForIngestionFailures: StrictBool | None = None
    AccessControlConfiguration: QuickSightAccessControlConfiguration | None = None
