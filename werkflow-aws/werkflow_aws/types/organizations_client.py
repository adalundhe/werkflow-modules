from abc import ABC, abstractmethod
from typing import Any

from botocore.paginate import Paginator


class OrganizationsClient(ABC):

    @abstractmethod
    def list_accounts(
        self,
        NextToken: str | None = None,
        MaxResults: int | None = None
    ) -> dict[str, Any]:
        pass
    
    @abstractmethod
    def get_paginator(
        self,
        Operation: str,
    ) -> Paginator:
        pass

    @abstractmethod
    def close(self):
        pass