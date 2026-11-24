from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_capacity_reservation_resource_association import SageMakerCapacityReservationResourceAssociation


class SageMakerDescribeResourceAssociationsResponse(BaseModel):
    SMCapacityReservationArn: StrictStr | None = None
    SMCapacityReservationId: StrictStr | None = None
    ResourceAssociations: list[SageMakerCapacityReservationResourceAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
