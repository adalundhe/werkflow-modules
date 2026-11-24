from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class TaxSettingsClient(ABC):

    @abstractmethod
    def batch_delete_tax_registration(
        self,
        *,
        accountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_tax_exemptions(
        self,
        *,
        accountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_put_tax_registration(
        self,
        *,
        accountIds: list[str],
        taxRegistrationEntry: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_supplemental_tax_registration(
        self,
        *,
        authorityId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tax_registration(
        self,
        *,
        accountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_tax_exemption_types(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_tax_inheritance(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_tax_registration(
        self,
        *,
        accountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_tax_registration_document(
        self,
        *,
        taxDocumentMetadata: dict[str, Any],
        destinationS3Location: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_supplemental_tax_registrations(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tax_exemptions(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tax_registrations(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_supplemental_tax_registration(
        self,
        *,
        taxRegistrationEntry: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_tax_exemption(
        self,
        *,
        accountIds: list[str],
        authority: dict[str, Any],
        exemptionType: str,
        exemptionCertificate: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_tax_inheritance(
        self,
        *,
        heritageStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_tax_registration(
        self,
        *,
        taxRegistrationEntry: dict[str, Any],
        accountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
