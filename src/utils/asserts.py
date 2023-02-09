from typing import Any
from typing import Dict
from typing import Iterable
from typing import List
from typing import Union

import numpy as np
from pandas import DataFrame


def assert_all_columns_in_df(df: DataFrame, columns: List[str]):
    for c in columns:
        assert (
            c in df.columns
        ), f"Asserting {columns} are in DataFrame.columns: {c} not in {df.columns}"


def assert_all_keys_in_dict(d: Dict[Any, Any], keys: Iterable[Any]):
    for c in keys:
        assert c in d.keys(), f"Asserting {keys} are in Dict.keys: {c} not in {d.keys()}"


def assert_columns_present(df: DataFrame, cols: List[str], label: str = ""):
    assert all([c in df for c in cols]), f"{label} Input dataframe should contain columns {cols}"


def assert_shape_equal(this: Union[list, np.ndarray], other: Union[list, np.ndarray]):
    assert this.shape == other.shape, "Shape of compared objects is not the same"


def assert_strictly_increasing(ts: np.ndarray):
    assert all(x < y for x, y in zip(ts, ts[1:])), "Timestamps values should be strictly increasing"


def assert_sampling_rate_from_ts(ts: np.ndarray, fs: int):
    fs_from_ts = np.mean(1.0 / np.diff(ts))
    assert (
        abs(fs - fs_from_ts) < 1
    ), f"Expected fs={fs} is different from timestamps-derived fs={fs_from_ts}"


def assert_sampling_rate_constant(ts: np.ndarray, tol: float = 1e-6):
    max_fs = np.max(np.diff(ts))
    min_fs = np.min(np.diff(ts))
    assert (
        abs(max_fs - min_fs) < tol
    ), f"Max fs {max_fs} - min fs {min_fs} is above the tolerance {tol}"


def assert_data_type(data, dtype: type):
    data = np.asarray(list(data))
    assert data.dtype == dtype, (
        f"Data to be filtered must be {dtype},\r\n" "Current data type is {data.dtype}"
    )
    return data
