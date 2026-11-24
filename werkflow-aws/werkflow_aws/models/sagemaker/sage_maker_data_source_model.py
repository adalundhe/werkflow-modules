from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_dataset_source_model import SageMakerDatasetSourceModel
from .sage_maker_file_system_data_source_model import SageMakerFileSystemDataSourceModel
from .sage_maker_s3_data_source_model import SageMakerS3DataSourceModel


class SageMakerDataSourceModel(BaseModel):
    S3DataSource: SageMakerS3DataSourceModel | None = None
    FileSystemDataSource: SageMakerFileSystemDataSourceModel | None = None
    DatasetSource: SageMakerDatasetSourceModel | None = None
