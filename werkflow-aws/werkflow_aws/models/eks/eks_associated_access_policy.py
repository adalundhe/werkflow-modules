from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .eks_access_scope import EKSAccessScope


class EKSAssociatedAccessPolicy(BaseModel):
    policyArn: StrictStr | None = None
    accessScope: EKSAccessScope | None = None
    associatedAt: datetime.datetime | StrictStr | None = None
    modifiedAt: datetime.datetime | StrictStr | None = None
