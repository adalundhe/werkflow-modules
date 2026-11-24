from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from typing import Literal
from .aws_secrets_manager_filter import AWSSecretsManagerFilter


class AWSSecretsManagerListSecretsRequest(BaseModel):
    IncludePlannedDeletion: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[AWSSecretsManagerFilter] | None = None
    SortOrder: Literal['asc', 'desc'] | None = None
    SortBy: Literal['created-date', 'last-accessed-date', 'last-changed-date', 'name'] | None = None
