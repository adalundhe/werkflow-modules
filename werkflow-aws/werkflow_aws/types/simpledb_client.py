from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class SimpleDBClient(ABC):

    @abstractmethod
    def batch_delete_attributes(
        self,
        *,
        DomainName: str,
        Items: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_put_attributes(
        self,
        *,
        DomainName: str,
        Items: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_attributes(
        self,
        *,
        DomainName: str,
        ItemName: str,
        Attributes: list[dict[str, Any]] | None = None,
        Expected: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def domain_metadata(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_attributes(
        self,
        *,
        DomainName: str,
        ItemName: str,
        AttributeNames: list[str] | None = None,
        ConsistentRead: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domains(
        self,
        *,
        MaxNumberOfDomains: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_attributes(
        self,
        *,
        DomainName: str,
        ItemName: str,
        Attributes: list[dict[str, Any]],
        Expected: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def select(
        self,
        *,
        SelectExpression: str,
        NextToken: str | None = None,
        ConsistentRead: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
