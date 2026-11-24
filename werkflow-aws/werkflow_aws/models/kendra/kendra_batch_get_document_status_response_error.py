from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraBatchGetDocumentStatusResponseError(BaseModel):
    DocumentId: StrictStr | None = None
    DataSourceId: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
