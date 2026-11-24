from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeUpdateDatasetRequest(BaseModel):
    datasetArn: StrictStr
    schemaArn: StrictStr
