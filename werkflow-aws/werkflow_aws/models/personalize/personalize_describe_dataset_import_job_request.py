from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeDatasetImportJobRequest(BaseModel):
    datasetImportJobArn: StrictStr
