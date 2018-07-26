from pkgutil import get_data
import scrapy
from scrapy_splash import SplashRequest
from w3lib.http import basic_auth_header
from __future__ import absolute_import
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule
from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import FundraiserByTayTomNguyenBuildingElementarItem, FundraiserForVaghinakKhachatryanByMakeEItem, FundraiserByIgemGttingenGlyphosateOnMyPlItem, FundraiserByNataliaParedesAcuaWeekMissioItem, FundraiserByAbbasHusseinSaveMeFromUniverItem, FundraiserByCeliaIncognitoKinderBrauchenIItem, FundraiserForThomasHartleibByBernadetteAltItem, FundraiserByPaulMeckerHelpingHandsForAfrItem, FundraiserForLuljetaLumiByRebekaAneqBekiItem, FundraiserByMichelleWielBennoInNotItem, FundraiserByGeronimoScherlerDeathICantAfItem, FundraiserForDavinaHartsfieldByAlisonDisarItem, FundraiserForCelenaZevnikByJenniferLynneItem, FundraiserByDebbieSpillaneSawasNewShelterItem, FundraiserByJohnWoodardSeanWurtzelItem, FundraiserByClaudiaBetzHauboldHanaVliegenItem, FundraiserByGasparyanSerobSerobGasparyanItem, FundraiserByLyraPramukLyrasGenderAffirmatItem, FundraiserByYonTongStudyTibetanItem, FundraiserForDarrellMielkeByShannonRempeItem, FundraiserByEviWagnerHilfeFrFritzItem, FundraiserByPhilipLappleVeteranRelocatingItem, FundraiserForKeitaWilliamsByMoeChoiDjSpItem, FundraiserForPhanindraGByAkshatJainPhaniItem, FundraiserByFreibergerNicholasMarathonForItem, FundraiserForEbonieMarieBaxterByTiaRobinsItem, FundraiserByAnnKreidlePennAlexanderRobotiItem, FundraiserForKiantePowellByIshmalePowellItem, FundraiserByShatangelaPattonHelpAaliyahKiItem, FundraiserByStephenHallMichaelDarsMedicalItem, FundraiserForBramPinkleyByTysonPinkleyHeItem, ResultsPageItem, FundraiserByChrisMerrittChrisCareerRebootItem, FundraiserByShirleyCoventryColinsCancerMeItem, FundraiserForValerieFarrarByPamShackelfordItem, FundraiserByJadeThorpeJadesMedicalFundItem, FundraiserForJeffreyLucasByJaybirdMarionItem, FundraiserByMahfuzaPatelIssasSpecialNeedsItem, FundraiserByKevinVanessaGoreFuneralExpensItem, FundraiserForHollyHarrisonBySusanHarrisonItem, FundraiserByEdwinCruzMelissaGuadalupeHernItem, PortiaItem


class GofundmeCom_1(BasePortiaSpider):
    name = "www.gofundme.com_1"
    allowed_domains = ['www.gofundme.com']
    start_urls = [{'fragments': [{'type': 'fixed',
                                  'valid': True,
                                  'value': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=GB&page='},
                                 {'type': 'range',
                                  'valid': True,
                                  'value': '1-2000'}],
                   'type': 'generated',
                   'url': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=GB&page=[1-2000]'},
                  {'fragments': [{'type': 'fixed',
                                  'valid': True,
                                  'value': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=US&page='},
                                 {'type': 'range',
                                  'valid': True,
                                  'value': '1-2000'}],
                   'type': 'generated',
                   'url': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=US&page=[1-2000]'},
                  'https://www.gofundme.com/discover/medical-fundraiser',
                  {'fragments': [{'type': 'fixed',
                                  'valid': True,
                                  'value': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=DE&page='},
                                 {'type': 'range',
                                  'valid': True,
                                  'value': '1-2000'}],
                   'type': 'generated',
                   'url': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=DE&page=[1-2000]'},
                  {'fragments': [{'type': 'fixed',
                                  'valid': True,
                                  'value': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=FR&page='},
                                 {'type': 'range',
                                  'valid': True,
                                  'value': '1-2000'}],
                   'type': 'generated',
                   'url': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=FR&page=[1-2000]'},
                  {'fragments': [{'type': 'fixed',
                                  'valid': True,
                                  'value': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=NE&page='},
                                 {'type': 'range',
                                  'valid': True,
                                  'value': '1-2000'}],
                   'type': 'generated',
                   'url': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=NE&page=[1-2000]'},
                  {'fragments': [{'type': 'fixed',
                                  'valid': True,
                                  'value': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=ES&page='},
                                 {'type': 'range',
                                  'valid': True,
                                  'value': '1-2000'}],
                   'type': 'generated',
                   'url': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=ES&page=[1-2000]'},
                  {'fragments': [{'type': 'fixed',
                                  'valid': True,
                                  'value': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=IT&page='},
                                 {'type': 'range',
                                  'valid': True,
                                  'value': '1-2000'}],
                   'type': 'generated',
                   'url': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=IT&page=[1-2000]'},
                  {'fragments': [{'type': 'fixed',
                                  'valid': True,
                                  'value': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=PT&page='},
                                 {'type': 'range',
                                  'valid': True,
                                  'value': '1-2000'}],
                   'type': 'generated',
                   'url': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=PT&page=[1-2000]'},
                  {'fragments': [{'type': 'fixed',
                                  'valid': True,
                                  'value': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=AU&page='},
                                 {'type': 'range',
                                  'valid': True,
                                  'value': '1-2000'}],
                   'type': 'generated',
                   'url': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=AU&page=[1-2000]'},
                  {'fragments': [{'type': 'fixed',
                                  'valid': True,
                                  'value': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=MX&page='},
                                 {'type': 'range',
                                  'valid': True,
                                  'value': '1-2000'}],
                   'type': 'generated',
                   'url': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=MX&page=[1-2000]'},
                  {'fragments': [{'type': 'fixed',
                                  'valid': True,
                                  'value': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=CA&page='},
                                 {'type': 'range',
                                  'valid': True,
                                  'value': '1-2000'}],
                   'type': 'generated',
                   'url': 'https://www.gofundme.com/mvc.php?route=category&term=medical&country=CA&page=[1-2000]'}]
    rules = [
        Rule(
            LinkExtractor(
                allow=('gofundme.com'),
                deny=(
                    'privacy$',
                    'sign-up$',
                    'tour$',
                    'school-fundraising$',
                    'natural-disasters$',
                    'emergency-accident-fundraising$',
                    'legal$',
                    'volunteer-fundraising$',
                    'contact$',
                    'signup_new$',
                    'hurricaneharvey$',
                    'emergency-fundraiser$',
                    'cpgn_share$',
                    'education-fundraiser$',
                    'subpoena$',
                    'sign-in$',
                    'guides',
                    'terms$',
                    'jobs$',
                    'classroom-fundraisers$',
                    'event-fundraiser$')),
            callback='parse_item',
            follow=True)]
    items = [
        [
            Item(
                FundraiserByEdwinCruzMelissaGuadalupeHernItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-18080338 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'closed',
                        '.static-btn-contain > .is-disabled *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-btns-contain:nth-child(6) > div:nth-child(4) > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '.created-date *::text',
                        [],
                        True),
                    Field(
                        'field1',
                        '.co-info:nth-child(5) > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(5) > .co-details > .js-profile-co *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        'span.text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '.js-location-link *::text',
                        [],
                        True),
                    Field(
                        'field2',
                        '.js-location-link::attr(href)',
                        [],
                        True)]),
            Item(
                FundraiserByJadeThorpeJadesMedicalFundItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-7020541 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'field2',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'creator',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '.icon-link:nth-child(2) *::text',
                        [],
                        True),
                    Field(
                        'field1',
                        '.icon-link:nth-child(2)::attr(href)',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'comments',
                        '.show-for-large:nth-child(8) > .js-comments-contain > .column > .comments-control-footer > .row *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '.created-date *::text',
                        [],
                        True)]),
            Item(
                FundraiserByAbbasHusseinSaveMeFromUniverItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-30741816 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'images',
                        '#js-open-media-viewer *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'closed',
                        '.static-btn-contain > .is-disabled *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'tag',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByKevinVanessaGoreFuneralExpensItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-16725540 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'field1',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'creator',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .icon-link *::text',
                        [],
                        True),
                    Field(
                        'field2',
                        '#story > div:nth-child(1) > .co-info > .co-details > .icon-link::attr(href)',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '.created-date *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        'span.text-small *::text',
                        [],
                        True)]),
            Item(
                FundraiserForHollyHarrisonBySusanHarrisonItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-18957912 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'field1',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'creator',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '.icon-link:nth-child(3) *::text',
                        [],
                        True),
                    Field(
                        'field2',
                        '.icon-link:nth-child(3)::attr(href)',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '.created-date *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        'span.text-small *::text',
                        [],
                        True)]),
            Item(
                FundraiserForEbonieMarieBaxterByTiaRobinsItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-29982126 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'images',
                        '#js-open-media-viewer *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        []),
                    Field(
                        'tag',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserForJeffreyLucasByJaybirdMarionItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-31000810 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'field1',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name::attr(href)',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByShirleyCoventryColinsCancerMeItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-15539443 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.mt0 > .hide-for-large > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.mt0 > .hide-for-large > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.mt0 > .hide-for-large > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.mt0 > .ugc-connection > .story-updates > li:nth-child(2) > a > .badge *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.mt0 > .ugc-connection > .tabs-content > .is-active > .co-story *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '.created-date *::text',
                        [],
                        True),
                    Field(
                        'campaign_creator_url',
                        '.co-info:nth-child(5) > .co-details > .js-profile-co *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        'span.text-small *::text',
                        [],
                        True),
                    Field(
                        'comments',
                        '.hide-for-large:nth-child(8) > .js-comments-contain > .column > .comments-control-footer > .row *::text',
                        [],
                        True)]),
            Item(
                FundraiserByClaudiaBetzHauboldHanaVliegenItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'campaign_creator_url',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByMahfuzaPatelIssasSpecialNeedsItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-18120894 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'field2',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'creator',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '.icon-link:nth-child(2) *::text',
                        [],
                        True),
                    Field(
                        'field1',
                        '.icon-link:nth-child(2)::attr(href)',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story > p:nth-child(1) *::text',
                        [],
                        True)]),
            Item(
                FundraiserByStephenHallMichaelDarsMedicalItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-31230218 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'images',
                        '#js-open-media-viewer *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'tag',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserForKiantePowellByIshmalePowellItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'campaign_creator_url',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserForThomasHartleibByBernadetteAltItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'campaign_creator_url',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserForKeitaWilliamsByMoeChoiDjSpItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-30635102 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'campaign_creator_url',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-badge-side-column > .co-info > .co-details > .js-profile-co *::text',
                        [],
                        True)]),
            Item(
                FundraiserByLyraPramukLyrasGenderAffirmatItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-30178800 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'images',
                        '#js-open-media-viewer *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByMichelleWielBennoInNotItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'field1',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'creator',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True)]),
            Item(
                FundraiserForPhanindraGByAkshatJainPhaniItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-18625664 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'closed',
                        '.static-btn-contain > .is-disabled *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '.icon-link:nth-child(3) *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story > p *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.js-co-orbit-container > .is-active > .mb20 > .co-info > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserForValerieFarrarByPamShackelfordItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByGeronimoScherlerDeathICantAfItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByChrisMerrittChrisCareerRebootItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '.layer-white:nth-child(5) > .campaign-status *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'campaign_creator_url',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByEviWagnerHilfeFrFritzItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByFreibergerNicholasMarathonForItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(8)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.fs-12-5 *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'campaign_creator_url',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.donations-column-contain > .column > .mb *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserForDavinaHartsfieldByAlisonDisarItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-19640040 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '.icon-link:nth-child(3) *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.js-co-orbit-container > .is-active > .mb20 > .co-info > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByPaulMeckerHelpingHandsForAfrItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(8)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'campaign_creator_url',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'field1',
                        '.co-badge-side-column > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-badge-side-column > .co-info > .co-details > .js-profile-co *::text',
                        [],
                        True)]),
            Item(
                FundraiserForLuljetaLumiByRebekaAneqBekiItem,
                None,
                'html',
                [
                    Field(
                        'canonical_url',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True)]),
            Item(
                FundraiserByDebbieSpillaneSawasNewShelterItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'creator_url',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'creator',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'comments',
                        '.hide-for-large:nth-child(8) > .js-comments-contain > .column > .comments-control-footer > .row *::text',
                        [],
                        True)]),
            Item(
                FundraiserForDarrellMielkeByShannonRempeItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'likes',
                        '.heart-31006856 > .fave-num-short > .roundedNum *::text',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True)]),
            Item(
                FundraiserByAnnKreidlePennAlexanderRobotiItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '#js-main-column > .campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '#js-main-column > .hide-for-large > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '#js-main-column > .hide-for-large > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '#js-main-column > .hide-for-large > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#js-main-column > .ugc-connection > .tabs-panel > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'campaign_creator_url',
                        '#js-main-column > .ugc-connection > .tabs-panel > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'tags',
                        '#js-main-column > .ugc-connection > .tabs-panel > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#js-main-column > .ugc-connection > .tabs-panel > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '#js-main-column > .ugc-connection > .tabs-panel > .co-story *::text',
                        [],
                        True)]),
            Item(
                FundraiserByShatangelaPattonHelpAaliyahKiItem,
                None,
                '.pg-campaign',
                [
                    Field(
                        'title',
                        '.main-column > .campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.mt0 > .hide-for-large > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.mt0 > .hide-for-large > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.mt0 > .hide-for-large > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.mt0 > .ugc-connection > .story-updates > li:nth-child(2) > a > .badge *::text',
                        [],
                        True),
                    Field(
                        'campaign_creator_url',
                        '.mt0 > .ugc-connection > .tabs-content > .is-active > div:nth-child(1) > .co-info > .co-details > .js-profile-co *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.mt0 > .ugc-connection > .tabs-content > .is-active > .co-story *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '.mt0 > .ugc-connection > .tabs-content > .is-active > div:nth-child(1) > .show-for-large > .created-date *::text, .mt0 > .co-badge-side-column > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        '.mt0 > .ugc-connection > .tabs-content > .is-active > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text, .mt0 > .co-badge-side-column > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True)]),
            Item(
                FundraiserByNataliaParedesAcuaWeekMissioItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True)]),
            Item(
                FundraiserForCelenaZevnikByJenniferLynneItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '.icon-link:nth-child(3) *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.js-co-orbit-container > .is-active > .mb20 > .co-info > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByGasparyanSerobSerobGasparyanItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'share',
                        '.fs-12-5 *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        [],
                        True),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story > strong *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserForVaghinakKhachatryanByMakeEItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'updates',
                        '.badge *::text',
                        [],
                        True),
                    Field(
                        'campaign_creator_url',
                        '#story > div:nth-child(1) > .co-info > .co-details > .js-profile-co::attr(href)',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True)]),
            Item(
                FundraiserByJohnWoodardSeanWurtzelItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.js-co-orbit-container > .is-active > .mb20 > .co-info > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByPhilipLappleVeteranRelocatingItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal *::text',
                        [],
                        True),
                    Field(
                        'date',
                        '#story > div:nth-child(1) > .show-for-large > .created-date *::text',
                        [],
                        True),
                    Field(
                        'tags',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .category-link-name > .text-small *::text',
                        []),
                    Field(
                        'location',
                        '#story > div:nth-child(1) > .co-info > .co-details > .pills-contain > .location-name *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByIgemGttingenGlyphosateOnMyPlItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'shares',
                        '.share-text > div > .js-share-count-text *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True)]),
            Item(
                FundraiserByYonTongStudyTibetanItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.co-info:nth-child(1) > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserForBramPinkleyByTysonPinkleyHeItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'funds',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > .smaller *::text',
                        [],
                        True),
                    Field(
                        'donors',
                        '.layer-white:nth-child(5) > .campaign-status > span *::text',
                        [],
                        True),
                    Field(
                        'creator',
                        '.theme-gfmgreen > div:nth-child(27) > .modal-contact-organizer > .medium-9 > .orbit-container > .is-active > .mb20 > .co-info > .co-details > strong *::text',
                        [],
                        True)]),
            Item(
                FundraiserByTayTomNguyenBuildingElementarItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True),
                    Field(
                        'title',
                        '.campaign-title *::text',
                        [],
                        True),
                    Field(
                        'goal',
                        '.layer-white:nth-child(5) > .goal > strong *::text',
                        [],
                        True),
                    Field(
                        'description',
                        '.co-story *::text',
                        [],
                        True)]),
            Item(
                ResultsPageItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(5)::attr(href)',
                        []),
                    Field(
                        'category',
                        'h1 *::text',
                        []),
                    Field(
                        'results',
                        'h2 *::text',
                        []),
                    Field(
                        'firstcampaignofpage',
                        '.cell:nth-child(1) > .react-campaign-tile > .react-campaign-tile-details > div:nth-child(2) > a > .clamp *::text',
                        [])]),
            Item(
                FundraiserByCeliaIncognitoKinderBrauchenIItem,
                None,
                'html',
                [
                    Field(
                        'canonical',
                        'link:nth-child(7)::attr(href)',
                        [],
                        True)])]]

    def __init__(self, *args, **kwargs):
        # to be able to load the Lua script on Scrapy Cloud, make sure your
        # project's setup.py file contains the "package_data" setting, similar
        # to this project's setup.py
        self.LUA_SOURCE = get_data(
            'splash_crawlera_example', 'scripts/crawlera.lua'
        ).decode('utf-8')
        super(GofundmeCom_1, self).__init__(*args, **kwargs)

