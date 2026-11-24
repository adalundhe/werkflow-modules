from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_intelligent_tiering_filter import AWSS3IntelligentTieringFilter
from .awss3_tiering import AWSS3Tiering


class AWSS3IntelligentTieringConfiguration(BaseModel):
    Id: StrictStr | None = None
    Filter: AWSS3IntelligentTieringFilter | None = None
    Status: StrictStr | None = None
    Tierings: list[AWSS3Tiering] | None = None
