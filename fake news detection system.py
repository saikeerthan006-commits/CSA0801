import tkinter as tk
from tkinter import scrolledtext


# -------------------------------------------------
# FUNCTION TO CHECK NEWS
# -------------------------------------------------

def check_news():

    news = text_box.get("1.0", tk.END).strip().lower()

    # Check whether input is empty
    if news == "":
        result_label.config(
            text="Please enter a news article!",
            fg="orange"
        )
        score_label.config(text="")
        return

    # Large list of suspicious keywords and phrases
    fake_words = [

        # Sensational words
        "shocking",
        "unbelievable",
        "unbelievable news",
        "you won't believe",
        "you will not believe",
        "amazing",
        "incredible",
        "miracle",
        "miracle cure",
        "secret",
        "secret cure",
        "secret method",
        "hidden truth",
        "truth revealed",
        "exposed",
        "exposed truth",

        # Urgency
        "urgent",
        "urgent warning",
        "act now",
        "act immediately",
        "do it now",
        "hurry",
        "last chance",
        "limited time",
        "before it's too late",
        "warning",
        "breaking",
        "breaking news",

        # Money related
        "free money",
        "earn money fast",
        "make money fast",
        "get rich quick",
        "easy money",
        "instant money",
        "cash reward",
        "free cash",
        "win money",
        "claim your reward",
        "claim money",
        "guaranteed income",
        "100% profit",
        "double your money",

        # Scam-like phrases
        "click here",
        "click now",
        "click this link",
        "share this",
        "share immediately",
        "forward this",
        "send this to everyone",
        "register now",
        "sign up now",
        "limited offer",
        "special offer",
        "free offer",

        # Health misinformation
        "cure all diseases",
        "cures every disease",
        "cure cancer instantly",
        "instant cure",
        "permanent cure",
        "no side effects",
        "guaranteed cure",
        "100% effective",
        "miracle treatment",
        "secret treatment",
        "doctors don't want you to know",

        # Conspiracy-style phrases
        "government is hiding",
        "government is hiding the truth",
        "they don't want you to know",
        "media is hiding",
        "hidden information",
        "secret government",
        "cover up",
        "massive cover up",
        "conspiracy",
        "they are lying",
        "the truth they hide",

        # Fake authority claims
        "scientists shocked",
        "doctors shocked",
        "experts are shocked",
        "experts cannot explain",
        "scientists cannot explain",
        "doctors cannot explain",
        "researchers shocked",

        # Viral/social media language
        "viral",
        "going viral",
        "must watch",
        "must read",
        "must share",
        "share before deleted",
        "internet is exploding",
        "social media is exploding",
        "everyone is talking about",

        # Exaggeration
        "world's first",
        "world's biggest",
        "never seen before",
        "never before",
        "historic discovery",
        "revolutionary discovery",
        "life changing",
        "life-changing",
        "once in a lifetime",
        "impossible",
        "completely unbelievable",
        "miraculous discovery",

        # Clickbait
        "clickbait",
        "read this immediately",
        "read before it is deleted",
        "watch before it is deleted",
        "this will shock you",
        "this changes everything",
        "what happens next will shock you",
        "you won't believe what happened",

        # Guaranteed claims
        "guaranteed",
        "100% guaranteed",
        "zero risk",
        "risk free",
        "risk-free",
        "guaranteed results",
        "guaranteed success",
        "guaranteed profit",

        # Fake announcement style
        "breaking alert",
        "breaking announcement",
        "major announcement",
        "huge announcement",
        "urgent announcement",
        "emergency alert",
        "secret announcement"
    ]

    # Count suspicious keywords
    count = 0

    found_words = []

    for word in fake_words:

        if word in news:

            count = count + 1
            found_words.append(word)

    # -------------------------------------------------
    # DISPLAY RESULT
    # -------------------------------------------------

    if count >= 3:

        result_label.config(
            text="⚠ FAKE NEWS",
            fg="red"
        )

    elif count >= 1:

        result_label.config(
            text="⚠ SUSPICIOUS NEWS",
            fg="orange"
        )

    else:

        result_label.config(
            text="✓ POSSIBLY REAL NEWS",
            fg="green"
        )

    # Display number of suspicious keywords
    score_label.config(
        text="Suspicious keywords found: " + str(count)
    )


# -------------------------------------------------
# CLEAR FUNCTION
# -------------------------------------------------

def clear_news():

    text_box.delete("1.0", tk.END)

    result_label.config(
        text="Result will appear here",
        fg="gray"
    )

    score_label.config(text="")


# -------------------------------------------------
# MAIN WINDOW
# -------------------------------------------------

window = tk.Tk()

window.title("Fake News Detection System")

window.geometry("850x700")

window.resizable(False, False)

window.configure(bg="#101827")


# -------------------------------------------------
# HEADER
# -------------------------------------------------

header = tk.Frame(
    window,
    bg="#1e293b",
    height=110
)

header.pack(fill="x")


title_label = tk.Label(
    header,
    text="FAKE NEWS DETECTION SYSTEM",
    font=("Arial", 25, "bold"),
    bg="#1e293b",
    fg="white"
)

title_label.pack(pady=(22, 5))


subtitle_label = tk.Label(
    header,
    text="Analyze news content using keyword-based detection",
    font=("Arial", 11),
    bg="#1e293b",
    fg="#cbd5e1"
)

subtitle_label.pack()


# -------------------------------------------------
# CONTENT
# -------------------------------------------------

content = tk.Frame(
    window,
    bg="#101827"
)

content.pack(
    fill="both",
    expand=True,
    padx=50,
    pady=25
)


# -------------------------------------------------
# INPUT TITLE
# -------------------------------------------------

input_label = tk.Label(
    content,
    text="Enter News Article",
    font=("Arial", 15, "bold"),
    bg="#101827",
    fg="white"
)

input_label.pack(anchor="w")


# -------------------------------------------------
# TEXT BOX
# -------------------------------------------------

text_box = scrolledtext.ScrolledText(
    content,
    width=90,
    height=14,
    font=("Arial", 11),
    wrap=tk.WORD,
    bg="white",
    fg="black",
    insertbackground="black",
    relief="flat",
    padx=12,
    pady=12
)

text_box.pack(
    pady=(10, 20)
)


# -------------------------------------------------
# BUTTONS
# -------------------------------------------------

button_frame = tk.Frame(
    content,
    bg="#101827"
)

button_frame.pack()


check_button = tk.Button(
    button_frame,
    text="CHECK NEWS",
    command=check_news,
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    padx=35,
    pady=12,
    cursor="hand2"
)

check_button.pack(
    side=tk.LEFT,
    padx=10
)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    command=clear_news,
    font=("Arial", 12, "bold"),
    bg="#475569",
    fg="white",
    activebackground="#64748b",
    activeforeground="white",
    relief="flat",
    padx=35,
    pady=12,
    cursor="hand2"
)

clear_button.pack(
    side=tk.LEFT,
    padx=10
)


# -------------------------------------------------
# RESULT BOX
# -------------------------------------------------

result_frame = tk.Frame(
    content,
    bg="#1e293b"
)

result_frame.pack(
    fill="x",
    pady=25
)


result_title = tk.Label(
    result_frame,
    text="DETECTION RESULT",
    font=("Arial", 11, "bold"),
    bg="#1e293b",
    fg="#94a3b8"
)

result_title.pack(pady=(18, 5))


result_label = tk.Label(
    result_frame,
    text="Result will appear here",
    font=("Arial", 21, "bold"),
    bg="#1e293b",
    fg="gray"
)

result_label.pack(pady=5)


score_label = tk.Label(
    result_frame,
    text="",
    font=("Arial", 11),
    bg="#1e293b",
    fg="white"
)

score_label.pack(pady=(2, 18))


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

footer = tk.Label(
    window,
    text="Python • Tkinter • Rule-Based Fake News Detection",
    font=("Arial", 9),
    bg="#101827",
    fg="#64748b"
)

footer.pack(pady=(0, 12))


# -------------------------------------------------
# RUN APPLICATION
# -------------------------------------------------

window.mainloop()