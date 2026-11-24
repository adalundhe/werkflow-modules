from __future__ import annotations
from pydantic import BaseModel
from .firehose_secrets_manager_configuration import FirehoseSecretsManagerConfiguration


class FirehoseDatabaseSourceAuthenticationConfiguration(BaseModel):
    SecretsManagerConfiguration: FirehoseSecretsManagerConfiguration | None = None
