from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_namespace_error import QuickSightNamespaceError


class QuickSightNamespaceInfoV2(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    CapacityRegion: StrictStr | None = None
    CreationStatus: StrictStr | None = None
    IdentityStore: StrictStr | None = None
    NamespaceError: QuickSightNamespaceError | None = None
    IamIdentityCenterApplicationArn: StrictStr | None = None
    IamIdentityCenterInstanceArn: StrictStr | None = None
