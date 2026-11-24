from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_efs_file_system_config import SageMakerEFSFileSystemConfig
from .sage_maker_f_sx_lustre_file_system_config import SageMakerFSxLustreFileSystemConfig
from .sage_maker_s3_file_system_config import SageMakerS3FileSystemConfig


class SageMakerCustomFileSystemConfig(BaseModel):
    EFSFileSystemConfig: SageMakerEFSFileSystemConfig | None = None
    FSxLustreFileSystemConfig: SageMakerFSxLustreFileSystemConfig | None = None
    S3FileSystemConfig: SageMakerS3FileSystemConfig | None = None
