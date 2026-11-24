from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_s3_presign import SageMakerS3Presign


class SageMakerWorkerAccessConfiguration(BaseModel):
    S3Presign: SageMakerS3Presign | None = None
