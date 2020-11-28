import dataclasses
import typing


@dataclasses.dataclass
class Summoner:
    account_id: str
    sumoner_id: str
    puuid: str
    name: str
    summoner_level: int
    profile_icon_id: int
    revision_date: int
    timestamp: str


@dataclasses.dataclass
class Match:
    game_id: str
    platform_id: str
    game_creation: int
    game_duration: int
    queue_id: int
    map_id: int
    season_id: int
    game_version: str
    game_mode: str
    game_type: str


@dataclasses.dataclass
class MatchReference:
    game_id: int
    account_id: str


@dataclasses.dataclass
class Team:
    team_id: str
    game_id: str
    win: str
    first_blood: int
    first_tower: int
    first_inhibitor: int
    first_baron: int
    first_dragon: int
    first_rift_herald: int
    tower_kills: int
    inhibitor_kills: int
    baron_kills: int
    dragon_kills: int
    rift_herald_kills: int
    bans: typing.List[int]


@dataclasses.dataclass
class Champion:
    champion_id: int
    name: str
    classes: typing.List[str]


@dataclasses.dataclass
class Timeline:
    timeline_id: str
    creeps_per_min_deltas: dict
    xp_per_min_deltas: dict
    gold_per_min_deltas: dict
    cs_diff_per_min_deltas: dict
    xp_diff_per_min_deltas: dict
    damage_taken_per_min_deltas: dict
    damage_taken_diff_per_min_deltas: dict


@dataclasses.dataclass
class Stat:
    stat_id: str
    win: bool
    items: typing.List[int]
    kills: int
    deaths: int
    assists: int
    largestKillingSpree: int
    largestMultiKill: int
    killingSprees: int
    longestTimeSpentLiving: int
    doubleKills: int
    tripleKills: int
    quadraKills: int
    pentaKills: int
    totalDamageDealt: int
    magicDamageDealt: int
    physicalDamageDealt: int
    trueDamageDealt: int
    largestCriticalStrike: int
    totalDamageDealtToChampions: int
    magicDamageDealtToChampions: int
    physicalDamageDealtToChampions: int
    trueDamageDealtToChampions: int
    totalHeal: int
    totalUnitsHealed: int
    damageSelfMitigated: int
    damageDealtToObjectives: int
    damageDealtToTurrets: int
    visionScore: int
    timeCCingOthers: int
    totalDamageTaken: int
    magicalDamageTaken: int
    physicalDamageTaken: int
    trueDamageTaken: int
    goldEarned: int
    goldSpent: int
    turretKills: int
    inhibitorKills: int
    totalMinionsKilled: int
    neutralMinionsKilledTeamJungle: int
    neutralMinionsKilledEnemyJungle: int
    totalTimeCrowdControlDealt: int
    champLevel: int
    visionWardsBoughtInGame: int
    sightWardsBoughtInGame: int
    wardsPlaced: int
    wardsKilled: int
    firstBloodKill: bool
    firstBloodAssist: bool
    firstTowerKill: bool
    firstTowerAssist: bool
    firstInhibitorKill: bool
    firstInhibitorAssist: bool
    combatPlayerScore: int
    objectivePlayerScore: int
    totalPlayerScore: int
    totalScoreRank: int
    playerScore0: int
    playerScore1: int
    playerScore2: int
    playerScore3: int
    playerScore4: int
    playerScore5: int
    playerScore6: int
    playerScore7: int
    playerScore8: int
    playerScore9: int
    perk0: int
    perk0Var1: int
    perk0Var2: int
    perk0Var3: int
    perk1: int
    perk1Var1: int
    perk1Var2: int
    perk1Var3: int
    perk2: int
    perk2Var1: int
    perk2Var2: int
    perk2Var3: int
    perk3: int
    perk3Var1: int
    perk3Var2: int
    perk3Var3: int
    perk4: int
    perk4Var1: int
    perk4Var2: int
    perk4Var3: int
    perk5: int
    perk5Var1: int
    perk5Var2: int
    perk5Var3: int
    perkPrimaryStyle: int
    perkSubStyle: int
    statPerk0: int
    statPerk1: int
    statPerk2: int


@dataclasses.dataclass
class Participant:
    participant_id: str
    game_id: str
    account_id: str
    champion_id: int
    stat_id: str
    timeline_id: str
    spell1_id: int
    spell2_id: int
    role: str
    lane: str


@dataclasses.dataclass
class ParticipantFrame:
    participant_id: str
    timestamp: int
    minions_killed: int
    team_score: int
    total_gold: int
    level: int
    xp: int
    current_gold: int
    position: tuple
    jungle_minions_killed: int


@dataclasses.dataclass
class Event:
    participant_id: str
    timestamp: int
    lane_type: str
    skill_slot: int
    ascended_type: str
    creator_id: int
    after_id: int
    event_type: str
    type: str
    level_up_type: str
    ward_type: str
    tower_type: str
    item_id: int
    before_id: int
    monster_type: str
    monster_sub_type: str
    position: tuple
    killer_id: str
    assisting_participant_ids: str
    building_type: str
    victim_id: str
