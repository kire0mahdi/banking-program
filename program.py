import tkinter as tk
from tkinter import messagebox

class BankingApp:
    def __init__(self, root):
        self.balance = 0
        
        # Root Window
        self.root = root
        self.root.title("Banking Program")

        # Widgets
        self.label = tk.Label(root, text="Banking Program", font=("Arial", 16))
        self.label.pack(pady=10)

        self.balance_label = tk.Label(root, text=f"Balance: ${self.balance:.2f}", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit, width=15, font=("Arial", 12))
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw, width=15, font=("Arial", 12))
        self.withdraw_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, width=15, font=("Arial", 12))
        self.exit_button.pack(pady=20)

    def update_balance(self):
        """Update balance label"""
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")

    def deposit(self):
        """Handle deposit operation"""
        amount = self.get_amount("Enter amount to deposit")
        if amount is not None:
            if amount < 0:
                messagebox.showerror("Invalid Input", "Amount must be greater than 0.")
            else:
                self.balance += amount
                self.update_balance()
                messagebox.showinfo("Success", f"${amount:.2f} deposited successfully!")

    def withdraw(self):
        """Handle withdraw operation"""
        amount = self.get_amount("Enter amount to withdraw")
        if amount is not None:
            if amount < 0:
                messagebox.showerror("Invalid Input", "Amount must be greater than 0.")
            elif amount > self.balance:
                messagebox.showerror("Insufficient Funds", "You don't have enough balance.")
            else:
                self.balance -= amount
                self.update_balance()
                messagebox.showinfo("Success", f"${amount:.2f} withdrawn successfully!")

    def get_amount(self, prompt):
        """Prompt user to enter an amount and validate"""
        amount = tk.simpledialog.askstring("Amount", prompt)
        if amount is None:  # Cancel pressed
            return None
        try:
            return float(amount)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return None

# Main Program
if __name__ == "__main__":
    import tkinter.simpledialog  # Needed for input dialogs
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
