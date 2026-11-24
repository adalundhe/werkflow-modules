from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_data_lake_settings import LakeFormationDataLakeSettings


class LakeFormationPutDataLakeSettingsRequest(BaseModel):
    DataLakeSettings: LakeFormationDataLakeSettings
    CatalogId: StrictStr | None = None
