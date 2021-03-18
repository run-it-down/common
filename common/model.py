import dataclasses
import typing


@dataclasses.dataclass(frozen=True)
class Summoner:
    account_id: str
    summoner_id: str
    puuid: str
    name: str
    summoner_level: int
    profile_icon_id: int
    revision_date: int
    timestamp: str


@dataclasses.dataclass(frozen=True)
class Match:
    game_id: int
    platform_id: str
    game_creation: int
    game_duration: int
    queue_id: int
    map_id: int
    season_id: int
    game_version: str
    game_mode: str
    game_type: str


@dataclasses.dataclass(frozen=True)
class SummonerMatch:
    account_id: str
    game_id: int


@dataclasses.dataclass(frozen=True)
class Team:
    team_id: int
    game_id: int
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


@dataclasses.dataclass(frozen=True)
class Champion:
    champion_id: int
    name: str
    classes: typing.List[str]


@dataclasses.dataclass(frozen=True)
class Timeline:
    timeline_id: str
    creeps_per_min_deltas: typing.Mapping[str, float]
    xp_per_min_deltas: typing.Mapping[str, float]
    gold_per_min_deltas: typing.Mapping[str, float]
    cs_diff_per_min_deltas: typing.Mapping[str, float]
    xp_diff_per_min_deltas: typing.Mapping[str, float]
    damage_taken_per_min_deltas: typing.Mapping[str, float]
    damage_taken_diff_per_min_deltas: typing.Mapping[str, float]


@dataclasses.dataclass(frozen=True)
class Stat:
    stat_id: str
    win: bool
    items: typing.List[int]
    kills: int
    deaths: int
    assists: int
    largest_killing_spree: int
    largest_multi_kill: int
    killing_sprees: int
    longest_time_spent_living: int
    double_kills: int
    triple_kills: int
    quadra_kills: int
    penta_kills: int
    total_damage_dealt: int
    magic_damage_dealt: int
    physical_damage_dealt: int
    true_damage_dealt: int
    largest_critical_strike: int
    total_damage_dealt_to_champions: int
    magic_damage_dealt_to_champions: int
    physical_damage_dealt_to_champions: int
    true_damage_dealt_to_champions: int
    total_heal: int
    total_units_healed: int
    damage_self_mitigated: int
    damage_dealt_to_objectives: int
    damage_dealt_to_turrets: int
    vision_score: int
    time_ccing_others: int
    total_damage_taken: int
    magical_damage_taken: int
    physical_damage_taken: int
    true_damage_taken: int
    gold_earned: int
    gold_spent: int
    turret_kills: int
    inhibitor_kills: int
    total_minions_killed: int
    neutral_minions_killed_team_jungle: int
    neutral_minions_killed_enemy_jungle: int
    total_time_crowd_control_dealt: int
    champ_level: int
    vision_wards_bought_in_game: int
    sight_wards_bought_in_game: int
    wards_placed: int
    wards_killed: int
    first_blood_kill: bool
    first_blood_assist: bool
    first_tower_kill: bool
    first_tower_assist: bool
    first_inhibitor_kill: bool
    first_inhibitor_assist: bool
    combat_player_score: int
    objective_player_score: int
    total_player_score: int
    total_score_rank: int
    perk0: int
    perk0_var1: int
    perk0_var2: int
    perk0_var3: int
    perk1: int
    perk1_var1: int
    perk1_var2: int
    perk1_var3: int
    perk2: int
    perk2_var1: int
    perk2_var2: int
    perk2_var3: int
    perk3: int
    perk3_var1: int
    perk3_var2: int
    perk3_var3: int
    perk4: int
    perk4_var1: int
    perk4_var2: int
    perk4_var3: int
    perk5: int
    perk5_var1: int
    perk5_var2: int
    perk5_var3: int
    perk_primary_style: int
    perk_sub_style: int
    stat_perk0: int
    stat_perk1: int
    stat_perk2: int


@dataclasses.dataclass(frozen=True)
class Participant:
    participant_id: str
    game_id: int
    account_id: str
    champion_id: int
    stat_id: str
    team_id: int
    timeline_id: str
    spell1_id: int
    spell2_id: int
    role: str
    lane: str


@dataclasses.dataclass(frozen=True)
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


@dataclasses.dataclass(frozen=True)
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
    assisting_participant_ids: typing.List[str]
    building_type: str
    victim_id: str


@dataclasses.dataclass(frozen=True)
class AnalyseRequest:
    summoner_name: str
    summoner_name_buddy: str
    request_time: str
