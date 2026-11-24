from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails(BaseModel):
    MinimumInstanceMetadataServiceVersion: StrictStr | None = None
