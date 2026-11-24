from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .rds_available_processor_feature import RDSAvailableProcessorFeature
from .rds_valid_additional_storage_options import RDSValidAdditionalStorageOptions
from .rds_valid_storage_options import RDSValidStorageOptions


class RDSValidDBInstanceModificationsMessage(BaseModel):
    Storage: list[RDSValidStorageOptions] | None = None
    ValidProcessorFeatures: list[RDSAvailableProcessorFeature] | None = None
    SupportsDedicatedLogVolume: StrictBool | None = None
    AdditionalStorage: RDSValidAdditionalStorageOptions | None = None
