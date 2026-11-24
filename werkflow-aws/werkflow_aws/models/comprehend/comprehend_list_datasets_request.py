from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_dataset_filter import ComprehendDatasetFilter


class ComprehendListDatasetsRequest(BaseModel):
    FlywheelArn: StrictStr | None = None
    Filter: ComprehendDatasetFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
