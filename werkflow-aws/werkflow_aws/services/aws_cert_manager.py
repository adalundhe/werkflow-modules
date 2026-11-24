from werkflow_aws.models.cert_manager import (
    ACMAddTagsToCertificateRequest,
    ACMAddTagsToCertificateResponse,
    ACMCreateAcmeDomainValidationRequest,
    ACMCreateAcmeDomainValidationResponse,
    ACMCreateAcmeEndpointRequest,
    ACMCreateAcmeEndpointResponse,
    ACMCreateAcmeExternalAccountBindingRequest,
    ACMCreateAcmeExternalAccountBindingResponse,
    ACMDeleteAcmeDomainValidationRequest,
    ACMDeleteAcmeDomainValidationResponse,
    ACMDeleteAcmeEndpointRequest,
    ACMDeleteAcmeEndpointResponse,
    ACMDeleteAcmeExternalAccountBindingRequest,
    ACMDeleteAcmeExternalAccountBindingResponse,
    ACMDeleteCertificateRequest,
    ACMDeleteCertificateResponse,
    ACMDescribeAcmeAccountRequest,
    ACMDescribeAcmeAccountResponse,
    ACMDescribeAcmeDomainValidationRequest,
    ACMDescribeAcmeDomainValidationResponse,
    ACMDescribeAcmeEndpointRequest,
    ACMDescribeAcmeEndpointResponse,
    ACMDescribeAcmeExternalAccountBindingRequest,
    ACMDescribeAcmeExternalAccountBindingResponse,
    ACMDescribeCertificateRequest,
    ACMDescribeCertificateResponse,
    ACMExportCertificateRequest,
    ACMExportCertificateResponse,
    ACMGetAccountConfigurationRequest,
    ACMGetAccountConfigurationResponse,
    ACMGetAcmeExternalAccountBindingCredentialsRequest,
    ACMGetAcmeExternalAccountBindingCredentialsResponse,
    ACMGetCertificateRequest,
    ACMGetCertificateResponse,
    ACMImportCertificateRequest,
    ACMImportCertificateResponse,
    ACMListAcmeAccountsRequest,
    ACMListAcmeAccountsResponse,
    ACMListAcmeDomainValidationsRequest,
    ACMListAcmeDomainValidationsResponse,
    ACMListAcmeEndpointsRequest,
    ACMListAcmeEndpointsResponse,
    ACMListAcmeExternalAccountBindingsRequest,
    ACMListAcmeExternalAccountBindingsResponse,
    ACMListCertificateDomainValidationsRequest,
    ACMListCertificateDomainValidationsResponse,
    ACMListCertificatesRequest,
    ACMListCertificatesResponse,
    ACMListTagsForCertificateRequest,
    ACMListTagsForCertificateResponse,
    ACMListTagsForResourceRequest,
    ACMListTagsForResourceResponse,
    ACMPutAccountConfigurationRequest,
    ACMPutAccountConfigurationResponse,
    ACMRemoveTagsFromCertificateRequest,
    ACMRemoveTagsFromCertificateResponse,
    ACMRenewCertificateRequest,
    ACMRenewCertificateResponse,
    ACMRequestCertificateRequest,
    ACMRequestCertificateResponse,
    ACMResendValidationEmailRequest,
    ACMResendValidationEmailResponse,
    ACMRevokeAcmeAccountRequest,
    ACMRevokeAcmeAccountResponse,
    ACMRevokeAcmeExternalAccountBindingRequest,
    ACMRevokeAcmeExternalAccountBindingResponse,
    ACMRevokeCertificateRequest,
    ACMRevokeCertificateResponse,
    ACMSearchCertificatesRequest,
    ACMSearchCertificatesResponse,
    ACMTagResourceRequest,
    ACMTagResourceResponse,
    ACMUntagResourceRequest,
    ACMUntagResourceResponse,
    ACMUpdateAcmeDomainValidationRequest,
    ACMUpdateAcmeDomainValidationResponse,
    ACMUpdateAcmeEndpointRequest,
    ACMUpdateAcmeEndpointResponse,
    ACMUpdateCertificateOptionsRequest,
    ACMUpdateCertificateOptionsResponse,
)
from werkflow_aws.types.cert_manager_client import ACMClient
from .base import AWSBaseService


class AWSACM(AWSBaseService[ACMClient]):
    service_name = 'cert-manager'
    boto3_service_name = 'acm'

    def __init__(self) -> None:
        super().__init__(service_name='cert-manager', boto3_service_name='acm')

    async def add_tags_to_certificate(
        self,
        request: ACMAddTagsToCertificateRequest,
    ) -> ACMAddTagsToCertificateResponse:
        client = self._require_client()
        return await self._execute(client.add_tags_to_certificate, request, ACMAddTagsToCertificateResponse)

    async def create_acme_domain_validation(
        self,
        request: ACMCreateAcmeDomainValidationRequest,
    ) -> ACMCreateAcmeDomainValidationResponse:
        client = self._require_client()
        return await self._execute(client.create_acme_domain_validation, request, ACMCreateAcmeDomainValidationResponse)

    async def create_acme_endpoint(
        self,
        request: ACMCreateAcmeEndpointRequest,
    ) -> ACMCreateAcmeEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_acme_endpoint, request, ACMCreateAcmeEndpointResponse)

    async def create_acme_external_account_binding(
        self,
        request: ACMCreateAcmeExternalAccountBindingRequest,
    ) -> ACMCreateAcmeExternalAccountBindingResponse:
        client = self._require_client()
        return await self._execute(client.create_acme_external_account_binding, request, ACMCreateAcmeExternalAccountBindingResponse)

    async def delete_acme_domain_validation(
        self,
        request: ACMDeleteAcmeDomainValidationRequest,
    ) -> ACMDeleteAcmeDomainValidationResponse:
        client = self._require_client()
        return await self._execute(client.delete_acme_domain_validation, request, ACMDeleteAcmeDomainValidationResponse)

    async def delete_acme_endpoint(
        self,
        request: ACMDeleteAcmeEndpointRequest,
    ) -> ACMDeleteAcmeEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_acme_endpoint, request, ACMDeleteAcmeEndpointResponse)

    async def delete_acme_external_account_binding(
        self,
        request: ACMDeleteAcmeExternalAccountBindingRequest,
    ) -> ACMDeleteAcmeExternalAccountBindingResponse:
        client = self._require_client()
        return await self._execute(client.delete_acme_external_account_binding, request, ACMDeleteAcmeExternalAccountBindingResponse)

    async def delete_certificate(
        self,
        request: ACMDeleteCertificateRequest,
    ) -> ACMDeleteCertificateResponse:
        client = self._require_client()
        return await self._execute(client.delete_certificate, request, ACMDeleteCertificateResponse)

    async def describe_acme_account(
        self,
        request: ACMDescribeAcmeAccountRequest,
    ) -> ACMDescribeAcmeAccountResponse:
        client = self._require_client()
        return await self._execute(client.describe_acme_account, request, ACMDescribeAcmeAccountResponse)

    async def describe_acme_domain_validation(
        self,
        request: ACMDescribeAcmeDomainValidationRequest,
    ) -> ACMDescribeAcmeDomainValidationResponse:
        client = self._require_client()
        return await self._execute(client.describe_acme_domain_validation, request, ACMDescribeAcmeDomainValidationResponse)

    async def describe_acme_endpoint(
        self,
        request: ACMDescribeAcmeEndpointRequest,
    ) -> ACMDescribeAcmeEndpointResponse:
        client = self._require_client()
        return await self._execute(client.describe_acme_endpoint, request, ACMDescribeAcmeEndpointResponse)

    async def describe_acme_external_account_binding(
        self,
        request: ACMDescribeAcmeExternalAccountBindingRequest,
    ) -> ACMDescribeAcmeExternalAccountBindingResponse:
        client = self._require_client()
        return await self._execute(client.describe_acme_external_account_binding, request, ACMDescribeAcmeExternalAccountBindingResponse)

    async def describe_certificate(
        self,
        request: ACMDescribeCertificateRequest,
    ) -> ACMDescribeCertificateResponse:
        client = self._require_client()
        return await self._execute(client.describe_certificate, request, ACMDescribeCertificateResponse)

    async def export_certificate(
        self,
        request: ACMExportCertificateRequest,
    ) -> ACMExportCertificateResponse:
        client = self._require_client()
        return await self._execute(client.export_certificate, request, ACMExportCertificateResponse)

    async def get_account_configuration(
        self,
        request: ACMGetAccountConfigurationRequest | None = None,
    ) -> ACMGetAccountConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_account_configuration, request, ACMGetAccountConfigurationResponse)

    async def get_acme_external_account_binding_credentials(
        self,
        request: ACMGetAcmeExternalAccountBindingCredentialsRequest,
    ) -> ACMGetAcmeExternalAccountBindingCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.get_acme_external_account_binding_credentials, request, ACMGetAcmeExternalAccountBindingCredentialsResponse)

    async def get_certificate(
        self,
        request: ACMGetCertificateRequest,
    ) -> ACMGetCertificateResponse:
        client = self._require_client()
        return await self._execute(client.get_certificate, request, ACMGetCertificateResponse)

    async def import_certificate(
        self,
        request: ACMImportCertificateRequest,
    ) -> ACMImportCertificateResponse:
        client = self._require_client()
        return await self._execute(client.import_certificate, request, ACMImportCertificateResponse)

    async def list_acme_accounts(
        self,
        request: ACMListAcmeAccountsRequest,
    ) -> ACMListAcmeAccountsResponse:
        client = self._require_client()
        return await self._execute(client.list_acme_accounts, request, ACMListAcmeAccountsResponse)

    async def list_acme_accounts_paginated(
        self,
        request: ACMListAcmeAccountsRequest,
    ) -> list[ACMListAcmeAccountsResponse]:
        return await self._paginate('list_acme_accounts', request, ACMListAcmeAccountsResponse)

    async def list_acme_domain_validations(
        self,
        request: ACMListAcmeDomainValidationsRequest,
    ) -> ACMListAcmeDomainValidationsResponse:
        client = self._require_client()
        return await self._execute(client.list_acme_domain_validations, request, ACMListAcmeDomainValidationsResponse)

    async def list_acme_domain_validations_paginated(
        self,
        request: ACMListAcmeDomainValidationsRequest,
    ) -> list[ACMListAcmeDomainValidationsResponse]:
        return await self._paginate('list_acme_domain_validations', request, ACMListAcmeDomainValidationsResponse)

    async def list_acme_endpoints(
        self,
        request: ACMListAcmeEndpointsRequest | None = None,
    ) -> ACMListAcmeEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.list_acme_endpoints, request, ACMListAcmeEndpointsResponse)

    async def list_acme_endpoints_paginated(
        self,
        request: ACMListAcmeEndpointsRequest | None = None,
    ) -> list[ACMListAcmeEndpointsResponse]:
        return await self._paginate('list_acme_endpoints', request, ACMListAcmeEndpointsResponse)

    async def list_acme_external_account_bindings(
        self,
        request: ACMListAcmeExternalAccountBindingsRequest,
    ) -> ACMListAcmeExternalAccountBindingsResponse:
        client = self._require_client()
        return await self._execute(client.list_acme_external_account_bindings, request, ACMListAcmeExternalAccountBindingsResponse)

    async def list_acme_external_account_bindings_paginated(
        self,
        request: ACMListAcmeExternalAccountBindingsRequest,
    ) -> list[ACMListAcmeExternalAccountBindingsResponse]:
        return await self._paginate('list_acme_external_account_bindings', request, ACMListAcmeExternalAccountBindingsResponse)

    async def list_certificate_domain_validations(
        self,
        request: ACMListCertificateDomainValidationsRequest,
    ) -> ACMListCertificateDomainValidationsResponse:
        client = self._require_client()
        return await self._execute(client.list_certificate_domain_validations, request, ACMListCertificateDomainValidationsResponse)

    async def list_certificate_domain_validations_paginated(
        self,
        request: ACMListCertificateDomainValidationsRequest,
    ) -> list[ACMListCertificateDomainValidationsResponse]:
        return await self._paginate('list_certificate_domain_validations', request, ACMListCertificateDomainValidationsResponse)

    async def list_certificates(
        self,
        request: ACMListCertificatesRequest | None = None,
    ) -> ACMListCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.list_certificates, request, ACMListCertificatesResponse)

    async def list_certificates_paginated(
        self,
        request: ACMListCertificatesRequest | None = None,
    ) -> list[ACMListCertificatesResponse]:
        return await self._paginate('list_certificates', request, ACMListCertificatesResponse)

    async def list_tags_for_certificate(
        self,
        request: ACMListTagsForCertificateRequest,
    ) -> ACMListTagsForCertificateResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_certificate, request, ACMListTagsForCertificateResponse)

    async def list_tags_for_resource(
        self,
        request: ACMListTagsForResourceRequest,
    ) -> ACMListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, ACMListTagsForResourceResponse)

    async def put_account_configuration(
        self,
        request: ACMPutAccountConfigurationRequest,
    ) -> ACMPutAccountConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_account_configuration, request, ACMPutAccountConfigurationResponse)

    async def remove_tags_from_certificate(
        self,
        request: ACMRemoveTagsFromCertificateRequest,
    ) -> ACMRemoveTagsFromCertificateResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags_from_certificate, request, ACMRemoveTagsFromCertificateResponse)

    async def renew_certificate(
        self,
        request: ACMRenewCertificateRequest,
    ) -> ACMRenewCertificateResponse:
        client = self._require_client()
        return await self._execute(client.renew_certificate, request, ACMRenewCertificateResponse)

    async def request_certificate(
        self,
        request: ACMRequestCertificateRequest,
    ) -> ACMRequestCertificateResponse:
        client = self._require_client()
        return await self._execute(client.request_certificate, request, ACMRequestCertificateResponse)

    async def resend_validation_email(
        self,
        request: ACMResendValidationEmailRequest,
    ) -> ACMResendValidationEmailResponse:
        client = self._require_client()
        return await self._execute(client.resend_validation_email, request, ACMResendValidationEmailResponse)

    async def revoke_acme_account(
        self,
        request: ACMRevokeAcmeAccountRequest,
    ) -> ACMRevokeAcmeAccountResponse:
        client = self._require_client()
        return await self._execute(client.revoke_acme_account, request, ACMRevokeAcmeAccountResponse)

    async def revoke_acme_external_account_binding(
        self,
        request: ACMRevokeAcmeExternalAccountBindingRequest,
    ) -> ACMRevokeAcmeExternalAccountBindingResponse:
        client = self._require_client()
        return await self._execute(client.revoke_acme_external_account_binding, request, ACMRevokeAcmeExternalAccountBindingResponse)

    async def revoke_certificate(
        self,
        request: ACMRevokeCertificateRequest,
    ) -> ACMRevokeCertificateResponse:
        client = self._require_client()
        return await self._execute(client.revoke_certificate, request, ACMRevokeCertificateResponse)

    async def search_certificates(
        self,
        request: ACMSearchCertificatesRequest | None = None,
    ) -> ACMSearchCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.search_certificates, request, ACMSearchCertificatesResponse)

    async def search_certificates_paginated(
        self,
        request: ACMSearchCertificatesRequest | None = None,
    ) -> list[ACMSearchCertificatesResponse]:
        return await self._paginate('search_certificates', request, ACMSearchCertificatesResponse)

    async def tag_resource(
        self,
        request: ACMTagResourceRequest,
    ) -> ACMTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, ACMTagResourceResponse)

    async def untag_resource(
        self,
        request: ACMUntagResourceRequest,
    ) -> ACMUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, ACMUntagResourceResponse)

    async def update_acme_domain_validation(
        self,
        request: ACMUpdateAcmeDomainValidationRequest,
    ) -> ACMUpdateAcmeDomainValidationResponse:
        client = self._require_client()
        return await self._execute(client.update_acme_domain_validation, request, ACMUpdateAcmeDomainValidationResponse)

    async def update_acme_endpoint(
        self,
        request: ACMUpdateAcmeEndpointRequest,
    ) -> ACMUpdateAcmeEndpointResponse:
        client = self._require_client()
        return await self._execute(client.update_acme_endpoint, request, ACMUpdateAcmeEndpointResponse)

    async def update_certificate_options(
        self,
        request: ACMUpdateCertificateOptionsRequest,
    ) -> ACMUpdateCertificateOptionsResponse:
        client = self._require_client()
        return await self._execute(client.update_certificate_options, request, ACMUpdateCertificateOptionsResponse)
