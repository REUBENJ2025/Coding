# Luck test
# ReubenJoseph
# 03/10/25
# AS Computer Science
# Greg Allock

import tkinter as tk
import random

# --- CONFIG ---
symbols = [
    ("🍒", "red"),
    ("🍋", "yellow"),
    ("🔔", "orange"),
    ("⭐", "gold"),
    ("💎", "cyan"),
    ("🍀", "green")
]

GRID_SIZE = 5
START_CREDITS = 20
ROUNDS = 10

# --- GAME STATE ---
credits = START_CREDITS
rounds_left = ROUNDS
spinning = False
multiplier = 1
wild_symbol = None  # upgrade: can set later


# --- FUNCTIONS ---
def spin_animation(steps=15):
    global spinning
    if steps > 0:
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                sym, color = random.choice(symbols)
                slot_labels[r][c].config(text=sym, fg=color)
        root.after(100, spin_animation, steps - 1)
    else:
        spinning = False
        check_win()


def spin():
    global credits, rounds_left, spinning
    if spinning or credits <= 0 or rounds_left <= 0:
        return

    credits -= 1
    rounds_left -= 1
    credit_label.config(text=f"Credits: {credits}")
    rounds_label.config(text=f"Rounds left: {rounds_left}")
    result_label.config(text="Spinning...")
    spinning = True
    spin_animation()


def check_win():
    global credits
    grid = [[slot_labels[r][c].cget("text") for c in range(GRID_SIZE)] for r in range(GRID_SIZE)]
    wins = 0

    # Rows
    for row in grid:
        if all(s == row[0] or (wild_symbol and wild_symbol in row) for s in row):
            wins += 1
    # Cols
    for c in range(GRID_SIZE):
        col = [grid[r][c] for r in range(GRID_SIZE)]
        if all(s == col[0] or (wild_symbol and wild_symbol in col) for s in col):
            wins += 1
    # Diags
    diag1 = [grid[i][i] for i in range(GRID_SIZE)]
    diag2 = [grid[i][GRID_SIZE - 1 - i] for i in range(GRID_SIZE)]
    if all(s == diag1[0] or (wild_symbol and wild_symbol in diag1) for s in diag1):
        wins += 1
    if all(s == diag2[0] or (wild_symbol and wild_symbol in diag2) for s in diag2):
        wins += 1

    if wins > 0:
        payout = wins * 5 * multiplier
        credits += payout
        result_label.config(text=f"WIN! {wins} line(s)! +{payout} credits 🎉")
    else:
        result_label.config(text="No win!")

    credit_label.config(text=f"Credits: {credits}")


# --- SHOP / UPGRADES ---
def buy_upgrade(upgrade):
    global credits, multiplier, wild_symbol
    if upgrade == "multiplier" and credits >= 10:
        credits -= 10
        multiplier += 1
        result_label.config(text=f"Multiplier upgraded! Now x{multiplier}")
    elif upgrade == "wild" and credits >= 15:
        credits -= 15
        wild_symbol = "⭐"
        result_label.config(text="Wild ⭐ activated!")
    else:
        result_label.config(text="Not enough credits!")

    credit_label.config(text=f"Credits: {credits}")


# --- GUI ---
root = tk.Tk()
root.title("Python Slot Machine 🎰")
root.geometry("600x700")

title_label = tk.Label(root, text="🎰 Python Slot Machine 🎰", font=("Arial", 20))
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

slot_labels = []
for r in range(GRID_SIZE):
    row_labels = []
    for c in range(GRID_SIZE):
        lbl = tk.Label(frame, text="❓", font=("Arial", 24), width=4)
        lbl.grid(row=r, column=c, padx=5, pady=5)
        row_labels.append(lbl)
    slot_labels.append(row_labels)

result_label = tk.Label(root, text="Press Spin!", font=("Arial", 14))
result_label.pack(pady=10)

credit_label = tk.Label(root, text=f"Credits: {credits}", font=("Arial", 14))
credit_label.pack(pady=5)

rounds_label = tk.Label(root, text=f"Rounds left: {rounds_left}", font=("Arial", 14))
rounds_label.pack(pady=5)

spin_button = tk.Button(root, text="Spin 🎲", font=("Arial", 16), command=spin)
spin_button.pack(pady=15)

# SHOP
shop_label = tk.Label(root, text="--- SHOP ---", font=("Arial", 16))
shop_label.pack(pady=10)

btn_mult = tk.Button(root, text="Upgrade Multiplier (10 credits)", command=lambda: buy_upgrade("multiplier"))
btn_mult.pack(pady=5)

btn_wild = tk.Button(root, text="Unlock Wild ⭐ (15 credits)", command=lambda: buy_upgrade("wild"))
btn_wild.pack(pady=5)

root.mainloop()

