from __future__ import absolute_import

import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, Identity
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image


class PortiaItem(scrapy.Item):
    fields = defaultdict(
        lambda: scrapy.Field(
            input_processor=Identity(),
            output_processor=Identity()
        )
    )

    def __setitem__(self, key, value):
        self._values[key] = value

    def __repr__(self):
        data = str(self)
        if not data:
            return '%s' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, data)

    def __str__(self):
        if not self._values:
            return ''
        string = super(PortiaItem, self).__repr__()
        return string


class FundraiserByTayTomNguyenBuildingElementarItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    lo = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserForVaghinakKhachatryanByMakeEItem(PortiaItem):
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )


class FundraiserByIgemGttingenGlyphosateOnMyPlItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByNataliaParedesAcuaWeekMissioItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByAbbasHusseinSaveMeFromUniverItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    closed = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tag = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByCeliaIncognitoKinderBrauchenIItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserForThomasHartleibByBernadetteAltItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    locat = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByPaulMeckerHelpingHandsForAfrItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field1 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserForLuljetaLumiByRebekaAneqBekiItem(PortiaItem):
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    contributors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    canonical_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByMichelleWielBennoInNotItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field1 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByGeronimoScherlerDeathICantAfItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserForDavinaHartsfieldByAlisonDisarItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserForCelenaZevnikByJenniferLynneItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByDebbieSpillaneSawasNewShelterItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    comments = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByJohnWoodardSeanWurtzelItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByClaudiaBetzHauboldHanaVliegenItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    locatio = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByGasparyanSerobSerobGasparyanItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    share = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByLyraPramukLyrasGenderAffirmatItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByYonTongStudyTibetanItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserForDarrellMielkeByShannonRempeItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByEviWagnerHilfeFrFritzItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByPhilipLappleVeteranRelocatingItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserForKeitaWilliamsByMoeChoiDjSpItem(PortiaItem):
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    cam = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )


class FundraiserForPhanindraGByAkshatJainPhaniItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    closed = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByFreibergerNicholasMarathonForItem(PortiaItem):
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserForEbonieMarieBaxterByTiaRobinsItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tag = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByAnnKreidlePennAlexanderRobotiItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserForKiantePowellByIshmalePowellItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByShatangelaPattonHelpAaliyahKiItem(PortiaItem):
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    comments = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByStephenHallMichaelDarsMedicalItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tag = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserForBramPinkleyByTysonPinkleyHeItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    closed = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class ResultsPageItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    category = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    results = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    nextpage = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    firstcampaignofpage = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    alternate = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )


class FundraiserByChrisMerrittChrisCareerRebootItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    comments = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByShirleyCoventryColinsCancerMeItem(PortiaItem):
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    campaign_creator_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    comments = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )


class FundraiserForValerieFarrarByPamShackelfordItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    images = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByJadeThorpeJadesMedicalFundItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field1 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field2 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    comments = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserForJeffreyLucasByJaybirdMarionItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field1 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByMahfuzaPatelIssasSpecialNeedsItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field1 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field2 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByKevinVanessaGoreFuneralExpensItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field1 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field2 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserForHollyHarrisonBySusanHarrisonItem(PortiaItem):
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field1 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field2 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class FundraiserByEdwinCruzMelissaGuadalupeHernItem(PortiaItem):
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    funds = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    goal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    donors = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    closed = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    likes = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    updates = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    date = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field1 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    creator = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    tags = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field2 = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    shares = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    canonical = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
