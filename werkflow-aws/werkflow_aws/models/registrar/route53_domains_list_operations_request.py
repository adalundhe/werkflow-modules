from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class Route53DomainsListOperationsRequest(BaseModel):
    SubmittedSince: datetime.datetime | StrictStr | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Status: list[Literal['SUBMITTED', 'IN_PROGRESS', 'ERROR', 'SUCCESSFUL', 'FAILED']] | None = None
    Type: list[Literal['REGISTER_DOMAIN', 'DELETE_DOMAIN', 'TRANSFER_IN_DOMAIN', 'UPDATE_DOMAIN_CONTACT', 'UPDATE_NAMESERVER', 'CHANGE_PRIVACY_PROTECTION', 'DOMAIN_LOCK', 'ENABLE_AUTORENEW', 'DISABLE_AUTORENEW', 'ADD_DNSSEC', 'REMOVE_DNSSEC', 'EXPIRE_DOMAIN', 'TRANSFER_OUT_DOMAIN', 'CHANGE_DOMAIN_OWNER', 'RENEW_DOMAIN', 'PUSH_DOMAIN', 'INTERNAL_TRANSFER_OUT_DOMAIN', 'INTERNAL_TRANSFER_IN_DOMAIN', 'RELEASE_TO_GANDI', 'TRANSFER_ON_RENEW', 'RESTORE_DOMAIN']] | None = None
    SortBy: Literal['SubmittedDate'] | None = None
    SortOrder: Literal['ASC', 'DESC'] | None = None
