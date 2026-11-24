from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr


class CodeArtifactPublishPackageVersionRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    domain: StrictStr
    repository: StrictStr
    format: Literal['npm', 'pypi', 'maven', 'nuget', 'generic', 'ruby', 'swift', 'cargo']
    package: StrictStr
    packageVersion: StrictStr
    assetContent: StrictBytes | BinaryIO | StrictStr
    assetName: StrictStr
    assetSHA256: StrictStr
    domainOwner: StrictStr | None = None
    namespace: StrictStr | None = None
    unfinished: StrictBool | None = None
