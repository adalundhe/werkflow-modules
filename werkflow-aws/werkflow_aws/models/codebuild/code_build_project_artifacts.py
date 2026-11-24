from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeBuildProjectArtifacts(BaseModel):
    type: StrictStr | None = None
    location: StrictStr | None = None
    path: StrictStr | None = None
    namespaceType: StrictStr | None = None
    name: StrictStr | None = None
    packaging: StrictStr | None = None
    overrideArtifactName: StrictBool | None = None
    encryptionDisabled: StrictBool | None = None
    artifactIdentifier: StrictStr | None = None
    bucketOwnerAccess: StrictStr | None = None
