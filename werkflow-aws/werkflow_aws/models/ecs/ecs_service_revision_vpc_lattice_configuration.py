from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSServiceRevisionVpcLatticeConfiguration(BaseModel):
    targetGroupArn: StrictStr | None = None
    productionListenerRule: StrictStr | None = None
