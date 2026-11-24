from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lake_formation_data_lake_settings import LakeFormationDataLakeSettings


class LakeFormationGetDataLakeSettingsResponse(BaseModel):
    DataLakeSettings: LakeFormationDataLakeSettings | None = None
    ResponseMetadata: dict[str, Any] | None = None
