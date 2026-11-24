from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_identity_center_configuration import QuickSightIdentityCenterConfiguration


class QuickSightAthenaParameters(BaseModel):
    WorkGroup: StrictStr | None = None
    RoleArn: StrictStr | None = None
    ConsumerAccountRoleArn: StrictStr | None = None
    IdentityCenterConfiguration: QuickSightIdentityCenterConfiguration | None = None
