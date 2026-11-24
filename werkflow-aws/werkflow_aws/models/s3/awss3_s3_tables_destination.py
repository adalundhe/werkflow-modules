from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3S3TablesDestination(BaseModel):
    TableBucketArn: StrictStr
    TableName: StrictStr
