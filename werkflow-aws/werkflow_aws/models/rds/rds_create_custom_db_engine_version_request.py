from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateCustomDBEngineVersionRequest(BaseModel):
    Engine: StrictStr
    EngineVersion: StrictStr
    DatabaseInstallationFilesS3BucketName: StrictStr | None = None
    DatabaseInstallationFilesS3Prefix: StrictStr | None = None
    DatabaseInstallationFiles: list[StrictStr] | None = None
    ImageId: StrictStr | None = None
    KMSKeyId: StrictStr | None = None
    SourceCustomDbEngineVersionIdentifier: StrictStr | None = None
    UseAwsProvidedLatestImage: StrictBool | None = None
    Description: StrictStr | None = None
    Manifest: StrictStr | None = None
    Tags: list[RDSTagModel] | None = None
