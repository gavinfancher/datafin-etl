from dagster import Definitions

from .dagster_test_1 import do_stuff, do_stuff_schedule
from .dagster_test_2 import do_stuff_2, do_stuff_schedule_2
from .get_polygon_day_aggs import run_daily_agg, daily_agg_schedule

defs = Definitions(
    jobs=[do_stuff,do_stuff_2, run_daily_agg],
    schedules=[do_stuff_schedule,do_stuff_schedule_2, daily_agg_schedule]
)