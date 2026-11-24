from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoIDPCreateUserImportJobRequest(BaseModel):
    JobName: StrictStr
    UserPoolId: StrictStr
    CloudWatchLogsRoleArn: StrictStr
    PasswordHashingAlgorithm: Literal['BCRYPT', 'SCRYPT', 'ARGON2ID', 'PBKDF2_SHA256'] | None = None
