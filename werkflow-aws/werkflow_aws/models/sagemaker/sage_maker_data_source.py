from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_dataset_source import SageMakerDatasetSource
from .sage_maker_file_system_data_source import SageMakerFileSystemDataSource
from .sage_maker_s3_data_source import SageMakerS3DataSource


class SageMakerDataSource(BaseModel):
    S3DataSource: SageMakerS3DataSource | None = None
    FileSystemDataSource: SageMakerFileSystemDataSource | None = None
    DatasetSource: SageMakerDatasetSource | None = None
