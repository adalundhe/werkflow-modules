from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListPolicyGrantsRequest(BaseModel):
    domainIdentifier: StrictStr
    entityType: Literal['DOMAIN_UNIT', 'ENVIRONMENT_BLUEPRINT_CONFIGURATION', 'ENVIRONMENT_PROFILE', 'ASSET_TYPE']
    entityIdentifier: StrictStr
    policyType: Literal['CREATE_DOMAIN_UNIT', 'OVERRIDE_DOMAIN_UNIT_OWNERS', 'ADD_TO_PROJECT_MEMBER_POOL', 'OVERRIDE_PROJECT_OWNERS', 'CREATE_GLOSSARY', 'CREATE_FORM_TYPE', 'CREATE_ASSET_TYPE', 'CREATE_PROJECT', 'CREATE_ENVIRONMENT_PROFILE', 'DELEGATE_CREATE_ENVIRONMENT_PROFILE', 'CREATE_ENVIRONMENT', 'CREATE_ENVIRONMENT_FROM_BLUEPRINT', 'CREATE_PROJECT_FROM_PROJECT_PROFILE', 'USE_ASSET_TYPE']
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
