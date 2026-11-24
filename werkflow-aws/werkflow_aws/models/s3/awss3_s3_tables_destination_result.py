from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3S3TablesDestinationResult(BaseModel):
    TableBucketArn: StrictStr | None = None
    TableName: StrictStr | None = None
    TableArn: StrictStr | None = None
    TableNamespace: StrictStr | None = None
