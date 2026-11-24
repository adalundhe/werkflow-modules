from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RekognitionListDatasetEntriesRequest(BaseModel):
    DatasetArn: StrictStr
    ContainsLabels: list[StrictStr] | None = None
    Labeled: StrictBool | None = None
    SourceRefContains: StrictStr | None = None
    HasErrors: StrictBool | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
