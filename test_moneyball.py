import pandas as pd
import moneyball


def test_key_with_max_value():
    hardware_store = {'shovel': 5, 'hammer': 2, 'screwdriver': 1, 'saw': 8}
    assert moneyball.key_with_max_value(hardware_store) == 'saw'


def test_find_position():
    data_frame = pd.DataFrame({'yearID': [2015, 2015, 2015],
                               'teamID': ['LAA', 'LAD', 'OAK'],
                               'playerID': ['Player1', 'Player2', 'Player3'],
                               'G_p': [25, 18, 12],
                               'G_c': [5, 10, 2],
                               'G_1b': [0, 43, 10],
                               'G_2b': [2, 3, 0],
                               'G_3b': [6, 2, 0],
                               'G_ss': [0, 1, 39],
                               'G_lf': [2, 2, 2],
                               'G_cf': [0, 0, 0],
                               'G_rf': [0, 0, 8],
                               'G_of': [0, 4, 2],
                               'G_dh': [0, 0, 0]})

    desired_result = ['pitcher', 'first_base', 'short_stop']
    assert moneyball.find_position(data_frame) == desired_result


def test_on_base_percentage():
    assert moneyball.on_base_percentage(1, 1, 1, 2, 2) == .5
