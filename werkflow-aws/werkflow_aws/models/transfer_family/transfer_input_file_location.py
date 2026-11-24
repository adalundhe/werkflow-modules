from __future__ import annotations
from pydantic import BaseModel
from .transfer_efs_file_location import TransferEfsFileLocation
from .transfer_s3_input_file_location import TransferS3InputFileLocation


class TransferInputFileLocation(BaseModel):
    S3FileLocation: TransferS3InputFileLocation | None = None
    EfsFileLocation: TransferEfsFileLocation | None = None
