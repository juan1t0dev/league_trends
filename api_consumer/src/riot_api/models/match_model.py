from pydantic import Field, BaseModel
from typing import List, Optional


# ============================================================
# Hojas (sin dependencias)
# ============================================================

class PerkStatsDto(BaseModel):
    defense: int
    flex: int
    offense: int


class PerkStyleSelectionDto(BaseModel):
    perk: int
    var1: int
    var2: int
    var3: int


class PerkStyleDto(BaseModel):
    description: str
    selections: List[PerkStyleSelectionDto]
    style: int


class PerksDto(BaseModel):
    statPerks: PerkStatsDto
    styles: List[PerkStyleDto]


class BanDto(BaseModel):
    championId: int
    pickTurn: int


class ObjectiveDto(BaseModel):
    first: bool
    kills: int


class ObjectivesDto(BaseModel):
    baron: ObjectiveDto
    champion: ObjectiveDto
    dragon: ObjectiveDto
    horde: ObjectiveDto
    inhibitor: ObjectiveDto
    riftHerald: ObjectiveDto
    tower: ObjectiveDto


class TeamDto(BaseModel):
    bans: List[BanDto]
    objectives: ObjectivesDto
    teamId: int
    win: bool


class MissionsDto(BaseModel):
    playerScore0: Optional[int] = None
    playerScore1: Optional[int] = None
    playerScore2: Optional[int] = None
    playerScore3: Optional[int] = None
    playerScore4: Optional[int] = None
    playerScore5: Optional[int] = None
    playerScore6: Optional[int] = None
    playerScore7: Optional[int] = None
    playerScore8: Optional[int] = None
    playerScore9: Optional[int] = None
    playerScore10: Optional[int] = None
    playerScore11: Optional[int] = None


class ChallengesDto(BaseModel):
    model_config = {"populate_by_name": True}

    assistStreakCount: Optional[int] = Field(None, alias="12AssistStreakCount")
    baronBuffGoldAdvantageOverThreshold: Optional[int] = None
    controlWardTimeCoverageInRiverOrEnemyHalf: Optional[float] = None
    earliestBaron: Optional[float] = None
    earliestDragonTakedown: Optional[float] = None
    earliestElderDragon: Optional[float] = None
    earlyLaningPhaseGoldExpAdvantage: Optional[int] = None
    fasterSupportQuestCompletion: Optional[int] = None
    fastestLegendary: Optional[float] = None
    hadAfkTeammate: Optional[int] = None
    highestChampionDamage: Optional[int] = None
    highestCrowdControlScore: Optional[int] = None
    highestWardKills: Optional[int] = None
    junglerKillsEarlyJungle: Optional[int] = None
    killsOnLanersEarlyJungleAsJungler: Optional[int] = None
    laningPhaseGoldExpAdvantage: Optional[int] = None
    legendaryCount: Optional[int] = None
    maxCsAdvantageOnLaneOpponent: Optional[float] = None
    maxLevelLeadLaneOpponent: Optional[int] = None
    mostWardsDestroyedOneSweeper: Optional[int] = None
    mythicItemUsed: Optional[int] = None
    playedChampSelectPosition: Optional[int] = None
    soloTurretsLategame: Optional[int] = None
    takedownsFirst25Minutes: Optional[int] = None
    teleportTakedowns: Optional[int] = None
    thirdInhibitorDestroyedTime: Optional[int] = None
    threeWardsOneSweeperCount: Optional[int] = None
    visionScoreAdvantageLaneOpponent: Optional[float] = None
    InfernalScalePickup: Optional[int] = None
    fistBumpParticipation: Optional[int] = None
    voidMonsterKill: Optional[int] = None
    abilityUses: Optional[int] = None
    acesBefore15Minutes: Optional[int] = None
    alliedJungleMonsterKills: Optional[float] = None
    baronTakedowns: Optional[int] = None
    blastConeOppositeOpponentCount: Optional[int] = None
    bountyGold: Optional[float] = None
    buffsStolen: Optional[int] = None
    completeSupportQuestInTime: Optional[int] = None
    controlWardsPlaced: Optional[int] = None
    damagePerMinute: Optional[float] = None
    damageTakenOnTeamPercentage: Optional[float] = None
    dancedWithRiftHerald: Optional[int] = None
    deathsByEnemyChamps: Optional[int] = None
    dodgeSkillShotsSmallWindow: Optional[int] = None
    doubleAces: Optional[int] = None
    dragonTakedowns: Optional[int] = None
    legendaryItemUsed: Optional[List[int]] = None
    effectiveHealAndShielding: Optional[float] = None
    elderDragonKillsWithOpposingSoul: Optional[int] = None
    elderDragonMultikills: Optional[int] = None
    enemyChampionImmobilizations: Optional[int] = None
    enemyJungleMonsterKills: Optional[float] = None
    epicMonsterKillsNearEnemyJungler: Optional[int] = None
    epicMonsterKillsWithin30SecondsOfSpawn: Optional[int] = None
    epicMonsterSteals: Optional[int] = None
    epicMonsterStolenWithoutSmite: Optional[int] = None
    firstTurretKilled: Optional[int] = None
    firstTurretKilledTime: Optional[float] = None
    flawlessAces: Optional[int] = None
    fullTeamTakedown: Optional[int] = None
    gameLength: Optional[float] = None
    getTakedownsInAllLanesEarlyJungleAsLaner: Optional[int] = None
    goldPerMinute: Optional[float] = None
    hadOpenNexus: Optional[int] = None
    immobilizeAndKillWithAlly: Optional[int] = None
    initialBuffCount: Optional[int] = None
    initialCrabCount: Optional[int] = None
    jungleCsBefore10Minutes: Optional[float] = None
    junglerTakedownsNearDamagedEpicMonster: Optional[int] = None
    kda: Optional[float] = None
    killAfterHiddenWithAlly: Optional[int] = None
    killedChampTookFullTeamDamageSurvived: Optional[int] = None
    killingSprees: Optional[int] = None
    killParticipation: Optional[float] = None
    killsNearEnemyTurret: Optional[int] = None
    killsOnOtherLanesEarlyJungleAsLaner: Optional[int] = None
    killsOnRecentlyHealedByAramPack: Optional[int] = None
    killsUnderOwnTurret: Optional[int] = None
    killsWithHelpFromEpicMonster: Optional[int] = None
    knockEnemyIntoTeamAndKill: Optional[int] = None
    kTurretsDestroyedBeforePlatesFall: Optional[int] = None
    landSkillShotsEarlyGame: Optional[int] = None
    laneMinionsFirst10Minutes: Optional[int] = None
    lostAnInhibitor: Optional[int] = None
    maxKillDeficit: Optional[int] = None
    mejaisFullStackInTime: Optional[int] = None
    moreEnemyJungleThanOpponent: Optional[float] = None
    multiKillOneSpell: Optional[int] = None
    multikills: Optional[int] = None
    multikillsAfterAggressiveFlash: Optional[int] = None
    multiTurretRiftHeraldCount: Optional[int] = None
    outerTurretExecutesBefore10Minutes: Optional[int] = None
    outnumberedKills: Optional[int] = None
    outnumberedNexusKill: Optional[int] = None
    perfectDragonSoulsTaken: Optional[int] = None
    perfectGame: Optional[int] = None
    pickKillWithAlly: Optional[int] = None
    poroExplosions: Optional[int] = None
    quickCleanse: Optional[int] = None
    quickFirstTurret: Optional[int] = None
    quickSoloKills: Optional[int] = None
    riftHeraldTakedowns: Optional[int] = None
    saveAllyFromDeath: Optional[int] = None
    scuttleCrabKills: Optional[int] = None
    shortestTimeToAceFromFirstTakedown: Optional[float] = None
    skillshotsDodged: Optional[int] = None
    skillshotsHit: Optional[int] = None
    snowballsHit: Optional[int] = None
    soloBaronKills: Optional[int] = None
    SWARM_DefeatAatrox: Optional[int] = None
    SWARM_DefeatBriar: Optional[int] = None
    SWARM_DefeatMiniBosses: Optional[int] = None
    SWARM_EvolveWeapon: Optional[int] = None
    SWARM_Have3Passives: Optional[int] = None
    SWARM_KillEnemy: Optional[int] = None
    SWARM_PickupGold: Optional[float] = None
    SWARM_ReachLevel50: Optional[int] = None
    SWARM_Survive15Min: Optional[int] = None
    SWARM_WinWith5EvolvedWeapons: Optional[int] = None
    soloKills: Optional[int] = None
    stealthWardsPlaced: Optional[int] = None
    survivedSingleDigitHpCount: Optional[int] = None
    survivedThreeImmobilizesInFight: Optional[int] = None
    takedownOnFirstTurret: Optional[int] = None
    takedowns: Optional[int] = None
    takedownsAfterGainingLevelAdvantage: Optional[int] = None
    takedownsBeforeJungleMinionSpawn: Optional[int] = None
    takedownsFirstXMinutes: Optional[int] = None
    takedownsInAlcove: Optional[int] = None
    takedownsInEnemyFountain: Optional[int] = None
    teamBaronKills: Optional[int] = None
    teamDamagePercentage: Optional[float] = None
    teamElderDragonKills: Optional[int] = None
    teamRiftHeraldKills: Optional[int] = None
    tookLargeDamageSurvived: Optional[int] = None
    turretPlatesTaken: Optional[int] = None
    turretsTakenWithRiftHerald: Optional[int] = None
    turretTakedowns: Optional[int] = None
    twentyMinionsIn3SecondsCount: Optional[int] = None
    twoWardsOneSweeperCount: Optional[int] = None
    unseenRecalls: Optional[int] = None
    visionScorePerMinute: Optional[float] = None
    wardsGuarded: Optional[int] = None
    wardTakedowns: Optional[int] = None
    wardTakedownsBefore20M: Optional[int] = None


# ============================================================
# Nivel intermedio
# ============================================================

class ParticipantDto(BaseModel):
    allInPings: int
    assistMePings: int
    assists: int
    baronKills: int
    bountyLevel: Optional[int] = None
    champExperience: int
    champLevel: int
    championId: int
    championName: str
    commandPings: int
    championTransform: int
    consumablesPurchased: int
    challenges: Optional[ChallengesDto] = None
    damageDealtToBuildings: int
    damageDealtToObjectives: int
    damageDealtToTurrets: int
    damageSelfMitigated: int
    deaths: int
    detectorWardsPlaced: int
    doubleKills: int
    dragonKills: int
    eligibleForProgression: bool
    enemyMissingPings: int
    enemyVisionPings: int
    firstBloodAssist: bool
    firstBloodKill: bool
    firstTowerAssist: bool
    firstTowerKill: bool
    gameEndedInEarlySurrender: bool
    gameEndedInSurrender: bool
    holdPings: int
    getBackPings: int
    goldEarned: int
    goldSpent: int
    individualPosition: str
    inhibitorKills: int
    inhibitorTakedowns: int
    inhibitorsLost: int
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    itemsPurchased: int
    killingSprees: int
    kills: int
    lane: str
    largestCriticalStrike: int
    largestKillingSpree: int
    largestMultiKill: int
    longestTimeSpentLiving: int
    magicDamageDealt: int
    magicDamageDealtToChampions: int
    magicDamageTaken: int
    missions: Optional[MissionsDto] = None
    neutralMinionsKilled: int
    needVisionPings: int
    nexusKills: int
    nexusTakedowns: int
    nexusLost: int
    objectivesStolen: int
    objectivesStolenAssists: int
    onMyWayPings: int
    participantId: int
    playerScore0: Optional[int] = None
    playerScore1: Optional[int] = None
    playerScore2: Optional[int] = None
    playerScore3: Optional[int] = None
    playerScore4: Optional[int] = None
    playerScore5: Optional[int] = None
    playerScore6: Optional[int] = None
    playerScore7: Optional[int] = None
    playerScore8: Optional[int] = None
    playerScore9: Optional[int] = None
    playerScore10: Optional[int] = None
    playerScore11: Optional[int] = None
    pentaKills: int
    perks: Optional[PerksDto] = None
    physicalDamageDealt: int
    physicalDamageDealtToChampions: int
    physicalDamageTaken: int
    placement: int
    playerAugment1: int
    playerAugment2: int
    playerAugment3: int
    playerAugment4: int
    playerSubteamId: int
    pushPings: int
    profileIcon: int
    puuid: str
    quadraKills: int
    riotIdGameName: str
    riotIdTagline: str
    role: str
    sightWardsBoughtInGame: int
    spell1Casts: int
    spell2Casts: int
    spell3Casts: int
    spell4Casts: int
    subteamPlacement: int
    summoner1Casts: int
    summoner1Id: int
    summoner2Casts: int
    summoner2Id: int
    summonerId: str
    summonerLevel: int
    summonerName: str
    teamEarlySurrendered: bool
    teamId: int
    teamPosition: str
    timeCCingOthers: int
    timePlayed: int
    totalAllyJungleMinionsKilled: int
    totalDamageDealt: int
    totalDamageDealtToChampions: int
    totalDamageShieldedOnTeammates: int
    totalDamageTaken: int
    totalEnemyJungleMinionsKilled: int
    totalHeal: int
    totalHealsOnTeammates: int
    totalMinionsKilled: int
    totalTimeCCDealt: int
    totalTimeSpentDead: int
    totalUnitsHealed: int
    tripleKills: int
    trueDamageDealt: int
    trueDamageDealtToChampions: int
    trueDamageTaken: int
    turretKills: int
    turretTakedowns: int
    turretsLost: int
    unrealKills: int
    visionScore: int
    visionClearedPings: int
    visionWardsBoughtInGame: int
    wardsKilled: int
    wardsPlaced: int
    win: bool


class InfoDto(BaseModel):
    endOfGameResult: Optional[str] = None
    gameCreation: int
    gameDuration: int
    gameEndTimestamp: int
    gameId: int
    gameMode: str
    gameName: str
    gameStartTimestamp: int
    gameType: str
    gameVersion: str
    mapId: int
    participants: List[ParticipantDto]
    platformId: str
    queueId: int
    teams: List[TeamDto]
    tournamentCode: Optional[str] = None


class MetadataDto(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[str]


# ============================================================
# Raíz
# ============================================================

class MatchDto(BaseModel):
    metadata: MetadataDto
    info: InfoDto