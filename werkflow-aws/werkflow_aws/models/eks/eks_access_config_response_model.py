from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EKSAccessConfigResponseModel(BaseModel):
    bootstrapClusterCreatorAdminPermissions: StrictBool | None = None
    authenticationMode: StrictStr | None = None
