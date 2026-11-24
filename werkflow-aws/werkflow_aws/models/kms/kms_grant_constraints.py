from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSGrantConstraints(BaseModel):
    EncryptionContextSubset: dict[StrictStr, StrictStr] | None = None
    EncryptionContextEquals: dict[StrictStr, StrictStr] | None = None
    SourceArn: StrictStr | None = None
