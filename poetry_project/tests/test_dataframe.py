from plt_temp import create_dataframe


def test_create_dataframe_sorts_and_preserves_temperatures():
    hours = [
        "2026-01-01T03:00",
        "2026-01-01T01:00",
        "2026-01-01T02:00",
    ]
    temperatures = [3.5, 1.5, 2.5]

    df = create_dataframe(hours, temperatures)

    assert list(df.columns) == ["time", "temperature_c"]
    assert len(df) == 3
    assert df["time"].dt.strftime("%H:%M").tolist() == [
        "01:00",
        "02:00",
        "03:00",
    ]
    assert df["temperature_c"].tolist() == [1.5, 2.5, 3.5]
