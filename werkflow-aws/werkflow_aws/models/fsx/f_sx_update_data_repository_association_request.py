from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_s3_data_repository_configuration import FSxS3DataRepositoryConfiguration


class FSxUpdateDataRepositoryAssociationRequest(BaseModel):
    AssociationId: StrictStr
    ClientRequestToken: StrictStr | None = None
    ImportedFileChunkSize: StrictInt | None = None
    S3: FSxS3DataRepositoryConfiguration | None = None
