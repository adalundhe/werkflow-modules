from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSArgoCdAwsIdcConfigRequest(BaseModel):
    idcInstanceArn: StrictStr
    idcRegion: StrictStr | None = None
