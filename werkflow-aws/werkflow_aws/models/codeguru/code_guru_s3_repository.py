from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruS3Repository(BaseModel):
    Name: StrictStr
    BucketName: StrictStr
