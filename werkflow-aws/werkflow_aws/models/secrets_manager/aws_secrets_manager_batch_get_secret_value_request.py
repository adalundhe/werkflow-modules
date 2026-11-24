from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .aws_secrets_manager_filter_model import AWSSecretsManagerFilterModel


class AWSSecretsManagerBatchGetSecretValueRequest(BaseModel):
    SecretIdList: list[StrictStr] | None = None
    Filters: list[AWSSecretsManagerFilterModel] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
