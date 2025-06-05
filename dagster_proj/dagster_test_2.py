from dagster import job, op, schedule, ScheduleEvaluationContext, Definitions

from datafin import FMPClient

fmp = FMPClient("370b0e6c12a3eb14463c34c6277abec3")


@op
def get_quote_2():
    q = fmp.get_quote("AAPL")
    return q

@op
def print_quote_2(arg):
    print(arg)

@job
def do_stuff_2():
    get_quote_2()

@schedule(
    job=do_stuff_2,
    cron_schedule="* * * * *"
)
def do_stuff_schedule_2(context: ScheduleEvaluationContext):
    return {}


# defs = Definitions(
#     jobs=[do_stuff_2],
#     schedules=[do_stuff_schedule_2]
# )