from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsCodeBuildProjectArtifactsDetails(BaseModel):
    ArtifactIdentifier: StrictStr | None = None
    EncryptionDisabled: StrictBool | None = None
    Location: StrictStr | None = None
    Name: StrictStr | None = None
    NamespaceType: StrictStr | None = None
    OverrideArtifactName: StrictBool | None = None
    Packaging: StrictStr | None = None
    Path: StrictStr | None = None
    Type: StrictStr | None = None
