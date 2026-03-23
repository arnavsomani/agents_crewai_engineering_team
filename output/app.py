import gradio as gr
from accounts import Account, get_share_price

# Initialize a single account for demonstration
user_account = Account(user_id="user123", initial_deposit=1000)

def create_account(initial_deposit):
    global user_account
    user_account = Account(user_id="user123", initial_deposit=initial_deposit)
    return "Account created with initial deposit of ${:.2f}".format(initial_deposit)

def deposit_funds(amount):
    user_account.deposit(amount)
    return "Deposited: ${:.2f}. Current balance: ${:.2f}".format(amount, user_account.balance)

def withdraw_funds(amount):
    try:
        user_account.withdraw(amount)
        return "Withdrew: ${:.2f}. Current balance: ${:.2f}".format(amount, user_account.balance)
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        user_account.buy_shares(symbol, quantity)
        return "Bought {} shares of {}. Current balance: ${:.2f}".format(quantity, symbol, user_account.balance)
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        user_account.sell_shares(symbol, quantity)
        return "Sold {} shares of {}. Current balance: ${:.2f}".format(quantity, symbol, user_account.balance)
    except ValueError as e:
        return str(e)

def get_portfolio_value():
    return "Total portfolio value: ${:.2f}".format(user_account.get_portfolio_value())

def get_profit_loss():
    return "Profit/Loss: ${:.2f}".format(user_account.get_profit_loss())

def get_holdings():
    return user_account.get_holdings()

def get_transactions():
    return user_account.get_transactions()

interface = gr.Interface(
    fn=create_account,
    inputs=gr.Number(label="Initial Deposit"),
    outputs="text",
    title="Trading Account Management",
    description="Create an account and manage your funds."
)

interface.add_function(fn=deposit_funds, inputs=gr.Number(label="Deposit Amount"), outputs="text", title="Deposit Funds")
interface.add_function(fn=withdraw_funds, inputs=gr.Number(label="Withdrawal Amount"), outputs="text", title="Withdraw Funds")
interface.add_function(fn=buy_shares, inputs=[gr.Textbox(label="Stock Symbol"), gr.Number(label="Quantity")], outputs="text", title="Buy Shares")
interface.add_function(fn=sell_shares, inputs=[gr.Textbox(label="Stock Symbol"), gr.Number(label="Quantity")], outputs="text", title="Sell Shares")
interface.add_function(fn=get_portfolio_value, inputs=[], outputs="text", title="Get Portfolio Value")
interface.add_function(fn=get_profit_loss, inputs=[], outputs="text", title="Get Profit/Loss")
interface.add_function(fn=get_holdings, inputs=[], outputs="json", title="Get Holdings")
interface.add_function(fn=get_transactions, inputs=[], outputs="text", title="Get Transactions")

interface.launch()