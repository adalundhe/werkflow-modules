from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerValidationErrorsEntry(BaseModel):
    CheckName: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
