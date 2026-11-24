from __future__ import annotations
from pydantic import BaseModel
from .tax_settings_belgium_additional_info import TaxSettingsBelgiumAdditionalInfo
from .tax_settings_brazil_additional_info import TaxSettingsBrazilAdditionalInfo
from .tax_settings_canada_additional_info import TaxSettingsCanadaAdditionalInfo
from .tax_settings_chile_additional_info import TaxSettingsChileAdditionalInfo
from .tax_settings_colombia_additional_info import TaxSettingsColombiaAdditionalInfo
from .tax_settings_egypt_additional_info import TaxSettingsEgyptAdditionalInfo
from .tax_settings_estonia_additional_info import TaxSettingsEstoniaAdditionalInfo
from .tax_settings_france_additional_info import TaxSettingsFranceAdditionalInfo
from .tax_settings_georgia_additional_info import TaxSettingsGeorgiaAdditionalInfo
from .tax_settings_germany_additional_info import TaxSettingsGermanyAdditionalInfo
from .tax_settings_greece_additional_info import TaxSettingsGreeceAdditionalInfo
from .tax_settings_india_additional_info import TaxSettingsIndiaAdditionalInfo
from .tax_settings_indonesia_additional_info import TaxSettingsIndonesiaAdditionalInfo
from .tax_settings_israel_additional_info import TaxSettingsIsraelAdditionalInfo
from .tax_settings_italy_additional_info import TaxSettingsItalyAdditionalInfo
from .tax_settings_kenya_additional_info import TaxSettingsKenyaAdditionalInfo
from .tax_settings_malaysia_additional_info import TaxSettingsMalaysiaAdditionalInfo
from .tax_settings_mexico_additional_info import TaxSettingsMexicoAdditionalInfo
from .tax_settings_monaco_additional_info import TaxSettingsMonacoAdditionalInfo
from .tax_settings_new_zealand_additional_info import TaxSettingsNewZealandAdditionalInfo
from .tax_settings_norway_additional_info import TaxSettingsNorwayAdditionalInfo
from .tax_settings_philippines_additional_info import TaxSettingsPhilippinesAdditionalInfo
from .tax_settings_poland_additional_info import TaxSettingsPolandAdditionalInfo
from .tax_settings_romania_additional_info import TaxSettingsRomaniaAdditionalInfo
from .tax_settings_saudi_arabia_additional_info import TaxSettingsSaudiArabiaAdditionalInfo
from .tax_settings_south_korea_additional_info import TaxSettingsSouthKoreaAdditionalInfo
from .tax_settings_spain_additional_info import TaxSettingsSpainAdditionalInfo
from .tax_settings_turkey_additional_info import TaxSettingsTurkeyAdditionalInfo
from .tax_settings_ukraine_additional_info import TaxSettingsUkraineAdditionalInfo
from .tax_settings_united_arab_emirates_additional_info import TaxSettingsUnitedArabEmiratesAdditionalInfo
from .tax_settings_uzbekistan_additional_info import TaxSettingsUzbekistanAdditionalInfo
from .tax_settings_vietnam_additional_info import TaxSettingsVietnamAdditionalInfo


class TaxSettingsAdditionalInfoResponse(BaseModel):
    malaysiaAdditionalInfo: TaxSettingsMalaysiaAdditionalInfo | None = None
    israelAdditionalInfo: TaxSettingsIsraelAdditionalInfo | None = None
    estoniaAdditionalInfo: TaxSettingsEstoniaAdditionalInfo | None = None
    canadaAdditionalInfo: TaxSettingsCanadaAdditionalInfo | None = None
    brazilAdditionalInfo: TaxSettingsBrazilAdditionalInfo | None = None
    spainAdditionalInfo: TaxSettingsSpainAdditionalInfo | None = None
    kenyaAdditionalInfo: TaxSettingsKenyaAdditionalInfo | None = None
    southKoreaAdditionalInfo: TaxSettingsSouthKoreaAdditionalInfo | None = None
    turkeyAdditionalInfo: TaxSettingsTurkeyAdditionalInfo | None = None
    georgiaAdditionalInfo: TaxSettingsGeorgiaAdditionalInfo | None = None
    italyAdditionalInfo: TaxSettingsItalyAdditionalInfo | None = None
    romaniaAdditionalInfo: TaxSettingsRomaniaAdditionalInfo | None = None
    ukraineAdditionalInfo: TaxSettingsUkraineAdditionalInfo | None = None
    polandAdditionalInfo: TaxSettingsPolandAdditionalInfo | None = None
    saudiArabiaAdditionalInfo: TaxSettingsSaudiArabiaAdditionalInfo | None = None
    indiaAdditionalInfo: TaxSettingsIndiaAdditionalInfo | None = None
    indonesiaAdditionalInfo: TaxSettingsIndonesiaAdditionalInfo | None = None
    vietnamAdditionalInfo: TaxSettingsVietnamAdditionalInfo | None = None
    egyptAdditionalInfo: TaxSettingsEgyptAdditionalInfo | None = None
    greeceAdditionalInfo: TaxSettingsGreeceAdditionalInfo | None = None
    uzbekistanAdditionalInfo: TaxSettingsUzbekistanAdditionalInfo | None = None
    philippinesAdditionalInfo: TaxSettingsPhilippinesAdditionalInfo | None = None
    belgiumAdditionalInfo: TaxSettingsBelgiumAdditionalInfo | None = None
    chileAdditionalInfo: TaxSettingsChileAdditionalInfo | None = None
    franceAdditionalInfo: TaxSettingsFranceAdditionalInfo | None = None
    monacoAdditionalInfo: TaxSettingsMonacoAdditionalInfo | None = None
    germanyAdditionalInfo: TaxSettingsGermanyAdditionalInfo | None = None
    mexicoAdditionalInfo: TaxSettingsMexicoAdditionalInfo | None = None
    colombiaAdditionalInfo: TaxSettingsColombiaAdditionalInfo | None = None
    unitedArabEmiratesAdditionalInfo: TaxSettingsUnitedArabEmiratesAdditionalInfo | None = None
    norwayAdditionalInfo: TaxSettingsNorwayAdditionalInfo | None = None
    newZealandAdditionalInfo: TaxSettingsNewZealandAdditionalInfo | None = None
