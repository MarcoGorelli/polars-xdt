from datetime import date, datetime

import holidays
import polars as pl
import polars_business


uk_holidays = holidays.country_holidays("UK", years=[2023, 2024])
df = pl.DataFrame(
    {"date": [datetime(2023, 4, 3, 6), datetime(2023, 9, 1, 1), datetime(2024, 1, 4, 2)]}
)
result = df.with_columns(
    date_plus_5_business_days=pl.col("date").dt.cast_time_unit('ns').dt.replace_time_zone('Asia/Kathmandu').business.advance_n_days(n=5),
)
print(result)

df = pl.DataFrame(
    {"date": [date(2023, 4, 3), date(2023, 9, 1), date(2024, 1, 4)]}
)

result = df.with_columns(
    date_plus_5_business_days=pl.col("date").business.advance_n_days(
        n=5, #holidays=uk_holidays
    )
)
print(result)