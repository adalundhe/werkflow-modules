from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .document_db_tag import DocumentDBTag


class DocumentDBCreateEventSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SnsTopicArn: StrictStr
    SourceType: StrictStr | None = None
    EventCategories: list[StrictStr] | None = None
    SourceIds: list[StrictStr] | None = None
    Enabled: StrictBool | None = None
    Tags: list[DocumentDBTag] | None = None
