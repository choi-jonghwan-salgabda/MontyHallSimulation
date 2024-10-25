class Documentation:
    def __init__(self, title):
        self.title = title
        self.content = ""

    def add_content(self, text):
        self.content += text + "\n"

    def generate_document(self):
        with open(f"{self.title}.txt", "w") as file:
            file.write(self.content)

