import dataclasses
import json
import os
import psycopg2
import psycopg2.extras
import typing

import model


# database general
#####################################################################################################
#####################################################################################################
#####################################################################################################


def get_connection(
        database=os.getenv('DB'),
        user=os.getenv('DBUSER'),
        password=os.getenv('DBPASSWD'),
        host=os.getenv('DBHOST'),
        port=int(os.getenv('DBPORT')),
):
    """
    Returns database connection, if not specified configuration is taken from environment.
    :param database:
    :param user:
    :param password:
    :param host:
    :param port:
    :return:
    """
    return psycopg2.connect(
        database=database,
        user=user,
        password=password,
        host=host,
        port=port,
    )


def kill_connection(conn):
    """
    Closes given connection.
    :param conn:
    :return:
    """
    try:
        conn.close()
    except psycopg2.Error:
        pass


def _execute(
    conn,
    statement: str,
    values: tuple,
    print_exception: bool = True,
):
    """
    Executes given prepared statement (with given values) on specified connection, therefore a cursor
    is created. In case of failure a rollback is executed and committed. Occurred error are printable,
    default is true.
    :param conn:
    :param statement:
    :param values:
    :param print_exception:
    :return:
    """
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute(statement, values)
    except psycopg2.Error as e:
        if print_exception:
            print(e)
        cur.execute("rollback")
        conn.commit()
    return cur


def _set_timestamp(target):
    """
    Sets target's field "timestamp" to "now()" so if inserted to database the timestamp function
    from postgres is used.
    :param target:
    :return:
    """
    # necessary since we have to differentiate between timestamp on runtime and timestamp in database
    target.timestamp = 'now()'
    return target


# insert statements
#####################################################################################################
#####################################################################################################
#####################################################################################################


def insert_summoner(conn,
                    summoner: model.Summoner,
                    ):
    statement = "INSERT INTO summoners " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    summoner = _set_timestamp(summoner)
    values = dataclasses.astuple(summoner)

    _execute(
        conn=conn,
        statement=statement,
        values=values,
        print_exception=False,
    )

    conn.commit()


def insert_match(conn,
                 match: model.Match,
                 ):
    statement = "INSERT INTO matches " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = dataclasses.astuple(match)

    _execute(
        conn=conn,
        statement=statement,
        values=values,
        print_exception=True,
    )

    conn.commit()


def insert_summoner_match(conn,
                          summoner_match: model.SummonerMatch
                          ):
    statement = "INSERT INTO summoner_matches " \
                "VALUES (%s, %s)"
    values = dataclasses.astuple(summoner_match)
    _execute(
        conn=conn,
        statement=statement,
        values=values,
        print_exception=True,
    )

    conn.commit()


def insert_team(conn,
                team: model.Team
                ):
    statement = "INSERT INTO teams " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = dataclasses.astuple(team)

    _execute(
        conn=conn,
        statement=statement,
        values=values,
        print_exception=True,
    )

    conn.commit()


def insert_champion(conn,
                    champion: model.Champion
                    ):
    statement = "INSERT INTO champions " \
                "VALUES (%s, %s, %s)"

    values = dataclasses.astuple(champion)

    _execute(
        conn=conn,
        statement=statement,
        values=values,
        print_exception=True,
    )

    conn.commit()


def select_champion_name_id(
    conn,
    champ_id: str,
):
    statement = 'SELECT * FROM champions WHERE championid = %s'
    cur = _execute(
        conn=conn,
        statement=statement,
        values=(champ_id,)
    )
    return cur.fetchone()


def insert_timeline(conn,
                    timeline: model.Timeline
                    ):
    statement = "INSERT INTO timelines " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
        timeline.timeline_id,
        json.dumps(timeline.creeps_per_min_deltas),
        json.dumps(timeline.xp_per_min_deltas),
        json.dumps(timeline.gold_per_min_deltas),
        json.dumps(timeline.cs_diff_per_min_deltas),
        json.dumps(timeline.xp_diff_per_min_deltas),
        json.dumps(timeline.damage_taken_per_min_deltas),
        json.dumps(timeline.damage_taken_diff_per_min_deltas)
    )

    _execute(
        conn=conn,
        statement=statement,
        values=values,
        print_exception=True,
    )

    conn.commit()


def insert_stat(conn,
                stat: model.Stat
                ):
    statement = "INSERT INTO stats " \
                "VALUES (" \
                "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = dataclasses.astuple(stat)
    _execute(
        conn=conn,
        statement=statement,
        values=values,
        print_exception=True,
    )

    conn.commit()


def insert_participant(conn,
                       participant: model.Participant
                       ):
    statement = "INSERT INTO participants " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = dataclasses.astuple(participant)
    print(values)

    _execute(
        conn=conn,
        statement=statement,
        values=values,
        print_exception=True,
    )

    conn.commit()


def insert_event(conn, event: model.Event):
    statement = "INSERT INTO events " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = dataclasses.astuple(event)

    _execute(
        conn=conn,
        statement=statement,
        values=values,
        print_exception=True,
    )

    conn.commit()


def insert_participant_frame(conn, participant_frame: model.ParticipantFrame):
    statement = "INSERT INTO participant_frame " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = dataclasses.astuple(participant_frame)

    _execute(
        conn=conn,
        statement=statement,
        values=values,
        print_exception=True,
    )

    conn.commit()

# select statements
#####################################################################################################
#####################################################################################################
#####################################################################################################


def select_count_summoner_match(conn,
                                account_id: str,
                                ):
    statement = "SELECT COUNT(*) FROM summoner_matches " \
                "WHERE accountid = %s"
    values = (account_id,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values,
    )

    conn.commit()
    return cur.fetchone()[0]


def select_summoner(conn,
                    summoner_name: str,
                    ):
    statement = "SELECT * FROM summoners " \
                "WHERE name = %s"
    values = (summoner_name,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values,
    )

    conn.commit()
    res = cur.fetchone()

    return model.Summoner(
        account_id=res[0],
        summoner_id=res[1],
        puuid=res[2],
        name=res[3],
        summoner_level=res[4],
        profile_icon_id=res[5],
        revision_date=res[6],
        timestamp=res[7]
    )


def select_stat_from_participant(conn,
                                 summoner: model.Summoner,
                                 ):
    statement = "SELECT statid FROM participants " \
                "WHERE accountid = %s"
    values = (summoner.account_id,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values,
    )

    return cur.fetchall()


def select_stats(conn,
                 statid: str,
                 ):
    statement = "SELECT * FROM stats " \
                "WHERE statid = %s"
    values = (statid,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values,
    )

    stat_raw = cur.fetchone()

    return model.Stat(
        stat_id=stat_raw[0],
        win=stat_raw[1],
        items=stat_raw[2],
        kills=stat_raw[3],
        deaths=stat_raw[4],
        assists=stat_raw[5],
        largest_killing_spree=stat_raw[6],
        largest_multi_kill=stat_raw[7],
        killing_sprees=stat_raw[8],
        longest_time_spent_living=stat_raw[9],
        double_kills=stat_raw[10],
        triple_kills=stat_raw[11],
        quadra_kills=stat_raw[12],
        penta_kills=stat_raw[13],
        total_damage_dealt=stat_raw[14],
        magic_damage_dealt=stat_raw[15],
        physical_damage_dealt=stat_raw[16],
        true_damage_dealt=stat_raw[17],
        largest_critical_strike=stat_raw[18],
        total_damage_dealt_to_champions=stat_raw[19],
        magic_damage_dealt_to_champions=stat_raw[20],
        physical_damage_dealt_to_champions=stat_raw[21],
        true_damage_dealt_to_champions=stat_raw[22],
        total_heal=stat_raw[23],
        total_units_healed=stat_raw[24],
        damage_self_mitigated=stat_raw[25],
        damage_dealt_to_objectives=stat_raw[26],
        damage_dealt_to_turrets=stat_raw[27],
        vision_score=stat_raw[28],
        time_ccing_others=stat_raw[29],
        total_damage_taken=stat_raw[30],
        magical_damage_taken=stat_raw[31],
        physical_damage_taken=stat_raw[32],
        true_damage_taken=stat_raw[33],
        gold_earned=stat_raw[34],
        gold_spent=stat_raw[35],
        turret_kills=stat_raw[36],
        inhibitor_kills=stat_raw[37],
        total_minions_killed=stat_raw[38],
        neutral_minions_killed_team_jungle=stat_raw[39],
        neutral_minions_killed_enemy_jungle=stat_raw[40],
        total_time_crowd_control_dealt=stat_raw[41],
        champ_level=stat_raw[42],
        vision_wards_bought_in_game=stat_raw[43],
        sight_wards_bought_in_game=stat_raw[44],
        wards_placed=stat_raw[45],
        wards_killed=stat_raw[46],
        first_blood_kill=stat_raw[47],
        first_blood_assist=stat_raw[48],
        first_tower_kill=stat_raw[49],
        first_tower_assist=stat_raw[50],
        first_inhibitor_kill=stat_raw[51],
        first_inhibitor_assist=stat_raw[52],
        combat_player_score=stat_raw[53],
        objective_player_score=stat_raw[54],
        total_player_score=stat_raw[55],
        total_score_rank=stat_raw[56],
        perk0=stat_raw[57],
        perk0_var1=stat_raw[58],
        perk0_var2=stat_raw[59],
        perk0_var3=stat_raw[60],
        perk1=stat_raw[61],
        perk1_var1=stat_raw[62],
        perk1_var2=stat_raw[63],
        perk1_var3=stat_raw[64],
        perk2=stat_raw[65],
        perk2_var1=stat_raw[66],
        perk2_var2=stat_raw[67],
        perk2_var3=stat_raw[68],
        perk3=stat_raw[69],
        perk3_var1=stat_raw[70],
        perk3_var2=stat_raw[71],
        perk3_var3=stat_raw[72],
        perk4=stat_raw[73],
        perk4_var1=stat_raw[74],
        perk4_var2=stat_raw[75],
        perk4_var3=stat_raw[76],
        perk5=stat_raw[77],
        perk5_var1=stat_raw[78],
        perk5_var2=stat_raw[79],
        perk5_var3=stat_raw[80],
        perk_primary_style=stat_raw[81],
        perk_sub_style=stat_raw[82],
        stat_perk0=stat_raw[83],
        stat_perk1=stat_raw[84],
        stat_perk2=stat_raw[85],
    )


def select_participant_from_stat(conn, stat: model.Stat):
    statement = "SELECT * FROM participants " \
                "WHERE statid = %s"
    values = (stat.stat_id,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values,
    )

    participant = cur.fetchone()
    return model.Participant(
        participant_id=participant[0],
        game_id=participant[1],
        account_id=participant[2],
        champion_id=participant[3],
        stat_id=participant[4],
        timeline_id=participant[5],
        spell1_id=participant[6],
        spell2_id=participant[7],
        role=participant[8],
        lane=participant[9]
    )


def select_common_games(conn, s1: model.Summoner, s2: model.Summoner):
    statement = "SELECT DISTINCT s1.gameid, s1.accountid s1_accountid, p1.participantid s1_participantid, " \
                "p1.statid s1_statid, p1.teamid s1_teamid, s2.accountid s2_accountid, p2.participantid s2_participantid, " \
                "p2.statid s2_statid, p2.teamid s2_teamid, p1.role s1_role, p1.lane s1_lane, " \
                "p2.role s2_role, p2.lane s2_lane, t.win from summoner_matches s1 " \
                "JOIN summoner_matches s2 ON s1.gameid = s2.gameid " \
                "JOIN participants p1 ON p1.accountid = s1.accountid AND p1.gameid = s1.gameid " \
                "JOIN participants p2 ON p2.accountid = s2.accountid AND p2.gameid = s2.gameid " \
                "JOIN teams t ON t.teamid = p1.teamid AND t.gameid = s1.gameid " \
                "WHERE s1.accountid = %s AND s2.accountid = %s AND p1.teamid = p2.teamid"
    values = (s1.account_id, s2.account_id)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values,
    )

    return cur.fetchall()


def select_participant(conn, participant_id: str):
    statement = "SELECT * FROM participants p WHERE p.participantid = %s"
    values = (participant_id,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values
    )
    participant = cur.fetchone()

    return model.Participant(
        participant_id=participant["participantid"],
        game_id=participant["gameid"],
        account_id=participant["accountid"],
        champion_id=participant["championid"],
        stat_id=participant["statid"],
        team_id=participant["teamid"],
        timeline_id=participant["timelineid"],
        spell1_id=participant["spell1id"],
        spell2_id=participant["spell2id"],
        role=participant["role"],
        lane=participant["lane"]
    )


def select_participant_frames(conn, participant_id: str):
    statement = "SELECT * FROM participant_frame p WHERE p.participantid = %s"
    values = (participant_id,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values
    )

    return cur.fetchall()

def select_participant_gold(conn, participant_id: str):
    statement = "SELECT totalgold FROM participant_frame p WHERE p.participantid = %s"
    values = (participant_id,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values
    )

    return cur.fetchall()


def select_opponent(conn, participant_id: str, game_id: str, position: (str, str)) -> model.Participant:
    statement = "SELECT * FROM participants p WHERE p.gameid = %s AND p.lane = %s AND p.role = %s AND p.participantid <> %s"
    values = (game_id, position[0], position[1], participant_id)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values
    )

    opponent = cur.fetchone()

    if opponent is None:
        return None
    return model.Participant(
        participant_id=opponent["participantid"],
        game_id=opponent["gameid"],
        account_id=opponent["accountid"],
        champion_id=opponent["championid"],
        stat_id=opponent["statid"],
        team_id=opponent["teamid"],
        timeline_id=opponent["timelineid"],
        spell1_id=opponent["spell1id"],
        spell2_id=opponent["spell2id"],
        role=opponent["role"],
        lane=opponent["lane"]
    )


def select_positions(conn, participant_id: str):
    statement = "SELECT p.position FROM participant_frame p WHERE p.participantid = %s"
    values = (participant_id,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values
    )

    return cur.fetchall()

def select_overall_kill_information(conn, game_id: str, team_id: int):
    statement = "SELECT SUM(s.kills) kills, SUM(s.deaths) deaths, SUM(s.assists) assists FROM stats s " \
                "JOIN participants p ON p.statid = s.statid " \
                "WHERE p.gameid = %s AND p.teamid = %s"
    values = (game_id, team_id,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values
    )

    return cur.fetchone()


def select_game_events(conn, game_id: str):
    statement = "SELECT * FROM events e  WHERE e.participantid = %s"
    values = (participant_id,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values
    )

    return cur.fetchall()


def select_kill_timeline(conn, game_id: str, team_id: int):
    statement = "SELECT p.participantid, e.timestamp, e.position, e.killerid killer, e.victimid victim, p.teamid, " \
                "e.assistingparticipantids FROM events e " \
                "JOIN participants p ON e.participantid = p.participantid " \
                "WHERE p.gameid = %s AND type = 'CHAMPION_KILL' AND p.teamid = %s" \
                "ORDER BY e.timestamp"
    values = (game_id, team_id,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values
    )

    return cur.fetchall()

def select_all_kill_timeline(conn, game_id: str):
    statement = "SELECT p.participantid, e.timestamp, e.position, e.killerid killer, e.victimid victim, p.teamid, " \
                "e.assistingparticipantids FROM events e " \
                "JOIN participants p ON e.participantid = p.participantid " \
                "WHERE p.gameid = %s AND type = 'CHAMPION_KILL'" \
                "ORDER BY e.timestamp"
    values = (game_id,)

    cur = _execute(
        conn=conn,
        statement=statement,
        values=values
    )

    return cur.fetchall()

def select_all_participants(conn):
    statement = "SELECT * FROM stats s JOIN participants p ON s.statid = p.statid"

    cur = _execute(
        conn=conn,
        statement=statement,
        values=()
    )

    return cur.fetchall()

def select_all_games(conn):
    statement = "SELECT DISTINCT s1.gameid, s1.accountid s1_accountid, p1.participantid s1_participantid, " \
                "p1.statid s1_statid, p1.teamid s1_teamid, p1.role s1_role, p1.lane s1_lane, t.win from summoner_matches s1 " \
                "JOIN participants p1 ON p1.accountid = s1.accountid AND p1.gameid = s1.gameid " \
                "JOIN teams t ON t.teamid = p1.teamid AND t.gameid = s1.gameid"
    cur = _execute(
        conn=conn,
        statement=statement,
        values=()
    )

    return cur.fetchall()

def select_game_frames(conn, game_id:str):
    statement = "SELECT * FROM participant_frame f " \
                "JOIN participants p ON p.participantid = f.participantid " \
                "WHERE p.gameid = %s " \
                "ORDER BY f.timestamp"
    cur = _execute(
        conn=conn,
        statement=statement,
        values=(game_id,)
    )

    return cur.fetchall()


def select_common_game_stats(conn, s1: model.Summoner, s2: model.Summoner):
    statement = "SELECT DISTINCT s1.gameid, st1.kills s1_kills, st1.deaths s1_deaths, " \
                "st1.assists s1_assists, st1.totalminionskilled s1_totalminionskilled, p1.role s1_role, p1.lane s1_lane, " \
                "st2.kills s2_kills, st2.deaths s2_deaths, st2.assists s2_assists, st2.totalminionskilled s2_totalminionskilled, " \
                "p2.role s2_role, p2.lane s2_lane, t.win, p1.championid s1_champion, p2.championid s2_champion from summoner_matches s1 " \
                "JOIN summoner_matches s2 ON s1.gameid = s2.gameid " \
                "JOIN participants p1 ON p1.accountid = s1.accountid AND p1.gameid = s1.gameid " \
                "JOIN participants p2 ON p2.accountid = s2.accountid AND p2.gameid = s2.gameid " \
                "JOIN teams t ON t.teamid = p1.teamid AND t.gameid = s1.gameid " \
                "JOIN stats st1 ON st1.statid = p1.statid " \
                "JOIN stats st2 ON st2.statid = p2.statid " \
                "WHERE s1.accountid = %s AND s2.accountid = %s AND p1.teamid = p2.teamid"
    cur = _execute(
        conn=conn,
        statement=statement,
        values=(s1.account_id, s2.account_id,)
    )

    return cur.fetchall()


def select_team_gold(conn, game_id: str, team_id):
    statement = "SELECT SUM(s.goldearned) gold FROM stats s " \
                "JOIN participants p ON p.statid = s.statid " \
                "WHERE p.gameid = %s and p.teamid = %s"
    cur = _execute(
        conn=conn,
        statement=statement,
        values=(game_id, team_id,)
    )
    return cur.fetchall()


def select_all_summoners(conn):
    statement = "SELECT * FROM summoners"
    cur = _execute(
        conn=conn,
        statement=statement,
        values=()
    )
    return cur.fetchall()


def select_summoner_games(conn, account_id: str):
    statement = "SELECT s.accountid, p.gameid, t.win FROM participants p " \
                "JOIN summoners s ON s.accountid = p.accountid " \
                "JOIN teams t ON t.teamid = p.teamid and t.gameid = p.gameid " \
                "WHERE s.accountid = %s"
    cur = _execute(
        conn=conn,
        statement=statement,
        values=(account_id,)
    )
    return cur.fetchall()


def select_team_cs(conn, game_id: str, team_id):
    statement = "SELECT SUM(s.totalminionskilled + s.neutralminionskilledteamjungle + s.neutralminionskilledenemyjungle) cs FROM stats s " \
                "JOIN participants p ON p.statid = s.statid " \
                "WHERE p.gameid = %s and p.teamid = %s"
    cur = _execute(
        conn=conn,
        statement=statement,
        values=(game_id, team_id,)
    )
    return cur.fetchall()


def select_participant_team(conn, participant_id: str):
    statement = "SELECT * FROM participants p WHERE p.participantid = %s"
    cur = _execute(
        conn=conn,
        statement=statement,
        values=(participant_id,)
    )
    return cur.fetchall()


def select_objectives(conn, game_id: str):
    statement = "SELECT * FROM events e " \
                "JOIN participants p ON p.participantid = e.participantid " \
                "WHERE p.gameid = %s and (e.type = 'BUILDING_KILL' or e.type = 'ELITE_MONSTER_KILL')"
    cur = _execute(
        conn=conn,
        statement=statement,
        values=(game_id,)
    )
    return cur.fetchall()


def select_participantid_from_game_and_account(
    conn,
    game_id: str,
    account_id: str,
):
    statement = "SELECT * FROM participants p WHERE p.gameid = %s AND p.accountid = %s"
    cur = _execute(
        conn=conn,
        statement=statement,
        values=(game_id, account_id)
    )
    return cur.fetchone()[0]


def select_teamid_from_game_and_account(
    conn,
    game_id: str,
    account_id: str,
):
    statement = "SELECT * FROM participants p WHERE p.gameid = %s AND p.accountid = %s"
    cur = _execute(
        conn=conn,
        statement=statement,
        values=(game_id, account_id)
    )
    return cur.fetchone()[5]


def select_team_from_teamid_and_gameid(
    conn,
    game_id: str,
    team_id: str,
):
    statement = 'SELECT * FROM teams WHERE gameid = %s and teamid = %s'
    cur = _execute(
        conn=conn,
        statement=statement,
        values=(game_id, team_id)
    )
    return cur.fetchone()


def select_accountid_in_game(
    conn,
    account_id: str,
    game_id: str,
):
    statement = 'SELECT * FROM participants WHERE gameid = %s and accountid = %s'
    cur = _execute(
        conn=conn,
        statement=statement,
        values=(game_id, account_id)
    )
    return cur.fetchone()
