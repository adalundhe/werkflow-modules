from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_document import QBusinessDocument


class QBusinessBatchPutDocumentRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    documents: list[QBusinessDocument]
    roleArn: StrictStr | None = None
    dataSourceSyncId: StrictStr | None = None
