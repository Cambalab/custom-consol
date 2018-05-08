from apscheduler.schedulers.blocking import BlockingScheduler
import main

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=13)
def scheduled_job():
    main.update_products()

sched.start()
