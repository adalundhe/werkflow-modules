from werkflow_aws.models.registrar import (
    Route53DomainsAcceptDomainTransferFromAnotherAwsAccountRequest,
    Route53DomainsAcceptDomainTransferFromAnotherAwsAccountResponse,
    Route53DomainsAssociateDelegationSignerToDomainRequest,
    Route53DomainsAssociateDelegationSignerToDomainResponse,
    Route53DomainsCancelDomainTransferToAnotherAwsAccountRequest,
    Route53DomainsCancelDomainTransferToAnotherAwsAccountResponse,
    Route53DomainsCheckDomainAvailabilityRequest,
    Route53DomainsCheckDomainAvailabilityResponse,
    Route53DomainsCheckDomainTransferabilityRequest,
    Route53DomainsCheckDomainTransferabilityResponse,
    Route53DomainsDeleteDomainRequest,
    Route53DomainsDeleteDomainResponse,
    Route53DomainsDeleteTagsForDomainRequest,
    Route53DomainsDeleteTagsForDomainResponse,
    Route53DomainsDisableDomainAutoRenewRequest,
    Route53DomainsDisableDomainAutoRenewResponse,
    Route53DomainsDisableDomainTransferLockRequest,
    Route53DomainsDisableDomainTransferLockResponse,
    Route53DomainsDisassociateDelegationSignerFromDomainRequest,
    Route53DomainsDisassociateDelegationSignerFromDomainResponse,
    Route53DomainsEnableDomainAutoRenewRequest,
    Route53DomainsEnableDomainAutoRenewResponse,
    Route53DomainsEnableDomainTransferLockRequest,
    Route53DomainsEnableDomainTransferLockResponse,
    Route53DomainsGetContactReachabilityStatusRequest,
    Route53DomainsGetContactReachabilityStatusResponse,
    Route53DomainsGetDomainDetailRequest,
    Route53DomainsGetDomainDetailResponse,
    Route53DomainsGetDomainPricesRequest,
    Route53DomainsGetDomainPricesResponse,
    Route53DomainsGetDomainSuggestionsRequest,
    Route53DomainsGetDomainSuggestionsResponse,
    Route53DomainsGetOperationDetailRequest,
    Route53DomainsGetOperationDetailResponse,
    Route53DomainsListDomainsRequest,
    Route53DomainsListDomainsResponse,
    Route53DomainsListOperationsRequest,
    Route53DomainsListOperationsResponse,
    Route53DomainsListPricesRequest,
    Route53DomainsListPricesResponse,
    Route53DomainsListTagsForDomainRequest,
    Route53DomainsListTagsForDomainResponse,
    Route53DomainsPushDomainRequest,
    Route53DomainsPushDomainResponse,
    Route53DomainsRegisterDomainRequest,
    Route53DomainsRegisterDomainResponse,
    Route53DomainsRejectDomainTransferFromAnotherAwsAccountRequest,
    Route53DomainsRejectDomainTransferFromAnotherAwsAccountResponse,
    Route53DomainsRenewDomainRequest,
    Route53DomainsRenewDomainResponse,
    Route53DomainsResendContactReachabilityEmailRequest,
    Route53DomainsResendContactReachabilityEmailResponse,
    Route53DomainsResendOperationAuthorizationRequest,
    Route53DomainsResendOperationAuthorizationResponse,
    Route53DomainsRestoreDomainRequest,
    Route53DomainsRestoreDomainResponse,
    Route53DomainsRetrieveDomainAuthCodeRequest,
    Route53DomainsRetrieveDomainAuthCodeResponse,
    Route53DomainsTransferDomainRequest,
    Route53DomainsTransferDomainResponse,
    Route53DomainsTransferDomainToAnotherAwsAccountRequest,
    Route53DomainsTransferDomainToAnotherAwsAccountResponse,
    Route53DomainsUpdateDomainContactPrivacyRequest,
    Route53DomainsUpdateDomainContactPrivacyResponse,
    Route53DomainsUpdateDomainContactRequest,
    Route53DomainsUpdateDomainContactResponse,
    Route53DomainsUpdateDomainNameserversRequest,
    Route53DomainsUpdateDomainNameserversResponse,
    Route53DomainsUpdateTagsForDomainRequest,
    Route53DomainsUpdateTagsForDomainResponse,
    Route53DomainsViewBillingRequest,
    Route53DomainsViewBillingResponse,
)
from werkflow_aws.types.registrar_client import Route53DomainsClient
from .base import AWSBaseService


class AWSRoute53Domains(AWSBaseService[Route53DomainsClient]):
    service_name = 'registrar'
    boto3_service_name = 'route53domains'

    def __init__(self) -> None:
        super().__init__(service_name='registrar', boto3_service_name='route53domains')

    async def accept_domain_transfer_from_another_aws_account(
        self,
        request: Route53DomainsAcceptDomainTransferFromAnotherAwsAccountRequest,
    ) -> Route53DomainsAcceptDomainTransferFromAnotherAwsAccountResponse:
        client = self._require_client()
        return await self._execute(client.accept_domain_transfer_from_another_aws_account, request, Route53DomainsAcceptDomainTransferFromAnotherAwsAccountResponse)

    async def associate_delegation_signer_to_domain(
        self,
        request: Route53DomainsAssociateDelegationSignerToDomainRequest,
    ) -> Route53DomainsAssociateDelegationSignerToDomainResponse:
        client = self._require_client()
        return await self._execute(client.associate_delegation_signer_to_domain, request, Route53DomainsAssociateDelegationSignerToDomainResponse)

    async def cancel_domain_transfer_to_another_aws_account(
        self,
        request: Route53DomainsCancelDomainTransferToAnotherAwsAccountRequest,
    ) -> Route53DomainsCancelDomainTransferToAnotherAwsAccountResponse:
        client = self._require_client()
        return await self._execute(client.cancel_domain_transfer_to_another_aws_account, request, Route53DomainsCancelDomainTransferToAnotherAwsAccountResponse)

    async def check_domain_availability(
        self,
        request: Route53DomainsCheckDomainAvailabilityRequest,
    ) -> Route53DomainsCheckDomainAvailabilityResponse:
        client = self._require_client()
        return await self._execute(client.check_domain_availability, request, Route53DomainsCheckDomainAvailabilityResponse)

    async def check_domain_transferability(
        self,
        request: Route53DomainsCheckDomainTransferabilityRequest,
    ) -> Route53DomainsCheckDomainTransferabilityResponse:
        client = self._require_client()
        return await self._execute(client.check_domain_transferability, request, Route53DomainsCheckDomainTransferabilityResponse)

    async def delete_domain(
        self,
        request: Route53DomainsDeleteDomainRequest,
    ) -> Route53DomainsDeleteDomainResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain, request, Route53DomainsDeleteDomainResponse)

    async def delete_tags_for_domain(
        self,
        request: Route53DomainsDeleteTagsForDomainRequest,
    ) -> Route53DomainsDeleteTagsForDomainResponse:
        client = self._require_client()
        return await self._execute(client.delete_tags_for_domain, request, Route53DomainsDeleteTagsForDomainResponse)

    async def disable_domain_auto_renew(
        self,
        request: Route53DomainsDisableDomainAutoRenewRequest,
    ) -> Route53DomainsDisableDomainAutoRenewResponse:
        client = self._require_client()
        return await self._execute(client.disable_domain_auto_renew, request, Route53DomainsDisableDomainAutoRenewResponse)

    async def disable_domain_transfer_lock(
        self,
        request: Route53DomainsDisableDomainTransferLockRequest,
    ) -> Route53DomainsDisableDomainTransferLockResponse:
        client = self._require_client()
        return await self._execute(client.disable_domain_transfer_lock, request, Route53DomainsDisableDomainTransferLockResponse)

    async def disassociate_delegation_signer_from_domain(
        self,
        request: Route53DomainsDisassociateDelegationSignerFromDomainRequest,
    ) -> Route53DomainsDisassociateDelegationSignerFromDomainResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_delegation_signer_from_domain, request, Route53DomainsDisassociateDelegationSignerFromDomainResponse)

    async def enable_domain_auto_renew(
        self,
        request: Route53DomainsEnableDomainAutoRenewRequest,
    ) -> Route53DomainsEnableDomainAutoRenewResponse:
        client = self._require_client()
        return await self._execute(client.enable_domain_auto_renew, request, Route53DomainsEnableDomainAutoRenewResponse)

    async def enable_domain_transfer_lock(
        self,
        request: Route53DomainsEnableDomainTransferLockRequest,
    ) -> Route53DomainsEnableDomainTransferLockResponse:
        client = self._require_client()
        return await self._execute(client.enable_domain_transfer_lock, request, Route53DomainsEnableDomainTransferLockResponse)

    async def get_contact_reachability_status(
        self,
        request: Route53DomainsGetContactReachabilityStatusRequest | None = None,
    ) -> Route53DomainsGetContactReachabilityStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_contact_reachability_status, request, Route53DomainsGetContactReachabilityStatusResponse)

    async def get_domain_detail(
        self,
        request: Route53DomainsGetDomainDetailRequest,
    ) -> Route53DomainsGetDomainDetailResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_detail, request, Route53DomainsGetDomainDetailResponse)

    async def get_domain_prices(
        self,
        request: Route53DomainsGetDomainPricesRequest,
    ) -> Route53DomainsGetDomainPricesResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_prices, request, Route53DomainsGetDomainPricesResponse)

    async def get_domain_suggestions(
        self,
        request: Route53DomainsGetDomainSuggestionsRequest,
    ) -> Route53DomainsGetDomainSuggestionsResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_suggestions, request, Route53DomainsGetDomainSuggestionsResponse)

    async def get_operation_detail(
        self,
        request: Route53DomainsGetOperationDetailRequest,
    ) -> Route53DomainsGetOperationDetailResponse:
        client = self._require_client()
        return await self._execute(client.get_operation_detail, request, Route53DomainsGetOperationDetailResponse)

    async def list_domains(
        self,
        request: Route53DomainsListDomainsRequest | None = None,
    ) -> Route53DomainsListDomainsResponse:
        client = self._require_client()
        return await self._execute(client.list_domains, request, Route53DomainsListDomainsResponse)

    async def list_domains_paginated(
        self,
        request: Route53DomainsListDomainsRequest | None = None,
    ) -> list[Route53DomainsListDomainsResponse]:
        return await self._paginate('list_domains', request, Route53DomainsListDomainsResponse)

    async def list_operations(
        self,
        request: Route53DomainsListOperationsRequest | None = None,
    ) -> Route53DomainsListOperationsResponse:
        client = self._require_client()
        return await self._execute(client.list_operations, request, Route53DomainsListOperationsResponse)

    async def list_operations_paginated(
        self,
        request: Route53DomainsListOperationsRequest | None = None,
    ) -> list[Route53DomainsListOperationsResponse]:
        return await self._paginate('list_operations', request, Route53DomainsListOperationsResponse)

    async def list_prices(
        self,
        request: Route53DomainsListPricesRequest | None = None,
    ) -> Route53DomainsListPricesResponse:
        client = self._require_client()
        return await self._execute(client.list_prices, request, Route53DomainsListPricesResponse)

    async def list_prices_paginated(
        self,
        request: Route53DomainsListPricesRequest | None = None,
    ) -> list[Route53DomainsListPricesResponse]:
        return await self._paginate('list_prices', request, Route53DomainsListPricesResponse)

    async def list_tags_for_domain(
        self,
        request: Route53DomainsListTagsForDomainRequest,
    ) -> Route53DomainsListTagsForDomainResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_domain, request, Route53DomainsListTagsForDomainResponse)

    async def push_domain(
        self,
        request: Route53DomainsPushDomainRequest,
    ) -> Route53DomainsPushDomainResponse:
        client = self._require_client()
        return await self._execute(client.push_domain, request, Route53DomainsPushDomainResponse)

    async def register_domain(
        self,
        request: Route53DomainsRegisterDomainRequest,
    ) -> Route53DomainsRegisterDomainResponse:
        client = self._require_client()
        return await self._execute(client.register_domain, request, Route53DomainsRegisterDomainResponse)

    async def reject_domain_transfer_from_another_aws_account(
        self,
        request: Route53DomainsRejectDomainTransferFromAnotherAwsAccountRequest,
    ) -> Route53DomainsRejectDomainTransferFromAnotherAwsAccountResponse:
        client = self._require_client()
        return await self._execute(client.reject_domain_transfer_from_another_aws_account, request, Route53DomainsRejectDomainTransferFromAnotherAwsAccountResponse)

    async def renew_domain(
        self,
        request: Route53DomainsRenewDomainRequest,
    ) -> Route53DomainsRenewDomainResponse:
        client = self._require_client()
        return await self._execute(client.renew_domain, request, Route53DomainsRenewDomainResponse)

    async def resend_contact_reachability_email(
        self,
        request: Route53DomainsResendContactReachabilityEmailRequest | None = None,
    ) -> Route53DomainsResendContactReachabilityEmailResponse:
        client = self._require_client()
        return await self._execute(client.resend_contact_reachability_email, request, Route53DomainsResendContactReachabilityEmailResponse)

    async def resend_operation_authorization(
        self,
        request: Route53DomainsResendOperationAuthorizationRequest,
    ) -> Route53DomainsResendOperationAuthorizationResponse:
        client = self._require_client()
        return await self._execute(client.resend_operation_authorization, request, Route53DomainsResendOperationAuthorizationResponse)

    async def restore_domain(
        self,
        request: Route53DomainsRestoreDomainRequest,
    ) -> Route53DomainsRestoreDomainResponse:
        client = self._require_client()
        return await self._execute(client.restore_domain, request, Route53DomainsRestoreDomainResponse)

    async def retrieve_domain_auth_code(
        self,
        request: Route53DomainsRetrieveDomainAuthCodeRequest,
    ) -> Route53DomainsRetrieveDomainAuthCodeResponse:
        client = self._require_client()
        return await self._execute(client.retrieve_domain_auth_code, request, Route53DomainsRetrieveDomainAuthCodeResponse)

    async def transfer_domain(
        self,
        request: Route53DomainsTransferDomainRequest,
    ) -> Route53DomainsTransferDomainResponse:
        client = self._require_client()
        return await self._execute(client.transfer_domain, request, Route53DomainsTransferDomainResponse)

    async def transfer_domain_to_another_aws_account(
        self,
        request: Route53DomainsTransferDomainToAnotherAwsAccountRequest,
    ) -> Route53DomainsTransferDomainToAnotherAwsAccountResponse:
        client = self._require_client()
        return await self._execute(client.transfer_domain_to_another_aws_account, request, Route53DomainsTransferDomainToAnotherAwsAccountResponse)

    async def update_domain_contact(
        self,
        request: Route53DomainsUpdateDomainContactRequest,
    ) -> Route53DomainsUpdateDomainContactResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_contact, request, Route53DomainsUpdateDomainContactResponse)

    async def update_domain_contact_privacy(
        self,
        request: Route53DomainsUpdateDomainContactPrivacyRequest,
    ) -> Route53DomainsUpdateDomainContactPrivacyResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_contact_privacy, request, Route53DomainsUpdateDomainContactPrivacyResponse)

    async def update_domain_nameservers(
        self,
        request: Route53DomainsUpdateDomainNameserversRequest,
    ) -> Route53DomainsUpdateDomainNameserversResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_nameservers, request, Route53DomainsUpdateDomainNameserversResponse)

    async def update_tags_for_domain(
        self,
        request: Route53DomainsUpdateTagsForDomainRequest,
    ) -> Route53DomainsUpdateTagsForDomainResponse:
        client = self._require_client()
        return await self._execute(client.update_tags_for_domain, request, Route53DomainsUpdateTagsForDomainResponse)

    async def view_billing(
        self,
        request: Route53DomainsViewBillingRequest | None = None,
    ) -> Route53DomainsViewBillingResponse:
        client = self._require_client()
        return await self._execute(client.view_billing, request, Route53DomainsViewBillingResponse)

    async def view_billing_paginated(
        self,
        request: Route53DomainsViewBillingRequest | None = None,
    ) -> list[Route53DomainsViewBillingResponse]:
        return await self._paginate('view_billing', request, Route53DomainsViewBillingResponse)
