from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class Route53DomainsClient(ABC):

    @abstractmethod
    def accept_domain_transfer_from_another_aws_account(
        self,
        *,
        DomainName: str,
        Password: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_delegation_signer_to_domain(
        self,
        *,
        DomainName: str,
        SigningAttributes: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_domain_transfer_to_another_aws_account(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def check_domain_availability(
        self,
        *,
        DomainName: str,
        IdnLangCode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def check_domain_transferability(
        self,
        *,
        DomainName: str,
        AuthCode: str | None = None,
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
    def delete_tags_for_domain(
        self,
        *,
        DomainName: str,
        TagsToDelete: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_domain_auto_renew(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_domain_transfer_lock(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_delegation_signer_from_domain(
        self,
        *,
        DomainName: str,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_domain_auto_renew(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_domain_transfer_lock(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_contact_reachability_status(
        self,
        *,
        domainName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_detail(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_prices(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_suggestions(
        self,
        *,
        DomainName: str,
        SuggestionCount: int,
        OnlyAvailable: bool,
        OnlyStandardPrices: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_operation_detail(
        self,
        *,
        OperationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domains(
        self,
        *,
        FilterConditions: list[dict[str, Any]] | None = None,
        SortCondition: dict[str, Any] | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_operations(
        self,
        *,
        SubmittedSince: datetime.datetime | str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
        Status: list[str] | None = None,
        Type: list[str] | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_prices(
        self,
        *,
        Tld: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_domain(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def push_domain(
        self,
        *,
        DomainName: str,
        Target: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_domain(
        self,
        *,
        DomainName: str,
        DurationInYears: int,
        AdminContact: dict[str, Any],
        RegistrantContact: dict[str, Any],
        TechContact: dict[str, Any],
        IdnLangCode: str | None = None,
        AutoRenew: bool | None = None,
        PrivacyProtectAdminContact: bool | None = None,
        PrivacyProtectRegistrantContact: bool | None = None,
        PrivacyProtectTechContact: bool | None = None,
        BillingContact: dict[str, Any] | None = None,
        PrivacyProtectBillingContact: bool | None = None,
        Consent: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_domain_transfer_from_another_aws_account(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def renew_domain(
        self,
        *,
        DomainName: str,
        CurrentExpiryYear: int,
        DurationInYears: int | None = None,
        Consent: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resend_contact_reachability_email(
        self,
        *,
        domainName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resend_operation_authorization(
        self,
        *,
        OperationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_domain(
        self,
        *,
        DomainName: str,
        Consent: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def retrieve_domain_auth_code(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def transfer_domain(
        self,
        *,
        DomainName: str,
        AdminContact: dict[str, Any],
        RegistrantContact: dict[str, Any],
        TechContact: dict[str, Any],
        IdnLangCode: str | None = None,
        DurationInYears: int | None = None,
        Nameservers: list[dict[str, Any]] | None = None,
        AuthCode: str | None = None,
        AutoRenew: bool | None = None,
        PrivacyProtectAdminContact: bool | None = None,
        PrivacyProtectRegistrantContact: bool | None = None,
        PrivacyProtectTechContact: bool | None = None,
        BillingContact: dict[str, Any] | None = None,
        PrivacyProtectBillingContact: bool | None = None,
        Consent: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def transfer_domain_to_another_aws_account(
        self,
        *,
        DomainName: str,
        AccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_contact(
        self,
        *,
        DomainName: str,
        AdminContact: dict[str, Any] | None = None,
        RegistrantContact: dict[str, Any] | None = None,
        TechContact: dict[str, Any] | None = None,
        Consent: dict[str, Any] | None = None,
        BillingContact: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_contact_privacy(
        self,
        *,
        DomainName: str,
        AdminPrivacy: bool | None = None,
        RegistrantPrivacy: bool | None = None,
        TechPrivacy: bool | None = None,
        BillingPrivacy: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_nameservers(
        self,
        *,
        DomainName: str,
        Nameservers: list[dict[str, Any]],
        FIAuthKey: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_tags_for_domain(
        self,
        *,
        DomainName: str,
        TagsToUpdate: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def view_billing(
        self,
        *,
        Start: datetime.datetime | str | None = None,
        End: datetime.datetime | str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
