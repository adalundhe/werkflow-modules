from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .aws_secrets_manager_secret_list_entry import AWSSecretsManagerSecretListEntry


class AWSSecretsManagerListSecretsResponse(BaseModel):
    SecretList: list[AWSSecretsManagerSecretListEntry] | None = None
    NextToken: StrictStr | None = None
