from apscheduler.schedulers.blocking import BlockingScheduler
import logging
from datetime import datetime

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('log.txt')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

def clearMessage():
    with open('log.txt', 'w') as f:
        f.truncate(0)
    # logger.info("Log data has been cleared successfully!")
    print("Log data has been cleared successfully!")

def log2txt(msg):
    logger.info("Log data {} has been logged successfully!".format(msg))

scheduler = BlockingScheduler()

msg="test log"
scheduler.add_job(log2txt, 'interval', seconds=5, args=[msg])
scheduler.add_job(clearMessage, 'interval', seconds=30)

try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass


scheduler.shutdown(wait=False)
###