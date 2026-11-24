from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_processing_s3_compression_type import SageMakerProcessingS3CompressionType
from .sage_maker_processing_s3_data_distribution_type import SageMakerProcessingS3DataDistributionType
from .sage_maker_processing_s3_data_type import SageMakerProcessingS3DataType
from .sage_maker_processing_s3_input_mode import SageMakerProcessingS3InputMode


class SageMakerProcessingS3Input(BaseModel):
    S3Uri: StrictStr | None = None
    LocalPath: StrictStr | None = None
    S3DataType: SageMakerProcessingS3DataType | None = None
    S3InputMode: SageMakerProcessingS3InputMode | None = None
    S3DataDistributionType: SageMakerProcessingS3DataDistributionType | None = None
    S3CompressionType: SageMakerProcessingS3CompressionType | None = None
