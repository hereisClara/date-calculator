# from datetime import datetime
# user_date_str = input("請輸入日期（年/月/日）：")
# user_date_name = input("請輸入紀念日名稱：")
# user_date_story = input("在這一天發生了什麼事？")

# user_date = datetime.strptime(user_date_str, "%Y/%m/%d")
# today = datetime.today()
# delta_date = abs(today - user_date).days

# while not user_date_str.strip():
#   print("請重新輸入日期")
#   user_date_str = input("請輸入日期（年/月/日）：")

# else:
#   print(f'{user_date_name}已經過了{delta_date}天，在{user_date_str}這一天你{user_date_story}。')

from datetime import datetime
from colorama import Fore

while True:
  user_date_str = input("請輸入日期（年/月/日）：")
  try:
    user_date = datetime.strptime(user_date_str, "%Y/%m/%d")
  except:
    print("日期格式不正確，請重新輸入")
  else:
    break

user_date_name = input("請輸入紀念日名稱：")
user_date_story = input("在這一天發生了什麼事？")

user_date = datetime.strptime(user_date_str, "%Y/%m/%d")
today = datetime.today()
delta_date = abs(today - user_date).days

print(f'{Fore.CYAN}{user_date_name}已經過了{delta_date}天，在{user_date_str}這一天你{user_date_story}。')


