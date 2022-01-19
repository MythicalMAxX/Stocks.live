from yahoo_fin import stock_info as si
from yahoo_fin import news
from tqdm import tqdm
from time import sleep
import pprint as p
from art import *


task = ["live price","company info","historical data","top gainers","top loosers","top crypto","trending today","news","quit"]
task_len = len(task)

def progress():
    for i in tqdm(range(101),
                  desc="Restarting…",
                  ascii=False, ncols=75):
        sleep(0.01)

def error1():
    print("Check your internet connection")
    print("Check for your input")

def start():
    print("Hi what can i do for you?"
          "\nMAIN MENU")
    for i in range(task_len):
        print(f"{i + 1}). {task[i]}")
    operation = input("Choose the operation:")
    operation = operation.lower()
    operation_type(operation)


def live_price():
    stock_name = input("enter stock nse code:")
    try:
        current_Price = si.get_live_price(stock_name)
        print(f"Current price of {stock_name} is {current_Price}")
        progress()
        start()
    except:
        print("Something Went Wrong... Try Again Later")
        error1()
        author()


def About():
    stock_name = input("enter stock nse code:")
    try:
        status = si.get_company_info(stock_name)
        print(status)
        progress()
        start()
    except:
        print("Something Went Wrong... Try Again Later")
        error1()
        author()


def historical_data():
    stock_name = input("enter stock nse code:")
    print("Date format dd/mm/yyyy")
    start_date = input("Enter start date:")
    end_date = input("Enter end date:")
    interval = input("Set Interval\n Available Intervals\n daily\n week\n month"
                     "\n Select interval:")
    try:
        data = si.get_data(stock_name,start_date,end_date,interval)
        print(data)
        progress()
        start()
    except:
        print("Something Went Wrong... Try Again Later")
        error1()
        author()

def top_gainers():
    try:
        gainers = si.get_day_gainers()
        print(f"Top gainers of today are {gainers}")
        progress()
        start()
    except:
        print("Something Went Wrong... Try Again Later")
        author()


def top_loosers():
    try:
        losers = si.get_day_losers()
        print(f"Top gainers of today are {losers}")
        progress()
        start()
    except:
        print("Something Went Wrong... Try Again Later")
        author()


def top_crypto():
    try:
        top_c = si.get_top_crypto()
        print(f"Top gainers of today are {top_c}")
        progress()
        start()
    except:
        print("Something Went Wrong... Try Again Later")
        author()

def trending():
    try:
        trend = si.get_day_most_active()
        print(f"Top gainers of today are {trend}")
        progress()
        start()
    except:
        print("Something Went Wrong... Try Again Later")
        author()

def News():
    stock_name = input("Enter stock nse code:")
    try:
        tnews = news.get_yf_rss(stock_name)
        for i in range(5):
            trend = tnews[i]
            trend = trend["link"]
            p.pprint(f"News {i+1}). {trend}")
        progress()
        start()
    except:
        print("Something Went Wrong... Try Again Later")
        error1()
        author()


def operation_type(operation):
    if operation in task:
        print(f"You selected {operation}")
        if operation == "live price":
            live_price()
        
        elif operation == "company info":
            About()
        elif operation == "historical data":
            historical_data()
        elif operation == "top gainers":
            top_gainers()
        elif operation == "top loosers":
            top_loosers()
        elif operation == "top crypto":
            top_crypto()
        elif operation == "trending today":
            trending()
        elif operation == "news":
            News()
        elif operation == "quit":
            confirmation = input("Would you like to close the program?"
                  "\nEnter y if yes or any key if no:")
            if confirmation == "y":
                author()
                quit()
            else:
                start()
        else:
            pass
    else:
        print("Invalid input")
        print("restarting...")
        progress()
        start()

def author():
    print("Author:")
    tprint("Vinamra Yadav", "3-d")

start()

