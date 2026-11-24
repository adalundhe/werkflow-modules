from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails(BaseModel):
    ReadOnly: StrictBool | None = None
    SourceContainer: StrictStr | None = None
