from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerRedshiftDatasetDefinitionModel(BaseModel):
    ClusterId: StrictStr | None = None
    Database: StrictStr | None = None
    DbUser: StrictStr | None = None
    QueryString: StrictStr | None = None
    ClusterRoleArn: StrictStr | None = None
    OutputS3Uri: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    OutputFormat: StrictStr | None = None
    OutputCompression: StrictStr | None = None
