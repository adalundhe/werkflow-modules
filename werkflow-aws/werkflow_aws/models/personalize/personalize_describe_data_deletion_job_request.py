from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeDataDeletionJobRequest(BaseModel):
    dataDeletionJobArn: StrictStr
