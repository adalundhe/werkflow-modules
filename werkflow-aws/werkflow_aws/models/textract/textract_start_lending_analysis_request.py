from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .textract_document_location import TextractDocumentLocation
from .textract_notification_channel import TextractNotificationChannel
from .textract_output_config import TextractOutputConfig


class TextractStartLendingAnalysisRequest(BaseModel):
    DocumentLocation: TextractDocumentLocation
    ClientRequestToken: StrictStr | None = None
    JobTag: StrictStr | None = None
    NotificationChannel: TextractNotificationChannel | None = None
    OutputConfig: TextractOutputConfig | None = None
    KMSKeyId: StrictStr | None = None
