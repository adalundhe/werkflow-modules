from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .textract_adapters_config import TextractAdaptersConfig
from .textract_document_location import TextractDocumentLocation
from .textract_notification_channel import TextractNotificationChannel
from .textract_output_config import TextractOutputConfig
from .textract_queries_config import TextractQueriesConfig


class TextractStartDocumentAnalysisRequest(BaseModel):
    DocumentLocation: TextractDocumentLocation
    FeatureTypes: list[Literal['TABLES', 'FORMS', 'QUERIES', 'SIGNATURES', 'LAYOUT']]
    ClientRequestToken: StrictStr | None = None
    JobTag: StrictStr | None = None
    NotificationChannel: TextractNotificationChannel | None = None
    OutputConfig: TextractOutputConfig | None = None
    KMSKeyId: StrictStr | None = None
    QueriesConfig: TextractQueriesConfig | None = None
    AdaptersConfig: TextractAdaptersConfig | None = None
