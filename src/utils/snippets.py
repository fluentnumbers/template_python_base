from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from typing import List
from typing import Union

import numpy as np
import pandas as pd
import yaml
from nptyping import NDArray
from nptyping.shape import Shape


np1d = NDArray[Shape["*"], Any]


def get_src_dir() -> Path:
    """Returns your ../hf-decompensation/src directory"""
    return Path(Path(__file__).absolute().parent.parent)


def get_config(yaml_file: Path = Path(get_src_dir().parent, "config.yaml")) -> dict:
    r"""
    Process yaml config.
    ! If this fails, make sure your working directory is hf-decompensation\src or
    provide the yaml_file argument explicitly
    """
    with open(yaml_file) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config


def detect_binary_changes(binary_vec: np1d, ts: np1d) -> (np1d, np1d):
    r"""
    Detect steps in a binary vector from False to True and vice-versa
    :param binary_vec: 1D boolean np.array
    :param ts: 1D timestamps np.array
    :return: (ts0, ts1) for begin\end of binary switches
    """
    # TODO: assert only 0 and 1 in binary_vec
    ts0, ts1 = [], []
    vec_diff = np.where(np.diff(binary_vec))[0]  # change happens AFTER each idx in vec_diff
    if binary_vec[0] is False:  # first value is False
        ts0 = ts[vec_diff[::2] + 1]
        if binary_vec[-1] is True:
            ts1 = ts[list(vec_diff[1::2] + 1) + [len(binary_vec) - 1]]
        else:
            ts1 = ts[vec_diff[1::2] + 1]
    elif binary_vec[0] is True:
        ts0 = ts[[0] + list(vec_diff[1::2] + 1)]
        if binary_vec[-1] is True:
            ts1 = ts[list(vec_diff[::2] + 1) + [len(binary_vec) - 1]]
        else:
            ts1 = ts[vec_diff[::2] + 1]
    return ts0, ts1


def move_column(df: pd.DataFrame, cols: list[str], mode: str = "first") -> pd.DataFrame:
    """
    Change order of several DF columns at once
    """
    cols.reverse()
    for c in cols:
        temp_cols = df.columns.tolist()
        if c not in temp_cols:
            continue
        else:
            index = df.columns.get_loc(c)
            new_cols = temp_cols
            if mode in ["first", "f"]:
                new_cols = (
                    temp_cols[index : index + 1] + temp_cols[0:index] + temp_cols[index + 1 :]
                )
            elif mode in ["last", "l"]:
                new_cols = (
                    temp_cols[0:index] + temp_cols[index + 1 :] + temp_cols[index : index + 1]
                )
            df = df[new_cols]
    return df


def str2datetime(datestr: str, timestr: str):
    date = datetime.strptime(datestr, "%m-%d-%Y")
    time = datetime.strptime(timestr, "%H:%M:%S")
    ts = datetime(
        date.year,
        date.month,
        date.day,
        time.hour,
        time.minute,
        time.second,
    )
    return ts


def generate_foldername(
    top_folder: Path | str,
    postfix_label: str = "",
    safe_create: bool = True,
) -> Path:
    date_time = datetime.now().strftime("%Y%m%d_%H_%M_%S")
    if postfix_label == "":
        p = Path(top_folder, date_time)
    else:
        p = Path(top_folder, date_time + "_" + postfix_label)
    if safe_create:
        p.mkdir(parents=True, exist_ok=True)
    return p


def round_up_to_odd(f: float) -> int:
    return int(np.ceil(f) // 2 * 2 + 1)
