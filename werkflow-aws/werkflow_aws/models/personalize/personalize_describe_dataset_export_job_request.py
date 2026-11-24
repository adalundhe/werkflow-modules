from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeDatasetExportJobRequest(BaseModel):
    datasetExportJobArn: StrictStr
