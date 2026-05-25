import tkinter as tk
import requests
import random

# ---------------- API KEY ----------------
API_KEY = "f1bc748730ac5c5ed8e163102e4b20e6"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ---------------- WEATHER FUNCTION ----------------
def get_weather():
    city = city_entry.get().strip()

    if not city:
        result_label.config(text="Enter a city 🌸")
        return

    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        print("DEBUG:", data)  # 👈 IMPORTANT FOR TESTING

        # ✅ FIX: proper error handling
        if str(data.get("cod")) != "200":
            msg = data.get("message", "Unknown error")
            result_label.config(text=f"❌ {msg}")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        result_label.config(
            text=f"🌸 {city.title()} 🌸\n\n"
                 f"🌡 Temperature: {temp}°C\n"
                 f"🌥 Condition: {weather}\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"🌬 Wind: {wind} m/s"
        )

    except requests.exceptions.RequestException:
        result_label.config(text="❌ Network error")
    except Exception as e:
        result_label.config(text=f"❌ Error: {str(e)}")


# ---------------- SAKURA ANIMATION ----------------
petals = []

def create_petals():
    for _ in range(45):
        x = random.randint(0, 520)
        y = random.randint(-700, 0)
        size = random.randint(4, 10)

        petal = canvas.create_oval(
            x, y, x + size, y + size,
            fill="#ffb6c1",
            outline=""
        )

        speed = random.randint(2, 6)
        petals.append([petal, speed])


def animate():
    for p in petals:
        canvas.move(p[0], 0, p[1])

        pos = canvas.coords(p[0])
        if pos and pos[1] > 720:
            canvas.move(p[0], random.randint(0, 520), -800)

    window.after(50, animate)


# ---------------- UI ----------------
window = tk.Tk()
window.title("🌸 Sakura Weather Studio Pro")
window.geometry("520x720")
window.resizable(False, False)

canvas = tk.Canvas(window, width=520, height=720, bg="#120018", highlightthickness=0)
canvas.pack(fill="both", expand=True)

create_petals()
animate()

# ---------------- GLASS FRAME ----------------
frame = tk.Frame(window, bg="#1f0f2e")
frame.place(relx=0.5, rely=0.5, anchor="center")

# TITLE
tk.Label(
    frame,
    text="🌸 WEATHER STUDIO PRO 🌸",
    font=("Arial", 16, "bold"),
    fg="#ff69b4",
    bg="#1f0f2e"
).pack(pady=10)

# INPUT
city_entry = tk.Entry(
    frame,
    font=("Arial", 14),
    width=25,
    justify="center",
    bg="#2a1b3d",
    fg="#ffb6c1",
    insertbackground="white"
)
city_entry.pack(pady=10)

# BUTTON
tk.Button(
    frame,
    text="🌦 Get Weather",
    command=get_weather,
    bg="#ff69b4",
    fg="white",
    relief="flat",
    width=20
).pack(pady=5)

# RESULT
result_label = tk.Label(
    frame,
    text="Enter a city 🌸",
    bg="#1f0f2e",
    fg="white",
    font=("Arial", 13),
    justify="center"
)
result_label.pack(pady=20)

window.mainloop()