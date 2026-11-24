from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeBuildBuildArtifacts(BaseModel):
    location: StrictStr | None = None
    sha256sum: StrictStr | None = None
    md5sum: StrictStr | None = None
    overrideArtifactName: StrictBool | None = None
    encryptionDisabled: StrictBool | None = None
    artifactIdentifier: StrictStr | None = None
    bucketOwnerAccess: StrictStr | None = None
