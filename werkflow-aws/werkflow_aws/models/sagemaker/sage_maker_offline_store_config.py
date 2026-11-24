from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_data_catalog_config import SageMakerDataCatalogConfig
from .sage_maker_s3_storage_config import SageMakerS3StorageConfig


class SageMakerOfflineStoreConfig(BaseModel):
    S3StorageConfig: SageMakerS3StorageConfig | None = None
    DisableGlueTableCreation: StrictBool | None = None
    DataCatalogConfig: SageMakerDataCatalogConfig | None = None
    TableFormat: StrictStr | None = None
