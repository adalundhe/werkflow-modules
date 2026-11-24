from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_athena_result_compression_type import SageMakerAthenaResultCompressionType
from .sage_maker_athena_result_format import SageMakerAthenaResultFormat


class SageMakerAthenaDatasetDefinition(BaseModel):
    Catalog: StrictStr | None = None
    Database: StrictStr | None = None
    QueryString: StrictStr | None = None
    WorkGroup: StrictStr | None = None
    OutputS3Uri: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    OutputFormat: SageMakerAthenaResultFormat | None = None
    OutputCompression: SageMakerAthenaResultCompressionType | None = None
