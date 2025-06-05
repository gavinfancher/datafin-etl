from dagster import job, op, schedule, ScheduleEvaluationContext, Definitions

from datafin import FMPClient

fmp = FMPClient("370b0e6c12a3eb14463c34c6277abec3")


@op
def get_quote():
    q = fmp.get_quote("AAPL")
    return q

@op
def print_quote(arg):
    print(arg)

@job
def do_stuff():
    get_quote()

@schedule(
    job=do_stuff,
    cron_schedule="* * * * *"
)
def do_stuff_schedule(context: ScheduleEvaluationContext):
    return {}


# defs = Definitions(
#     jobs=[do_stuff],
#     schedules=[do_stuff_schedule]
# )