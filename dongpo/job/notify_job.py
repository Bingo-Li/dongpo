import schedule
import datetime
from dongpo import config, manager


def print_time():
    print(datetime.datetime.now())


# 创建一个按3秒间隔执行任务
schedule.every(3).seconds.do(print_time)

# 我的定时任务
schedule.every().day.at("12:00").do(manager.query_house_info, config.v0_config_init())
schedule.every().sunday.at("08:00").do(manager.query_house_info, config.v1_config_init())
schedule.every().sunday.at("09:00").do(manager.query_house_info, config.v2_config_init())

# 客户的任务
schedule.every().day.at("10:00").do(manager.query_house_info, config.shell_config_init())

# while True:
#     schedule.run_pending()
