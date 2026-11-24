from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMROnDemandCapacityReservationOptions(BaseModel):
    UsageStrategy: StrictStr | None = None
    CapacityReservationPreference: StrictStr | None = None
    CapacityReservationResourceGroupArn: StrictStr | None = None
