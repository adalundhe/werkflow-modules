from __future__ import annotations

from botocore.paginate import Paginator
from abc import ABC, abstractmethod
from typing import Any


class MSKClient(ABC):

    @abstractmethod
    def list_clusters(
        self,     
        ClusterNameFilter: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
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