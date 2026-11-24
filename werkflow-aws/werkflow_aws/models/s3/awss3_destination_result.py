from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3DestinationResult(BaseModel):
    TableBucketType: StrictStr | None = None
    TableBucketArn: StrictStr | None = None
    TableNamespace: StrictStr | None = None
