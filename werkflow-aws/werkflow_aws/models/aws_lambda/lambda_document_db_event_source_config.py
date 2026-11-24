from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_full_document import LambdaFullDocument


class LambdaDocumentDBEventSourceConfig(BaseModel):
    DatabaseName: StrictStr | None = None
    CollectionName: StrictStr | None = None
    FullDocument: LambdaFullDocument | None = None
