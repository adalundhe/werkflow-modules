from werkflow_aws.models.cloudsearch import (
    CloudSearchBuildSuggestersRequest,
    CloudSearchBuildSuggestersResponse,
    CloudSearchCreateDomainRequest,
    CloudSearchCreateDomainResponse,
    CloudSearchDefineAnalysisSchemeRequest,
    CloudSearchDefineAnalysisSchemeResponse,
    CloudSearchDefineExpressionRequest,
    CloudSearchDefineExpressionResponse,
    CloudSearchDefineIndexFieldRequest,
    CloudSearchDefineIndexFieldResponse,
    CloudSearchDefineSuggesterRequest,
    CloudSearchDefineSuggesterResponse,
    CloudSearchDeleteAnalysisSchemeRequest,
    CloudSearchDeleteAnalysisSchemeResponse,
    CloudSearchDeleteDomainRequest,
    CloudSearchDeleteDomainResponse,
    CloudSearchDeleteExpressionRequest,
    CloudSearchDeleteExpressionResponse,
    CloudSearchDeleteIndexFieldRequest,
    CloudSearchDeleteIndexFieldResponse,
    CloudSearchDeleteSuggesterRequest,
    CloudSearchDeleteSuggesterResponse,
    CloudSearchDescribeAnalysisSchemesRequest,
    CloudSearchDescribeAnalysisSchemesResponse,
    CloudSearchDescribeAvailabilityOptionsRequest,
    CloudSearchDescribeAvailabilityOptionsResponse,
    CloudSearchDescribeDomainEndpointOptionsRequest,
    CloudSearchDescribeDomainEndpointOptionsResponse,
    CloudSearchDescribeDomainsRequest,
    CloudSearchDescribeDomainsResponse,
    CloudSearchDescribeExpressionsRequest,
    CloudSearchDescribeExpressionsResponse,
    CloudSearchDescribeIndexFieldsRequest,
    CloudSearchDescribeIndexFieldsResponse,
    CloudSearchDescribeScalingParametersRequest,
    CloudSearchDescribeScalingParametersResponse,
    CloudSearchDescribeServiceAccessPoliciesRequest,
    CloudSearchDescribeServiceAccessPoliciesResponse,
    CloudSearchDescribeSuggestersRequest,
    CloudSearchDescribeSuggestersResponse,
    CloudSearchIndexDocumentsRequest,
    CloudSearchIndexDocumentsResponse,
    CloudSearchListDomainNamesRequest,
    CloudSearchListDomainNamesResponse,
    CloudSearchUpdateAvailabilityOptionsRequest,
    CloudSearchUpdateAvailabilityOptionsResponse,
    CloudSearchUpdateDomainEndpointOptionsRequest,
    CloudSearchUpdateDomainEndpointOptionsResponse,
    CloudSearchUpdateScalingParametersRequest,
    CloudSearchUpdateScalingParametersResponse,
    CloudSearchUpdateServiceAccessPoliciesRequest,
    CloudSearchUpdateServiceAccessPoliciesResponse,
)
from werkflow_aws.types.cloudsearch_client import CloudSearchClient
from .base import AWSBaseService


class AWSCloudSearch(AWSBaseService[CloudSearchClient]):
    service_name = 'cloudsearch'
    boto3_service_name = 'cloudsearch'

    def __init__(self) -> None:
        super().__init__(service_name='cloudsearch', boto3_service_name='cloudsearch')

    async def build_suggesters(
        self,
        request: CloudSearchBuildSuggestersRequest,
    ) -> CloudSearchBuildSuggestersResponse:
        client = self._require_client()
        return await self._execute(client.build_suggesters, request, CloudSearchBuildSuggestersResponse)

    async def create_domain(
        self,
        request: CloudSearchCreateDomainRequest,
    ) -> CloudSearchCreateDomainResponse:
        client = self._require_client()
        return await self._execute(client.create_domain, request, CloudSearchCreateDomainResponse)

    async def define_analysis_scheme(
        self,
        request: CloudSearchDefineAnalysisSchemeRequest,
    ) -> CloudSearchDefineAnalysisSchemeResponse:
        client = self._require_client()
        return await self._execute(client.define_analysis_scheme, request, CloudSearchDefineAnalysisSchemeResponse)

    async def define_expression(
        self,
        request: CloudSearchDefineExpressionRequest,
    ) -> CloudSearchDefineExpressionResponse:
        client = self._require_client()
        return await self._execute(client.define_expression, request, CloudSearchDefineExpressionResponse)

    async def define_index_field(
        self,
        request: CloudSearchDefineIndexFieldRequest,
    ) -> CloudSearchDefineIndexFieldResponse:
        client = self._require_client()
        return await self._execute(client.define_index_field, request, CloudSearchDefineIndexFieldResponse)

    async def define_suggester(
        self,
        request: CloudSearchDefineSuggesterRequest,
    ) -> CloudSearchDefineSuggesterResponse:
        client = self._require_client()
        return await self._execute(client.define_suggester, request, CloudSearchDefineSuggesterResponse)

    async def delete_analysis_scheme(
        self,
        request: CloudSearchDeleteAnalysisSchemeRequest,
    ) -> CloudSearchDeleteAnalysisSchemeResponse:
        client = self._require_client()
        return await self._execute(client.delete_analysis_scheme, request, CloudSearchDeleteAnalysisSchemeResponse)

    async def delete_domain(
        self,
        request: CloudSearchDeleteDomainRequest,
    ) -> CloudSearchDeleteDomainResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain, request, CloudSearchDeleteDomainResponse)

    async def delete_expression(
        self,
        request: CloudSearchDeleteExpressionRequest,
    ) -> CloudSearchDeleteExpressionResponse:
        client = self._require_client()
        return await self._execute(client.delete_expression, request, CloudSearchDeleteExpressionResponse)

    async def delete_index_field(
        self,
        request: CloudSearchDeleteIndexFieldRequest,
    ) -> CloudSearchDeleteIndexFieldResponse:
        client = self._require_client()
        return await self._execute(client.delete_index_field, request, CloudSearchDeleteIndexFieldResponse)

    async def delete_suggester(
        self,
        request: CloudSearchDeleteSuggesterRequest,
    ) -> CloudSearchDeleteSuggesterResponse:
        client = self._require_client()
        return await self._execute(client.delete_suggester, request, CloudSearchDeleteSuggesterResponse)

    async def describe_analysis_schemes(
        self,
        request: CloudSearchDescribeAnalysisSchemesRequest,
    ) -> CloudSearchDescribeAnalysisSchemesResponse:
        client = self._require_client()
        return await self._execute(client.describe_analysis_schemes, request, CloudSearchDescribeAnalysisSchemesResponse)

    async def describe_availability_options(
        self,
        request: CloudSearchDescribeAvailabilityOptionsRequest,
    ) -> CloudSearchDescribeAvailabilityOptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_availability_options, request, CloudSearchDescribeAvailabilityOptionsResponse)

    async def describe_domain_endpoint_options(
        self,
        request: CloudSearchDescribeDomainEndpointOptionsRequest,
    ) -> CloudSearchDescribeDomainEndpointOptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_domain_endpoint_options, request, CloudSearchDescribeDomainEndpointOptionsResponse)

    async def describe_domains(
        self,
        request: CloudSearchDescribeDomainsRequest | None = None,
    ) -> CloudSearchDescribeDomainsResponse:
        client = self._require_client()
        return await self._execute(client.describe_domains, request, CloudSearchDescribeDomainsResponse)

    async def describe_expressions(
        self,
        request: CloudSearchDescribeExpressionsRequest,
    ) -> CloudSearchDescribeExpressionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_expressions, request, CloudSearchDescribeExpressionsResponse)

    async def describe_index_fields(
        self,
        request: CloudSearchDescribeIndexFieldsRequest,
    ) -> CloudSearchDescribeIndexFieldsResponse:
        client = self._require_client()
        return await self._execute(client.describe_index_fields, request, CloudSearchDescribeIndexFieldsResponse)

    async def describe_scaling_parameters(
        self,
        request: CloudSearchDescribeScalingParametersRequest,
    ) -> CloudSearchDescribeScalingParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_scaling_parameters, request, CloudSearchDescribeScalingParametersResponse)

    async def describe_service_access_policies(
        self,
        request: CloudSearchDescribeServiceAccessPoliciesRequest,
    ) -> CloudSearchDescribeServiceAccessPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.describe_service_access_policies, request, CloudSearchDescribeServiceAccessPoliciesResponse)

    async def describe_suggesters(
        self,
        request: CloudSearchDescribeSuggestersRequest,
    ) -> CloudSearchDescribeSuggestersResponse:
        client = self._require_client()
        return await self._execute(client.describe_suggesters, request, CloudSearchDescribeSuggestersResponse)

    async def index_documents(
        self,
        request: CloudSearchIndexDocumentsRequest,
    ) -> CloudSearchIndexDocumentsResponse:
        client = self._require_client()
        return await self._execute(client.index_documents, request, CloudSearchIndexDocumentsResponse)

    async def list_domain_names(
        self,
        request: CloudSearchListDomainNamesRequest | None = None,
    ) -> CloudSearchListDomainNamesResponse:
        client = self._require_client()
        return await self._execute(client.list_domain_names, request, CloudSearchListDomainNamesResponse)

    async def update_availability_options(
        self,
        request: CloudSearchUpdateAvailabilityOptionsRequest,
    ) -> CloudSearchUpdateAvailabilityOptionsResponse:
        client = self._require_client()
        return await self._execute(client.update_availability_options, request, CloudSearchUpdateAvailabilityOptionsResponse)

    async def update_domain_endpoint_options(
        self,
        request: CloudSearchUpdateDomainEndpointOptionsRequest,
    ) -> CloudSearchUpdateDomainEndpointOptionsResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_endpoint_options, request, CloudSearchUpdateDomainEndpointOptionsResponse)

    async def update_scaling_parameters(
        self,
        request: CloudSearchUpdateScalingParametersRequest,
    ) -> CloudSearchUpdateScalingParametersResponse:
        client = self._require_client()
        return await self._execute(client.update_scaling_parameters, request, CloudSearchUpdateScalingParametersResponse)

    async def update_service_access_policies(
        self,
        request: CloudSearchUpdateServiceAccessPoliciesRequest,
    ) -> CloudSearchUpdateServiceAccessPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.update_service_access_policies, request, CloudSearchUpdateServiceAccessPoliciesResponse)
