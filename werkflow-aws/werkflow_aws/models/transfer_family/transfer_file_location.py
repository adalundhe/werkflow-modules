from __future__ import annotations
from pydantic import BaseModel
from .transfer_efs_file_location import TransferEfsFileLocation
from .transfer_s3_file_location import TransferS3FileLocation


class TransferFileLocation(BaseModel):
    S3FileLocation: TransferS3FileLocation | None = None
    EfsFileLocation: TransferEfsFileLocation | None = None
