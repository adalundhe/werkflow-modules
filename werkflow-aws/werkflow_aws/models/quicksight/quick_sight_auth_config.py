from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .quick_sight_authentication_metadata import QuickSightAuthenticationMetadata


class QuickSightAuthConfig(BaseModel):
    AuthenticationType: Literal['BASIC', 'API_KEY', 'OAUTH2_CLIENT_CREDENTIALS', 'NONE', 'IAM', 'OAUTH2_AUTHORIZATION_CODE']
    AuthenticationMetadata: QuickSightAuthenticationMetadata
