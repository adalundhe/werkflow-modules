from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DocumentDBDBClusterMember(BaseModel):
    DBInstanceIdentifier: StrictStr | None = None
    IsClusterWriter: StrictBool | None = None
    DBClusterParameterGroupStatus: StrictStr | None = None
    PromotionTier: StrictInt | None = None
