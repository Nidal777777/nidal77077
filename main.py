from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class AINidalApp(App):
    def build(self):
        # الشاشة الرئيسية بتصميم مرتب
        root = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # العنوان الترحيبي الفخم
        title_label = Label(
            text="[b]ai.nidal[/b]\nUltimate AI & Software Hub",
            markup=True,
            font_size=24,
            halign='center',
            size_hint_y=0.25
        )
        root.add_widget(title_label)
        
        # نافذة عرض المحادثة أو المخرجات
        self.output_label = Label(
            text="Welcome! System ready for chats and software tools...",
            halign='center',
            valign='middle',
            size_hint_y=0.45
        )
        self.output_label.bind(size=self.output_label.setter('text_size'))
        root.add_widget(self.output_label)
        
        # حقل الإدخال
        self.input_field = TextInput(
            hint_text="Type your command or prompt here...",
            size_hint_y=0.15,
            multiline=False
        )
        root.add_widget(self.input_field)
        
        # أزرار العمليات (دردشة وبرمجيات)
        btn_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.15)
        
        chat_btn = Button(text="AI Chat")
        chat_btn.bind(on_press=self.handle_chat)
        btn_layout.add_widget(chat_btn)
        
        tools_btn = Button(text="Software Tools")
        tools_btn.bind(on_press=self.handle_tools)
        btn_layout.add_widget(tools_btn)
        
        root.add_widget(btn_layout)
        
        return root

    def handle_chat(self, instance):
        user_text = self.input_field.text
        if user_text:
            self.output_label.text = f"AI Chat >> {user_text}\nProcessing response..."
            self.input_field.text = ""
        else:
            self.output_label.text = "AI Chat mode active. Please enter a prompt."

    def handle_tools(self, instance):
        self.output_label.text = "Software Tools Hub >> Initializing advanced code tools..."

if __name__ == '__main__':
    AINidalApp().run()
