from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSArgoCdAwsIdcConfigResponse(BaseModel):
    idcInstanceArn: StrictStr | None = None
    idcRegion: StrictStr | None = None
    idcManagedApplicationArn: StrictStr | None = None
