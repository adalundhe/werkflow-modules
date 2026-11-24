from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AlternatePathHint(BaseModel):
    ComponentId: StrictStr | None = None
    ComponentArn: StrictStr | None = None
