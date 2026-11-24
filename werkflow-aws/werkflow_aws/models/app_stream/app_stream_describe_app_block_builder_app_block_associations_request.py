from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamDescribeAppBlockBuilderAppBlockAssociationsRequest(BaseModel):
    AppBlockArn: StrictStr | None = None
    AppBlockBuilderName: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
