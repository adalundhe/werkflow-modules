from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DataZoneListRulesRequest(BaseModel):
    domainIdentifier: StrictStr
    targetType: Literal['DOMAIN_UNIT']
    targetIdentifier: StrictStr
    ruleType: Literal['METADATA_FORM_ENFORCEMENT', 'GLOSSARY_TERM_ENFORCEMENT'] | None = None
    action: Literal['CREATE_LISTING_CHANGE_SET', 'CREATE_SUBSCRIPTION_REQUEST'] | None = None
    projectIds: list[StrictStr] | None = None
    assetTypes: list[StrictStr] | None = None
    dataProduct: StrictBool | None = None
    includeCascaded: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
