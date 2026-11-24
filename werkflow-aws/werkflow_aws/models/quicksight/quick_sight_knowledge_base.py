from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .quick_sight_access_control_configuration import QuickSightAccessControlConfiguration
from .quick_sight_knowledge_base_configuration import QuickSightKnowledgeBaseConfiguration
from .quick_sight_knowledge_base_ingestion_summary import QuickSightKnowledgeBaseIngestionSummary
from .quick_sight_media_extraction_configuration import QuickSightMediaExtractionConfiguration


class QuickSightKnowledgeBase(BaseModel):
    KnowledgeBaseArn: StrictStr | None = None
    KnowledgeBaseId: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    DataSourceArn: StrictStr | None = None
    KnowledgeBaseConfiguration: QuickSightKnowledgeBaseConfiguration | None = None
    MediaExtractionConfiguration: QuickSightMediaExtractionConfiguration | None = None
    AccessControlConfiguration: QuickSightAccessControlConfiguration | None = None
    Type: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    IsEmailNotificationOptedForIngestionFailures: StrictBool | None = None
    FirstCompletedIngestionSummary: QuickSightKnowledgeBaseIngestionSummary | None = None
    FirstIncompleteIngestionSummary: QuickSightKnowledgeBaseIngestionSummary | None = None
    LatestIngestionSummary: QuickSightKnowledgeBaseIngestionSummary | None = None
    KnowledgeBaseSizeBytes: StrictInt | None = None
    DocumentCount: StrictInt | None = None
    PrimaryOwnerArn: StrictStr | None = None
    PrimaryOwnerUsername: StrictStr | None = None
