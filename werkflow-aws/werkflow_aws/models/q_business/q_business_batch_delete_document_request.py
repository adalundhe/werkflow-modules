from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_delete_document import QBusinessDeleteDocument


class QBusinessBatchDeleteDocumentRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    documents: list[QBusinessDeleteDocument]
    dataSourceSyncId: StrictStr | None = None
