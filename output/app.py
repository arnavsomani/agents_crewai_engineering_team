import gradio as gr
from accounts import Account, get_share_price

# Create an instance of the Account class for a single user
user_account = Account("DemoUser")

def create_account(initial_deposit):
    user_account.create_account(initial_deposit)
    return f"Account created with an initial deposit of ${initial_deposit}."

def deposit_funds(amount):
    user_account.deposit(amount)
    return f"Deposited ${amount}. Current balance: ${user_account.balance}."

def withdraw_funds(amount):
    try:
        user_account.withdraw(amount)
        return f"Withdrew ${amount}. Current balance: ${user_account.balance}."
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        user_account.buy_shares(symbol, quantity)
        return f"Bought {quantity} shares of {symbol}."
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        user_account.sell_shares(symbol, quantity)
        return f"Sold {quantity} shares of {symbol}."
    except ValueError as e:
        return str(e)

def portfolio_value():
    return f"Total portfolio value: ${user_account.calculate_portfolio_value()}."

def report_holdings():
    holdings = user_account.report_holdings()
    return holdings if holdings else "No holdings."

def report_profit_loss():
    profit_loss = user_account.report_profit_loss()
    return f"Profit/Loss: ${profit_loss}."

def list_transactions():
    transactions = user_account.list_transactions()
    return transactions if transactions else "No transactions."

# Gradio UI layout
with gr.Blocks() as demo:
    gr.Markdown("# Trading Account Management System")
    
    with gr.Tab("Account Operations"):
        initial_deposit = gr.Number(label="Initial Deposit", value=1000, step=100)
        gr.Button("Create Account").click(create_account, inputs=initial_deposit, outputs="output")
        gr.Markdown("### Deposit Funds")
        deposit_amount = gr.Number(label="Deposit Amount", step=50)
        gr.Button("Deposit").click(deposit_funds, inputs=deposit_amount, outputs="output")
        
        gr.Markdown("### Withdraw Funds")
        withdraw_amount = gr.Number(label="Withdraw Amount", step=50)
        gr.Button("Withdraw").click(withdraw_funds, inputs=withdraw_amount, outputs="output")
        
        gr.Markdown("### Buy Shares")
        buy_symbol = gr.Textbox(label="Share Symbol (e.g., AAPL, TSLA, GOOGL)")
        buy_quantity = gr.Number(label="Quantity", step=1)
        gr.Button("Buy").click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs="output")
        
        gr.Markdown("### Sell Shares")
        sell_symbol = gr.Textbox(label="Share Symbol (e.g., AAPL, TSLA, GOOGL)")
        sell_quantity = gr.Number(label="Quantity", step=1)
        gr.Button("Sell").click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs="output")

    with gr.Tab("Portfolio Information"):
        gr.Button("Portfolio Value").click(portfolio_value, outputs="output")
        gr.Button("Report Holdings").click(report_holdings, outputs="output")
        gr.Button("Report Profit/Loss").click(report_profit_loss, outputs="output")
        gr.Button("List Transactions").click(list_transactions, outputs="output")

    output = gr.Textbox(label="Output", interactive=False)

demo.launch()