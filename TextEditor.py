class TextEditor:
    def __init__(self, n):
        self.n = n
        paragraphs = []
        with open("TextFile.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip() #Removes leading and following whitespace
                if line:
                    paragraphs.append(line)
        self.paragraphs = paragraphs
        self.display = []
        self.pos = 1
        self.index = 0

    def split_text(self):
        """Splits the text into n paragraphs


        Args:
            text (string): The text to be edited as a text file
            n (int): The number of paragraphs to split
        """
        if self.index < len(self.paragraphs):
            for i in range(self.n):
                if self.index < len(self.paragraphs):
                    self.display.append(self.paragraphs[self.index])
                    self.index += 1
        return '\n\n'.join(self.display)
   


    def add(self, x=1):
        """Adds a single line or x lines
        """
        if (self.index < len(self.paragraphs)):
            self.display.append(self.paragraphs[self.index])
            self.index += 1
        return '\n\n'.join(self.display)


    def sub(self, x=1):
        """Removes a single line or x lines
        """
        self.display.pop()
        self.index -= 1
        return '\n\n'.join(self.display)
   
    def next(self):
        """_summary_
        """
        if self.index < len(self.paragraphs):
            self.display = []
            self.split_text()
            self.pos += 1
            return '\n\n'.join(self.display)


    def previous(self):
        """_summary_
        """
        # If we are at the end of the list and we want to go back
        if (self.index == (len(self.paragraphs)) and len(self.paragraphs) % self.n != 0):
            self.index -= (len(self.paragraphs) % self.n) + self.n
        # If we can safely go back n spaces
        elif self.index - self.n*2 > -1:
            self.index -= self.n*2
        # If we are near the start of the list and there are no n lines previous
        else:
            self.index = 0
        self.display = []
        self.pos -= 1
        self.split_text()
        return '\n\n'.join(self.display)


    def display_past(self):
        """_summary_


        Returns:
            _type_: _description_
        """
        return '\n\n'.join(self.paragraphs[: self.index])
   
    def display_all(self):
        """_summary_


        Returns:
            _type_: _description_
        """
        return '\n\n'.join(self.paragraphs)

    def save(self, edited_content, original_line_count):
        line_diff = len(edited_content) - original_line_count

        if self.index - self.n < 0: #Means we are near front of list 
            self.paragraphs = edited_content + self.paragraphs[self.index:]
        else:
            self.paragraphs = self.paragraphs[:self.index - original_line_count] + edited_content + self.paragraphs[self.index:]

        self.index += line_diff
        self.display = edited_content

    def reset_lines(self):
        self.paragraphs = [line.strip() for line in self.paragraphs]



# Have to fix when keep pressing next and we go to the last blank page and that updates the dipslay to be []
# function that shows you how many passages you have [14/30]
