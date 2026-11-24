from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRPutImageRequest(BaseModel):
    repositoryName: StrictStr
    imageManifest: StrictStr
    registryId: StrictStr | None = None
    imageManifestMediaType: StrictStr | None = None
    imageTag: StrictStr | None = None
    imageDigest: StrictStr | None = None
