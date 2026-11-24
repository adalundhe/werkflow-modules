from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectResiliencyGroupAssociation(BaseModel):
    resiliencyGroupId: StrictStr | None = None
    connectionArn: StrictStr | None = None
    state: StrictStr | None = None
