from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerIdentityProviderOAuthSetting(BaseModel):
    DataSourceName: StrictStr | None = None
    Status: StrictStr | None = None
    SecretArn: StrictStr | None = None
