from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionListDatasetLabelsRequest(BaseModel):
    DatasetArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
