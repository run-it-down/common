from dataclasses import dataclass
import typing


@dataclass
class MasteryDto:
    rank: int
    master_id: int


@dataclass
class ParticipantTimelineDto:
    participant_id: int
    cs_diff_per_min_deltas: typing.Mapping[str, float]
    damage_taken_per_min_deltas: typing.Mapping[str, float]
    role: str
    damage_taken_diff_per_min_deltas: typing.Mapping[str, float]
    xp_per_min_deltas: typing.Mapping[str, float]
    xp_diff_per_min_deltas: typing.Mapping[str, float]
    lane: str
    creeps_per_min_deltas: typing.Mapping[str, float]
    gold_per_min_deltas: typing.Mapping[str, float]


@dataclass
class ParticipantStatsDto:
    item0: int
    item2: int
    total_units_healed: int
    item1: int
    largest_multi_kill: int
    gold_earned: int
    first_inhibitor_kill: bool
    physical_damage_taken: int
    node_neutralize_assist: int
    total_player_score: int
    champ_level: int
    damage_dealt_to_objectives: int
    total_damage_taken: int
    neutral_minions_killed: int
    deaths: int
    triple_kills: int
    magic_damage_dealt_to_champions: int
    wards_killed: int
    penta_kills: int
    damage_self_mitigated: int
    largest_critical_strike: int
    node_neutralize: int
    total_time_crowd_control_dealt: int
    first_tower_kill: bool
    magic_damage_dealt: int
    total_score_rank: int
    node_capture: int
    wards_placed: int
    total_damage_dealt: int
    time_ccing_others: int
    magical_damage_taken: int
    largest_killing_spree: int
    total_damage_dealt_to_champions: int
    physical_damage_dealt_to_champions: int
    neutral_minions_killed_team_jungle: int
    total_minions_killed: int
    first_inhibitor_assist: bool
    vision_wards_bought_in_game: int
    objective_player_score: int
    kills: int
    first_tower_assist: bool
    combat_player_score: int
    inhibitor_kills: int
    turret_kills: int
    participant_id: int
    true_damage_taken: int
    first_blood_assist: bool
    node_capture_assist: int
    assists: int
    team_objective: int
    altars_neutralized: int
    gold_spent: int
    damage_dealt_to_turrets: int
    altars_captured: int
    win: bool
    total_heal: int
    unreal_kills: int
    vision_score: int
    physical_damage_dealt: int
    first_blood_kill: bool
    longest_time_spent_living: int
    killing_sprees: int
    sight_wards_bought_in_game: int
    true_damage_dealt_to_champions: int
    neutral_minions_killed_enemy_jungle: int
    double_kills: int
    true_damage_dealt: int
    quadra_kills: int
    item4: int
    item3: int
    item6: int
    item5: int
    player_score0: int
    player_score1: int
    player_score2: int
    player_score3: int
    player_score4: int
    player_score5: int
    player_score6: int
    player_score7: int
    player_score8: int
    player_score9: int
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


@dataclass
class RuneDto:
    rune_id: int
    rank: int


@dataclass
class ParticipantDto:
    participant_id: int
    champion_id: int
    runes: typing.List[RuneDto]
    stats: ParticipantStatsDto
    team_id: int
    timeline: ParticipantTimelineDto
    spell1_id: int
    spell2_id: int
    highest_achieved_season_tier: str
    masteries: typing.List[MasteryDto]


@dataclass
class TeamBansDto:
    champion_id: int
    pick_turn: int


@dataclass
class TeamStatsDto:
    tower_kills: int
    rift_herald_kills: int
    first_blood: bool
    inhibitor_kills: int
    bans: typing.List[TeamBansDto]
    first_baron: bool
    first_dragon: bool
    dominion_victory_score: int
    dragon_kills: int
    baron_kills: int
    first_inhibitor: bool
    first_tower: bool
    vilemaw_kills: int
    first_rift_herald: bool
    team_id: int
    win: str


@dataclass
class PlayerDto:
    profile_icon: int
    account_id: str
    match_history_uri: str
    current_account_id: str
    current_platform_id: str
    summoner_name: str
    summoner_id: str
    platform_id: str


@dataclass
class ParticipantIdentityDto:
    participant_id: int
    player: PlayerDto


@dataclass
class MatchDto:
    game_id: int
    participant_identities: typing.List[ParticipantIdentityDto]
    queue_id: int
    game_type: str
    game_duration: int
    teams: typing.List[TeamStatsDto]
    platform_id: str
    game_creation: int
    season_id: int
    game_version: str
    map_id: int
    game_mode: str
    participants: typing.List[ParticipantDto]