from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .aws_secrets_manager_secret_versions_list_entry import AWSSecretsManagerSecretVersionsListEntry


class AWSSecretsManagerListSecretVersionIdsResponse(BaseModel):
    Versions: list[AWSSecretsManagerSecretVersionsListEntry] | None = None
    NextToken: StrictStr | None = None
    ARN: StrictStr | None = None
    Name: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
