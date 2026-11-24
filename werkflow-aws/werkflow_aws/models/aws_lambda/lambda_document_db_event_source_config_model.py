from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaDocumentDBEventSourceConfigModel(BaseModel):
    DatabaseName: StrictStr | None = None
    CollectionName: StrictStr | None = None
    FullDocument: StrictStr | None = None
