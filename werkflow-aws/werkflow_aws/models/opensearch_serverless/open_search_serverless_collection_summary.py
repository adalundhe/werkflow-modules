from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessCollectionSummary(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    arn: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
    collectionGroupName: StrictStr | None = None
