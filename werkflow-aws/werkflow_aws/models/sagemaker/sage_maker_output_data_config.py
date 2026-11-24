from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_output_compression_type import SageMakerOutputCompressionType


class SageMakerOutputDataConfig(BaseModel):
    KmsKeyId: StrictStr | None = None
    S3OutputPath: StrictStr | None = None
    CompressionType: SageMakerOutputCompressionType | None = None
