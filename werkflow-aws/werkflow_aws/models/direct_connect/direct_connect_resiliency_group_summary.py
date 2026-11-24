from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectResiliencyGroupSummary(BaseModel):
    resiliencyGroupId: StrictStr | None = None
    resiliencyGroupArn: StrictStr | None = None
    resiliencyGroupName: StrictStr | None = None
    resiliencyGroupType: StrictStr | None = None
    ownerAccount: StrictStr | None = None
    state: StrictStr | None = None
