from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from datetime import datetime
import random

#ai free chatbot cuz im a broke minor dev

Window.clearcolor = (0.93, 0.92, 0.89, 1)
Window.softinput_mode = "below_target"

DARK = (0.05, 0.05, 0.05, 1)
HEADER = (0.02, 0.37, 0.33, 1)
GREEN = (0.07, 0.55, 0.49, 1)
CHAT_BG = (0.93, 0.91, 0.87, 1)
WHITE = (1, 1, 1, 1)
MY_BUBBLE = (0.84, 0.97, 0.80, 1)
BOT_BUBBLE = (1, 1, 1, 1)
MUTED = (0.35, 0.40, 0.40, 1)

def reply(text):
    t = text.lower().strip()

    if any(w in t for w in ("hello", "hi", "hey")):
        return random.choice(["Hey! 👋", "Hello! 😄", "Hey there! 🤖"])
    if "who made you" in t:
    	return "A smart student named Kanishk made me!"
    if "how are you" in t:
        return "I'm doing great! 😄, what about you?"
    if "who are you" in t:
        return "I'm ChatAI  🤖 — a very advanced chatbot."
    if "what can you do" in t:
        return "I can chat, tell jokes, give coding ideas, and answer simple questions."
    if "tell me a joke" in t:
        return "Why did the computer get cold? It left its Windows open! 😂"
    if "im great" in t:
    	return "That's always great to hear!"
    if "what should I code" in t:
        return "Try making a game, quiz, calculator, or your own app! 💻"
    if "time" in t:
        return "It's " + datetime.now().strftime("%I:%M %p").lstrip("0") + "."
    if "date" in t:
        return "Today is " + datetime.now().strftime("%d %B %Y") + "."
    if "thank" in t:
        return "You're welcome! 😄"
    if "bye" in t:
        return "Bye! 👋 See you later!"
    if "what is your name" in t:
    	return "my name is chatAI! I was inspired by Whatsapp Meta Ai!"
    if "what do you do for a living?" in t:
        return "dude i am a chatbot, im not employed"
    if "fun fact" in t:
    	return "the term 'robot' came from the latin word 'robota' which meant forced labour"
    if "↑↓→←↓↓→←→→" in t:
    	return "(6₹_*:+#-3- Hey, Im the dev, so you found my secret message, well, congrats on wasting ur time, have a good one"
    if "?" in t:
        return random.choice([
            "I'm still learning 🤔. Try asking me something simpler!",
            "I don't know that one yet 😅.",
            "Good question! I'm a small offline chatbot."
        ])
    return random.choice([
        "Interesting! 👀", "Cool! 😎", "Got it! 👍",
        "Tell me more!", "Hmm... 🤔", "idk broski ts aint tuff", "i dont know that, but I do know where you live"
    ])


class Bubble(BoxLayout):
    def __init__(self, message, mine=False, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.mine = mine
        self.size_hint_y = None
        self.padding = (dp(13), dp(9), dp(13), dp(6))
        self.spacing = dp(2)

        with self.canvas.before:
            self.bg = Color(*(MY_BUBBLE if mine else BOT_BUBBLE))
            self.rect = RoundedRectangle(
                pos=self.pos, size=self.size, radius=[dp(14)]
            )
        self.bind(pos=self._update_rect, size=self._update_rect)

        # Explicit black text. Do NOT inherit any theme color.
        label = Label(
            text=message,
            color=(0, 0, 0, 1),
            font_size=dp(15),
            halign="left",
            valign="top",
            size_hint_y=None,
            text_size=(dp(285), None),
            padding=(0, 0),
        )
        label.bind(texture_size=self._label_size)
        self.add_widget(label)

        time = Label(
            text=datetime.now().strftime("%I:%M %p").lstrip("0"),
            color=MUTED,
            font_size=dp(9),
            halign="right",
            valign="center",
            size_hint_y=None,
            height=dp(15),
            text_size=(None, dp(15)),
        )
        self.add_widget(time)

        Clock.schedule_once(self._set_height, 0)

    def _label_size(self, label, size):
        label.height = size[1] + dp(2)

    def _set_height(self, *args):
        self.height = self.minimum_height + dp(2)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class ChatAI(App):
    def build(self):
        self.title = "ChatAI Free"

        root = BoxLayout(orientation="vertical")

        # Header
        header = BoxLayout(
            size_hint_y=None,
            height=dp(64),
            padding=(dp(12), dp(6)),
            spacing=dp(6),
        )
        with header.canvas.before:
            Color(*HEADER)
            self.header_rect = RoundedRectangle(
                pos=header.pos, size=header.size, radius=[dp(0)]
            )
        header.bind(
            pos=lambda w, v: setattr(self.header_rect, "pos", w.pos),
            size=lambda w, v: setattr(self.header_rect, "size", w.size),
        )

        avatar = Label(
            text="AI",
            color=WHITE,
            font_size=dp(15),
            bold=True,
            size_hint_x=None,
            width=dp(44),
        )
        header.add_widget(avatar)

        info = BoxLayout(orientation="vertical")
        title = Label(
            text="ChatAI Free",
            color=WHITE,
            font_size=dp(17),
            bold=True,
            halign="left",
            valign="bottom",
        )
        title.bind(size=lambda w, v: setattr(w, "text_size", v))
        status = Label(
            text="offline • free",
            color=(0.82, 1, 0.88, 1),
            font_size=dp(10),
            halign="left",
            valign="top",
        )
        status.bind(size=lambda w, v: setattr(w, "text_size", v))
        info.add_widget(title)
        info.add_widget(status)
        header.add_widget(info)

        clear = Button(
            text="CLEAR",
            color=WHITE,
            font_size=dp(10),
            bold=True,
            size_hint_x=None,
            width=dp(62),
            background_normal="",
            background_color=(0, 0, 0, 0),
        )
        clear.bind(on_release=self.clear_chat)
        header.add_widget(clear)

        root.add_widget(header)

        # Chat area
        self.scroll = ScrollView(do_scroll_x=False, bar_width=dp(3))
        self.chat = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            padding=(dp(8), dp(10)),
            size_hint_y=None,
        )
        self.chat.bind(minimum_height=self.chat.setter("height"))
        self.scroll.add_widget(self.chat)
        root.add_widget(self.scroll)

        # Message composer
        composer = BoxLayout(
            size_hint_y=None,
            height=dp(62),
            padding=dp(7),
            spacing=dp(7),
        )

        self.input = TextInput(
            hint_text="Type a message...",
            hint_text_color=(0.45, 0.48, 0.48, 1),
            foreground_color=(0, 0, 0, 1),
            cursor_color=(0, 0, 0, 1),
            background_color=WHITE,
            font_size=dp(15),
            multiline=False,
            padding=(dp(12), dp(11)),
        )
        self.input.bind(on_text_validate=self.send)
        composer.add_widget(self.input)

        send = Button(
            text="SEND",
            color=WHITE,
            font_size=dp(11),
            bold=True,
            size_hint_x=None,
            width=dp(66),
            background_normal="",
            background_color=GREEN,
        )
        send.bind(on_release=self.send)
        composer.add_widget(send)

        root.add_widget(composer)

        Clock.schedule_once(
            lambda dt: self.add_message(
                "Hey! 👋 I'm ChatAI Free.\nI work completely offline!", False
            ),
            0.1,
        )
        return root

    def add_message(self, text, mine):
        row = BoxLayout(
            size_hint_y=None,
            padding=(dp(0), dp(0)),
        )
        bubble = Bubble(text, mine=mine)

        if mine:
            row.add_widget(Label(size_hint_x=0.17))
            row.add_widget(bubble)
        else:
            row.add_widget(bubble)
            row.add_widget(Label(size_hint_x=0.17))

        row.height = bubble.height
        bubble.bind(height=lambda b, h: setattr(row, "height", h))
        self.chat.add_widget(row)

        Clock.schedule_once(lambda dt: self._bottom(), 0.05)

    def _bottom(self):
        self.scroll.scroll_y = 0

    def send(self, *args):
        text = self.input.text.strip()
        if not text:
            return
        self.input.text = ""
        self.add_message(text, True)
        Clock.schedule_once(
            lambda dt: self.add_message(reply(text), False), 0.35
        )

    def clear_chat(self, *args):
        self.chat.clear_widgets()
        Clock.schedule_once(
            lambda dt: self.add_message("Chat cleared! 👋", False), 0.05
        )


if __name__ == "__main__":
    ChatAI().run()
