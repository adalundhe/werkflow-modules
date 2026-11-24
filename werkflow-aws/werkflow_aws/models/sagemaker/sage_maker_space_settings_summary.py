from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_space_storage_settings import SageMakerSpaceStorageSettings


class SageMakerSpaceSettingsSummary(BaseModel):
    AppType: StrictStr | None = None
    RemoteAccess: StrictStr | None = None
    SpaceStorageSettings: SageMakerSpaceStorageSettings | None = None
