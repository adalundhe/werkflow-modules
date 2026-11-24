from __future__ import annotations
from .account_status_name import AccountStatusName
from .aws_account_status import AWSAccountStatus
from .organizations_account_status import OrganizationsAccountStatus


class OrganizationAccountStatusMap:

    def __init__(self):
        self._status_map: dict[
            AccountStatusName,
            OrganizationsAccountStatus,
        ] = {
            'active': OrganizationsAccountStatus.ACTIVE,
            'pending-closure': OrganizationsAccountStatus.PENDING_CLOSURE,
            'suspended': OrganizationsAccountStatus.SUSPENDED,
        }

        self._reverse_status_map: dict[
            AWSAccountStatus,
            AccountStatusName
        ] = {
            'ACTIVE': 'active',
            'PENDING_CLOSURE': 'pending-closure',
            'SUSPENDED': 'suspended'
        }

    def get(self, account_status: AccountStatusName):
        return self._status_map[account_status]
    
    def get_status_name(self, aws_account_status: AWSAccountStatus):
        return self._reverse_status_map[aws_account_status]
