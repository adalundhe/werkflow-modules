from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_efs_file_system import SageMakerEFSFileSystem
from .sage_maker_f_sx_lustre_file_system import SageMakerFSxLustreFileSystem
from .sage_maker_s3_file_system import SageMakerS3FileSystem


class SageMakerCustomFileSystem(BaseModel):
    EFSFileSystem: SageMakerEFSFileSystem | None = None
    FSxLustreFileSystem: SageMakerFSxLustreFileSystem | None = None
    S3FileSystem: SageMakerS3FileSystem | None = None
