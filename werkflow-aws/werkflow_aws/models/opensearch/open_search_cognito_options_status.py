from __future__ import annotations
from pydantic import BaseModel
from .open_search_cognito_options import OpenSearchCognitoOptions
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchCognitoOptionsStatus(BaseModel):
    Options: OpenSearchCognitoOptions | None = None
    Status: OpenSearchOptionStatus | None = None
