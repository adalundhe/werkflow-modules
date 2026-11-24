from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2FlexCostAllocationPolicyAssociationDescription(BaseModel):
    FcaPolicyAssociationId: StrictStr | None = None
    FcaPolicyId: StrictStr | None = None
    NetworkResourceId: StrictStr | None = None
    OwnerAccount: StrictStr | None = None
    AssociatedAt: datetime.datetime | StrictStr | None = None
    ExpectedEffectiveAt: datetime.datetime | StrictStr | None = None
    AssociationMode: StrictStr | None = None
    ManagedBy: StrictStr | None = None
