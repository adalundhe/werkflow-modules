from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerDescribeResourceAssociationsRequest(BaseModel):
    SMCapacityReservationArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
