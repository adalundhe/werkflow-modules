from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcrContainerImageDetails(BaseModel):
    RegistryId: StrictStr | None = None
    RepositoryName: StrictStr | None = None
    Architecture: StrictStr | None = None
    ImageDigest: StrictStr | None = None
    ImageTags: list[StrictStr] | None = None
    ImagePublishedAt: StrictStr | None = None
