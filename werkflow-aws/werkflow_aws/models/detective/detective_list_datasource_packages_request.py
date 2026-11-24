from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DetectiveListDatasourcePackagesRequest(BaseModel):
    GraphArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
