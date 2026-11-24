from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMRelatedOpsItem(BaseModel):
    OpsItemId: StrictStr | None = None
