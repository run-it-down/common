import dataclasses
import json
import os
import psycopg2
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
    cur = conn.cursor()
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
        timeline_id=participant[4],
        stat_id=participant[5],
        team_id=participant[6],
        spell1_id=participant[7],
        spell2_id=participant[8],
        role=participant[9],
        lane=participant[10]
    )
