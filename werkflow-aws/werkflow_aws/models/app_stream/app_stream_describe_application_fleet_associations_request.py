from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamDescribeApplicationFleetAssociationsRequest(BaseModel):
    FleetName: StrictStr | None = None
    ApplicationArn: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
