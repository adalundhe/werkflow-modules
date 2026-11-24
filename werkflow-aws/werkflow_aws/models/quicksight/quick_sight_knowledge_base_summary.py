from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightKnowledgeBaseSummary(BaseModel):
    KnowledgeBaseArn: StrictStr | None = None
    KnowledgeBaseId: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    DataSourceArn: StrictStr | None = None
    Type: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    KnowledgeBaseSizeBytes: StrictInt | None = None
    DocumentCount: StrictInt | None = None
    PrimaryOwnerArn: StrictStr | None = None
    PrimaryOwnerUsername: StrictStr | None = None
