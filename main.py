import tkinter as tk

def load_save():
    save = [x.split("\n")[0] for x in open("save.txt", "r", encoding="utf-8").readlines()]
    global coins
    coins = int(save[0])

def save():
    with open("save.txt", "w", encoding="utf-8") as f:
        f.write(str(coins))

def main():
    global window, B_coins, B_quit
    window = tk.Tk()
    height = 400
    length = 400
    window.geometry(f"{height}x{length}")
    window.title("My Window")
    def add_coin():
        global coins, B_coins
        coins += 1
        B_coins.destroy()
        B_coins = tk.Button(window, text=f"Coins: {coins}", command=add_coin)
        B_coins.place(height=30, width=70, x=(length-70)/2, y=30)
        B_coins.pack()
    B_coins = tk.Button(window, text=f"coins:{coins}", command=add_coin)
    B_coins.place(height=30, width=70, x=(length-70)/2, y=30)
    B_coins.pack()
    def quit():
        save()
        window.quit()
    B_quit = tk.Button(window, text="Quit", command=quit)
    B_quit.pack()
    B_quit.place(height=30, width=50, x=(length-50)/2, y=height-30)
    
    window.mainloop()
    
load_save()
main()