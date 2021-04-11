from datetime import datetime
import typing
from uuid import uuid4

import model
from dtos import summoner
from dtos import match
from dtos import matchlist
from dtos import match_timeline


def parse_summoner(summoner_dto: summoner.SummonerDto
                   ) -> model.Summoner:
    return model.Summoner(
        account_id=summoner_dto.account_id,
        summoner_id=summoner_dto.id,
        puuid=summoner_dto.puuid,
        name=summoner_dto.name,
        summoner_level=summoner_dto.summoner_level,
        profile_icon_id=summoner_dto.profile_icon_id,
        revision_date=summoner_dto.revision_date,
        timestamp=str(datetime.now()),
    )


def parse_match(match_dto: match.MatchDto
                ) -> model.Match:
    return model.Match(
        game_id=match_dto.game_id,
        platform_id=match_dto.platform_id,
        game_creation=match_dto.game_creation,
        game_duration=match_dto.game_duration,
        queue_id=match_dto.queue_id,
        map_id=match_dto.map_id,
        season_id=match_dto.season_id,
        game_version=match_dto.game_version,
        game_mode=match_dto.game_mode,
        game_type=match_dto.game_type
    )


def parse_summoner_matches(matchlist_dto: matchlist.MatchlistDto,
                           account_id: str,
                           ) -> typing.List[model.SummonerMatch]:
    matches = []
    for match in matchlist_dto.matches:
        matches.append(model.SummonerMatch(
            account_id=account_id,
            game_id=match.game_id,
        ))
    return matches


def parse_teams(match: match.MatchDto,
                ) -> typing.List[model.Team]:
    teams = []
    for team in match.teams:
        ban_ids = []
        for ban in team.bans:
            ban_ids.append(ban.champion_id)
        teams.append(model.Team(
            team_id=team.team_id,
            game_id=match.game_id,
            win=team.win,
            first_blood=team.first_blood,
            first_tower=team.first_tower,
            first_inhibitor=team.first_inhibitor,
            first_baron=team.first_baron,
            first_dragon=team.first_dragon,
            first_rift_herald=team.first_rift_herald,
            tower_kills=team.tower_kills,
            inhibitor_kills=team.inhibitor_kills,
            baron_kills=team.baron_kills,
            dragon_kills=team.dragon_kills,
            rift_herald_kills=team.rift_herald_kills,
            bans=ban_ids,
        ))
    return teams


def parse_team(team_dto: match.TeamStatsDto,
               game_id: int) -> model.Team:
    return model.Team(
        team_id=team_dto.team_id,
        game_id=game_id,
        win=team_dto.win,
        first_blood=team_dto.first_blood,
        first_tower=team_dto.first_tower,
        first_inhibitor=team_dto.first_inhibitor,
        first_baron=team_dto.first_baron,
        first_dragon=team_dto.first_dragon,
        first_rift_herald=team_dto.first_rift_herald,
        tower_kills=team_dto.tower_kills,
        inhibitor_kills=team_dto.inhibitor_kills,
        baron_kills=team_dto.baron_kills,
        dragon_kills=team_dto.dragon_kills,
        rift_herald_kills=team_dto.rift_herald_kills,
        bans=[ban.champion_id for ban in team_dto.bans],
    )


def parse_timelines(match: match.MatchDto,
                    ) -> typing.List[model.Timeline]:
    timelines = []
    for participant in match.participants:
        timelines.append(model.Timeline(
            timeline_id=str(uuid4()),
            creeps_per_min_deltas=participant.timeline.cs_diff_per_min_deltas,
            xp_per_min_deltas=participant.timeline.cs_diff_per_min_deltas,
            gold_per_min_deltas=participant.timeline.cs_diff_per_min_deltas,
            cs_diff_per_min_deltas=participant.timeline.cs_diff_per_min_deltas,
            xp_diff_per_min_deltas=participant.timeline.cs_diff_per_min_deltas,
            damage_taken_per_min_deltas=participant.timeline.cs_diff_per_min_deltas,
            damage_taken_diff_per_min_deltas=participant.timeline.cs_diff_per_min_deltas,
        ))

    return timelines


def parse_timeline(timeline_dto: match.ParticipantTimelineDto) -> model.Timeline:
    return model.Timeline(
        timeline_id=str(uuid4()),
        creeps_per_min_deltas=timeline_dto.cs_diff_per_min_deltas,
        xp_per_min_deltas=timeline_dto.cs_diff_per_min_deltas,
        gold_per_min_deltas=timeline_dto.cs_diff_per_min_deltas,
        cs_diff_per_min_deltas=timeline_dto.cs_diff_per_min_deltas,
        xp_diff_per_min_deltas=timeline_dto.cs_diff_per_min_deltas,
        damage_taken_per_min_deltas=timeline_dto.cs_diff_per_min_deltas,
        damage_taken_diff_per_min_deltas=timeline_dto.cs_diff_per_min_deltas,
    )


def parse_stats(stat: match.ParticipantStatsDto
                ) -> model.Stat:
    return (model.Stat(
        stat_id=str(uuid4()),
        win=stat.win,
        items=[stat.item0, stat.item1, stat.item2, stat.item3, stat.item4, stat.item5],
        kills=stat.kills,
        deaths=stat.deaths,
        assists=stat.assists,
        largest_killing_spree=stat.largest_killing_spree,
        largest_multi_kill=stat.largest_multi_kill,
        killing_sprees=stat.killing_sprees,
        longest_time_spent_living=stat.longest_time_spent_living,
        double_kills=stat.double_kills,
        triple_kills=stat.triple_kills,
        quadra_kills=stat.quadra_kills,
        penta_kills=stat.penta_kills,
        total_damage_dealt=stat.total_damage_dealt,
        magic_damage_dealt=stat.magic_damage_dealt,
        physical_damage_dealt=stat.physical_damage_dealt,
        true_damage_dealt=stat.true_damage_dealt,
        largest_critical_strike=stat.largest_critical_strike,
        total_damage_dealt_to_champions=stat.total_damage_dealt_to_champions,
        magic_damage_dealt_to_champions=stat.magic_damage_dealt_to_champions,
        physical_damage_dealt_to_champions=stat.physical_damage_dealt_to_champions,
        true_damage_dealt_to_champions=stat.true_damage_dealt_to_champions,
        total_heal=stat.total_heal,
        total_units_healed=stat.total_units_healed,
        damage_self_mitigated=stat.damage_self_mitigated,
        damage_dealt_to_objectives=stat.damage_dealt_to_objectives,
        damage_dealt_to_turrets=stat.damage_dealt_to_turrets,
        vision_score=stat.vision_score,
        time_ccing_others=stat.time_ccing_others,
        total_damage_taken=stat.total_damage_taken,
        magical_damage_taken=stat.magical_damage_taken,
        physical_damage_taken=stat.physical_damage_taken,
        true_damage_taken=stat.true_damage_taken,
        gold_earned=stat.gold_earned,
        gold_spent=stat.gold_spent,
        turret_kills=stat.turret_kills,
        inhibitor_kills=stat.inhibitor_kills,
        total_minions_killed=stat.total_minions_killed,
        neutral_minions_killed_team_jungle=stat.neutral_minions_killed_team_jungle,
        neutral_minions_killed_enemy_jungle=stat.neutral_minions_killed_enemy_jungle,
        total_time_crowd_control_dealt=stat.total_time_crowd_control_dealt,
        champ_level=stat.champ_level,
        vision_wards_bought_in_game=stat.vision_wards_bought_in_game,
        sight_wards_bought_in_game=stat.sight_wards_bought_in_game,
        wards_placed=stat.wards_placed,
        wards_killed=stat.wards_killed,
        first_blood_kill=stat.first_blood_kill,
        first_blood_assist=stat.first_blood_assist,
        first_tower_kill=stat.first_tower_kill,
        first_tower_assist=stat.first_tower_assist,
        first_inhibitor_kill=stat.first_inhibitor_kill,
        first_inhibitor_assist=stat.first_inhibitor_assist,
        combat_player_score=stat.combat_player_score,
        objective_player_score=stat.objective_player_score,
        total_player_score=stat.total_player_score,
        total_score_rank=stat.total_score_rank,
        perk0=stat.perk0,
        perk0_var1=stat.perk0_var1,
        perk0_var2=stat.perk0_var2,
        perk0_var3=stat.perk0_var3,
        perk1=stat.perk1,
        perk1_var1=stat.perk1_var1,
        perk1_var2=stat.perk1_var2,
        perk1_var3=stat.perk1_var3,
        perk2=stat.perk2,
        perk2_var1=stat.perk2_var1,
        perk2_var2=stat.perk2_var2,
        perk2_var3=stat.perk2_var3,
        perk3=stat.perk3,
        perk3_var1=stat.perk3_var1,
        perk3_var2=stat.perk3_var2,
        perk3_var3=stat.perk3_var3,
        perk4=stat.perk4,
        perk4_var1=stat.perk4_var1,
        perk4_var2=stat.perk4_var2,
        perk4_var3=stat.perk4_var3,
        perk5=stat.perk5,
        perk5_var1=stat.perk5_var1,
        perk5_var2=stat.perk5_var2,
        perk5_var3=stat.perk5_var3,
        perk_primary_style=stat.perk_primary_style,
        perk_sub_style=stat.perk_sub_style,
        stat_perk0=stat.stat_perk0,
        stat_perk1=stat.stat_perk1,
        stat_perk2=stat.stat_perk2,
    ))


def parse_participants(match_dto: match.MatchDto,
                       stat_ids: typing.Mapping[int, str],
                       timelines: typing.Mapping[int, str],
                       roles: typing.Mapping[int, str],
                       lanes: typing.Mapping[int, str],
                       ) -> typing.List[model.Participant]:
    participants = []
    for participant in match_dto.participants:

        # find corresponding participant identity
        identity = None
        for participant_identity in match_dto.participant_identities:
            if participant_identity.participant_id == participant.participant_id:
                identity = participant_identity

        participants.append(model.Participant(
            participant_id=str(uuid4()),
            game_id=match_dto.game_id,
            account_id=identity.player.account_id,
            champion_id=participant.champion_id,
            stat_id=stat_ids[participant.participant_id],
            team_id=identity.team_id,
            timeline_id=timelines[participant.participant_id],
            spell1_id=participant.spell1_id,
            spell2_id=participant.spell2_id,
            role=roles[participant.participant_id],
            lane=lanes[participant.participant_id],
        ))

    return participants


def parse_participant(participant_dto: match.ParticipantDto,
                      game_id: int,
                      account_id: str,
                      stat_id: str,
                      team_id: int,
                      timeline_id: str,
                      role: str,
                      lane: str
                      ) -> model.Participant:
    return model.Participant(
        participant_id=str(uuid4()),
        game_id=game_id,
        account_id=account_id,
        champion_id=participant_dto.champion_id,
        stat_id=stat_id,
        team_id=team_id,
        timeline_id=timeline_id,
        spell1_id=participant_dto.spell1_id,
        spell2_id=participant_dto.spell2_id,
        role=role,
        lane=lane
    )


def parse_match_timeline_frames(match_timeline: match_timeline.MatchTimelineDto,
                                mapping_participant_ids_to_match_participant_ids: typing.Mapping[int, str],
                                ) -> (typing.List[model.ParticipantFrame], typing.List[model.Event]):
    participant_frames = []
    events = []
    for frame in match_timeline.frames:
        for participant_frame_dto in frame.participant_frames.values():
            participant_frames.append(model.ParticipantFrame(
                participant_id=mapping_participant_ids_to_match_participant_ids[participant_frame_dto.participant_id],
                timestamp=frame.timestamp,
                minions_killed=participant_frame_dto.minions_killed,
                team_score=participant_frame_dto.team_score,
                total_gold=participant_frame_dto.total_gold,
                level=participant_frame_dto.level,
                xp=participant_frame_dto.xp,
                current_gold=participant_frame_dto.current_gold,
                position=({participant_frame_dto.position.x}, {participant_frame_dto.position.y}),
                jungle_minions_killed=participant_frame_dto.jungle_minions_killed,
            ))

        for event_dto in frame.events:
            assisting_participant_ids = []
            for assisting_participant_id in event_dto.assisting_participant_ids:
                assisting_participant_ids.append(
                    mapping_participant_ids_to_match_participant_ids[assisting_participant_id])

            events.append(model.Event(
                participant_id=mapping_participant_ids_to_match_participant_ids[event_dto.participant_id],
                timestamp=frame.timestamp,
                lane_type=event_dto.lane_type,
                skill_slot=event_dto.skill_slot,
                ascended_type=event_dto.ascended_type,
                creator_id=event_dto.creator_id,
                after_id=event_dto.after_id,
                event_type=event_dto.event_type,
                type=event_dto.type,
                level_up_type=event_dto.level_up_type,
                ward_type=event_dto.ward_type,
                tower_type=event_dto.tower_type,
                item_id=event_dto.item_id,
                before_id=event_dto.before_id,
                monster_type=event_dto.monster_type,
                monster_sub_type=event_dto.monster_sub_type,
                position=(event_dto.position.x, event_dto.item_id.y),
                killer_id=mapping_participant_ids_to_match_participant_ids[event_dto.killer_id],
                assisting_participant_ids=assisting_participant_ids,
                building_type=event_dto.building_type,
                victim_id=mapping_participant_ids_to_match_participant_ids[event_dto.victim_id],
            ))

    return participant_frames


def parse_event(
    event_dto: match_timeline.MatchEventDto,
    map: dict,
) -> model.Event:
    participant_id = event_dto.participant_id
    if participant_id is None:
        if event_dto.creator_id:
            participant_id = map[event_dto.creator_id]
        elif event_dto.killer_id:
            participant_id = map[event_dto.killer_id]
    else:
        participant_id = map[event_dto.participant_id]

    assisting_participant_ids = []
    if event_dto.assisting_participant_ids:
        for assisting_participant_id in event_dto.assisting_participant_ids:
            assisting_participant_ids.append(map[assisting_participant_id])

    return model.Event(
        participant_id=participant_id,
        timestamp=event_dto.timestamp,
        lane_type=event_dto.lane_type,
        skill_slot=event_dto.skill_slot,
        ascended_type=event_dto.ascended_type,
        creator_id=event_dto.creator_id,
        after_id=event_dto.after_id,
        event_type=event_dto.event_type,
        type=event_dto.type,
        level_up_type=event_dto.level_up_type,
        ward_type=event_dto.ward_type,
        tower_type=event_dto.tower_type,
        item_id=event_dto.item_id,
        before_id=event_dto.before_id,
        monster_type=event_dto.monster_type,
        monster_sub_type=event_dto.monster_sub_type,
        team_id=event_dto.team_id,
        position=f'{event_dto.position.x},{event_dto.position.y}' if event_dto.position else None,
        killer_id=map[event_dto.killer_id] if event_dto.killer_id else None,
        assisting_participant_ids=assisting_participant_ids,
        building_type=event_dto.building_type,
        victim_id=map[event_dto.victim_id] if event_dto.victim_id else None,
    )


def parse_participant_frame(participant_frame_dto: match_timeline.MatchParticipantFrameDto,
                            participant_id: str,
                            timestamp: int) -> model.ParticipantFrame:
    return model.ParticipantFrame(
        participant_id=participant_id,
        timestamp=timestamp,
        minions_killed=participant_frame_dto.minions_killed,
        team_score=participant_frame_dto.team_score,
        total_gold=participant_frame_dto.total_gold,
        level=participant_frame_dto.level,
        xp=participant_frame_dto.xp,
        current_gold=participant_frame_dto.current_gold,
        position=f'{participant_frame_dto.position.x},{participant_frame_dto.position.y}' if participant_frame_dto.position else None,
        jungle_minions_killed=participant_frame_dto.jungle_minions_killed,
    )
