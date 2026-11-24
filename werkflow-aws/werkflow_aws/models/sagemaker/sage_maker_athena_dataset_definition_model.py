from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAthenaDatasetDefinitionModel(BaseModel):
    Catalog: StrictStr | None = None
    Database: StrictStr | None = None
    QueryString: StrictStr | None = None
    WorkGroup: StrictStr | None = None
    OutputS3Uri: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    OutputFormat: StrictStr | None = None
    OutputCompression: StrictStr | None = None
