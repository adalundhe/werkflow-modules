from werkflow_aws.models.tax import (
    TaxSettingsBatchDeleteTaxRegistrationRequest,
    TaxSettingsBatchDeleteTaxRegistrationResponse,
    TaxSettingsBatchGetTaxExemptionsRequest,
    TaxSettingsBatchGetTaxExemptionsResponse,
    TaxSettingsBatchPutTaxRegistrationRequest,
    TaxSettingsBatchPutTaxRegistrationResponse,
    TaxSettingsDeleteSupplementalTaxRegistrationRequest,
    TaxSettingsDeleteSupplementalTaxRegistrationResponse,
    TaxSettingsDeleteTaxRegistrationRequest,
    TaxSettingsDeleteTaxRegistrationResponse,
    TaxSettingsGetTaxExemptionTypesRequest,
    TaxSettingsGetTaxExemptionTypesResponse,
    TaxSettingsGetTaxInheritanceRequest,
    TaxSettingsGetTaxInheritanceResponse,
    TaxSettingsGetTaxRegistrationDocumentRequest,
    TaxSettingsGetTaxRegistrationDocumentResponse,
    TaxSettingsGetTaxRegistrationRequest,
    TaxSettingsGetTaxRegistrationResponse,
    TaxSettingsListSupplementalTaxRegistrationsRequest,
    TaxSettingsListSupplementalTaxRegistrationsResponse,
    TaxSettingsListTaxExemptionsRequest,
    TaxSettingsListTaxExemptionsResponse,
    TaxSettingsListTaxRegistrationsRequest,
    TaxSettingsListTaxRegistrationsResponse,
    TaxSettingsPutSupplementalTaxRegistrationRequest,
    TaxSettingsPutSupplementalTaxRegistrationResponse,
    TaxSettingsPutTaxExemptionRequest,
    TaxSettingsPutTaxExemptionResponse,
    TaxSettingsPutTaxInheritanceRequest,
    TaxSettingsPutTaxInheritanceResponse,
    TaxSettingsPutTaxRegistrationRequest,
    TaxSettingsPutTaxRegistrationResponse,
)
from werkflow_aws.types.tax_client import TaxSettingsClient
from .base import AWSBaseService


class AWSTaxSettings(AWSBaseService[TaxSettingsClient]):
    service_name = 'tax'
    boto3_service_name = 'taxsettings'

    def __init__(self) -> None:
        super().__init__(service_name='tax', boto3_service_name='taxsettings')

    async def batch_delete_tax_registration(
        self,
        request: TaxSettingsBatchDeleteTaxRegistrationRequest,
    ) -> TaxSettingsBatchDeleteTaxRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_tax_registration, request, TaxSettingsBatchDeleteTaxRegistrationResponse)

    async def batch_get_tax_exemptions(
        self,
        request: TaxSettingsBatchGetTaxExemptionsRequest,
    ) -> TaxSettingsBatchGetTaxExemptionsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_tax_exemptions, request, TaxSettingsBatchGetTaxExemptionsResponse)

    async def batch_put_tax_registration(
        self,
        request: TaxSettingsBatchPutTaxRegistrationRequest,
    ) -> TaxSettingsBatchPutTaxRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.batch_put_tax_registration, request, TaxSettingsBatchPutTaxRegistrationResponse)

    async def delete_supplemental_tax_registration(
        self,
        request: TaxSettingsDeleteSupplementalTaxRegistrationRequest,
    ) -> TaxSettingsDeleteSupplementalTaxRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.delete_supplemental_tax_registration, request, TaxSettingsDeleteSupplementalTaxRegistrationResponse)

    async def delete_tax_registration(
        self,
        request: TaxSettingsDeleteTaxRegistrationRequest | None = None,
    ) -> TaxSettingsDeleteTaxRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.delete_tax_registration, request, TaxSettingsDeleteTaxRegistrationResponse)

    async def get_tax_exemption_types(
        self,
        request: TaxSettingsGetTaxExemptionTypesRequest | None = None,
    ) -> TaxSettingsGetTaxExemptionTypesResponse:
        client = self._require_client()
        return await self._execute(client.get_tax_exemption_types, request, TaxSettingsGetTaxExemptionTypesResponse)

    async def get_tax_inheritance(
        self,
        request: TaxSettingsGetTaxInheritanceRequest | None = None,
    ) -> TaxSettingsGetTaxInheritanceResponse:
        client = self._require_client()
        return await self._execute(client.get_tax_inheritance, request, TaxSettingsGetTaxInheritanceResponse)

    async def get_tax_registration(
        self,
        request: TaxSettingsGetTaxRegistrationRequest | None = None,
    ) -> TaxSettingsGetTaxRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.get_tax_registration, request, TaxSettingsGetTaxRegistrationResponse)

    async def get_tax_registration_document(
        self,
        request: TaxSettingsGetTaxRegistrationDocumentRequest,
    ) -> TaxSettingsGetTaxRegistrationDocumentResponse:
        client = self._require_client()
        return await self._execute(client.get_tax_registration_document, request, TaxSettingsGetTaxRegistrationDocumentResponse)

    async def list_supplemental_tax_registrations(
        self,
        request: TaxSettingsListSupplementalTaxRegistrationsRequest | None = None,
    ) -> TaxSettingsListSupplementalTaxRegistrationsResponse:
        client = self._require_client()
        return await self._execute(client.list_supplemental_tax_registrations, request, TaxSettingsListSupplementalTaxRegistrationsResponse)

    async def list_supplemental_tax_registrations_paginated(
        self,
        request: TaxSettingsListSupplementalTaxRegistrationsRequest | None = None,
    ) -> list[TaxSettingsListSupplementalTaxRegistrationsResponse]:
        return await self._paginate('list_supplemental_tax_registrations', request, TaxSettingsListSupplementalTaxRegistrationsResponse)

    async def list_tax_exemptions(
        self,
        request: TaxSettingsListTaxExemptionsRequest | None = None,
    ) -> TaxSettingsListTaxExemptionsResponse:
        client = self._require_client()
        return await self._execute(client.list_tax_exemptions, request, TaxSettingsListTaxExemptionsResponse)

    async def list_tax_exemptions_paginated(
        self,
        request: TaxSettingsListTaxExemptionsRequest | None = None,
    ) -> list[TaxSettingsListTaxExemptionsResponse]:
        return await self._paginate('list_tax_exemptions', request, TaxSettingsListTaxExemptionsResponse)

    async def list_tax_registrations(
        self,
        request: TaxSettingsListTaxRegistrationsRequest | None = None,
    ) -> TaxSettingsListTaxRegistrationsResponse:
        client = self._require_client()
        return await self._execute(client.list_tax_registrations, request, TaxSettingsListTaxRegistrationsResponse)

    async def list_tax_registrations_paginated(
        self,
        request: TaxSettingsListTaxRegistrationsRequest | None = None,
    ) -> list[TaxSettingsListTaxRegistrationsResponse]:
        return await self._paginate('list_tax_registrations', request, TaxSettingsListTaxRegistrationsResponse)

    async def put_supplemental_tax_registration(
        self,
        request: TaxSettingsPutSupplementalTaxRegistrationRequest,
    ) -> TaxSettingsPutSupplementalTaxRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.put_supplemental_tax_registration, request, TaxSettingsPutSupplementalTaxRegistrationResponse)

    async def put_tax_exemption(
        self,
        request: TaxSettingsPutTaxExemptionRequest,
    ) -> TaxSettingsPutTaxExemptionResponse:
        client = self._require_client()
        return await self._execute(client.put_tax_exemption, request, TaxSettingsPutTaxExemptionResponse)

    async def put_tax_inheritance(
        self,
        request: TaxSettingsPutTaxInheritanceRequest | None = None,
    ) -> TaxSettingsPutTaxInheritanceResponse:
        client = self._require_client()
        return await self._execute(client.put_tax_inheritance, request, TaxSettingsPutTaxInheritanceResponse)

    async def put_tax_registration(
        self,
        request: TaxSettingsPutTaxRegistrationRequest,
    ) -> TaxSettingsPutTaxRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.put_tax_registration, request, TaxSettingsPutTaxRegistrationResponse)
