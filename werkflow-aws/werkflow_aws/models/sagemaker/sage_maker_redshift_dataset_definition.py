from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_redshift_result_compression_type import SageMakerRedshiftResultCompressionType
from .sage_maker_redshift_result_format import SageMakerRedshiftResultFormat


class SageMakerRedshiftDatasetDefinition(BaseModel):
    ClusterId: StrictStr | None = None
    Database: StrictStr | None = None
    DbUser: StrictStr | None = None
    QueryString: StrictStr | None = None
    ClusterRoleArn: StrictStr | None = None
    OutputS3Uri: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    OutputFormat: SageMakerRedshiftResultFormat | None = None
    OutputCompression: SageMakerRedshiftResultCompressionType | None = None
