import unittest
from TextEditor import TextEditor


class TestTextEditor(unittest.TestCase):
    def setUp(self):
        self.editor = TextEditor(3)
        self.editor.paragraphs = [
            "Paragraph 1",
            "Paragraph 2",
            "Paragraph 3",
            "Paragraph 4",
            "Paragraph 5",
            "Paragraph 6",
            "Paragraph 7"
        ]

    def test_split_text(self):
        self.editor.split_text()
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.assertEqual(self.editor.index, 3)

    def test_split_text2(self):
        self.editor.index = 3
        self.editor.split_text()
        self.assertEqual(self.editor.display, ["Paragraph 4", "Paragraph 5", "Paragraph 6"])
        self.assertEqual(self.editor.index, 6)

    def test_split_text3(self):
        self.editor.split_text()
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.editor.next()
        self.assertEqual(self.editor.display, ["Paragraph 4", "Paragraph 5", "Paragraph 6"])
        self.editor.next()
        self.assertEqual(self.editor.display, ["Paragraph 7"])


    def test_add(self):
        self.editor.index = 2
        self.editor.display = ["Paragraph 1", "Paragraph 2"]
        self.editor.add()
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.assertEqual(self.editor.index, 3)

    # def test_add2(self):
    #     self.editor.index = 2
    #     self.editor.display = ["Paragraph 1", "Paragraph 2"]
    #     self.editor.add(2)
    #     self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3", "Paragraph 4"])
    #     self.assertEqual(self.editor.index, 4)
    
    def test_add3(self):
        self.editor.split_text()
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.editor.next()
        self.editor.add(3)
        self.assertEqual(self.editor.display, ["Paragraph 4", "Paragraph 5", "Paragraph 6", "Paragraph 7"])

    def test_sub(self):
        self.editor.split_text()
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.editor.sub()
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2"])

    def test_sub2(self):
        self.editor.split_text()
        self.editor.next()
        self.assertEqual(self.editor.display, ["Paragraph 4", "Paragraph 5", "Paragraph 6"])
        self.editor.sub()
        self.assertEqual(self.editor.display, ["Paragraph 4", "Paragraph 5"])

    def test_next(self):
        self.editor.index = 0
        self.editor.split_text()
        self.editor.next()
        self.assertEqual(self.editor.display, ["Paragraph 4", "Paragraph 5", "Paragraph 6"])
        self.assertEqual(self.editor.index, 6)

    def test_next2(self):
        self.editor.index = 0
        self.editor.split_text()
        self.editor.next()
        self.assertEqual(self.editor.display, ["Paragraph 4", "Paragraph 5", "Paragraph 6"])
        self.assertEqual(self.editor.index, 6)
        self.editor.next()
        self.assertEqual(self.editor.display, ["Paragraph 7"])

    def test_previous(self):
        self.editor.split_text()
        self.editor.previous()
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.assertEqual(self.editor.index, 3)

    def test_previous2(self):
        self.editor.split_text()
        self.editor.next()
        self.assertEqual(self.editor.display, ["Paragraph 4", "Paragraph 5", "Paragraph 6"])
        self.assertEqual(self.editor.index, 6)
        self.editor.previous()
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.assertEqual(self.editor.index, 3)

    def test_previous3(self):
        self.editor.split_text()
        self.editor.previous()
        #self.assertEqual(self.editor.pre, [])
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.assertEqual(self.editor.index, 3)

    def test_previous4(self):
        self.editor.split_text()
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.editor.next()
        self.assertEqual(self.editor.display, ["Paragraph 4", "Paragraph 5", "Paragraph 6"])
        self.assertEqual(self.editor.index, 6)
        self.editor.next()
        self.assertEqual(self.editor.display, ["Paragraph 7"])
        self.editor.previous()
        self.assertEqual(self.editor.display, ["Paragraph 4", "Paragraph 5", "Paragraph 6"])
        self.assertEqual(self.editor.index, 6)
        self.editor.next()
        self.assertEqual(self.editor.display, ["Paragraph 7"])

    # Test Case 1: Replace lines with edited content
    def test_save(self):
        self.editor.split_text()  # Split the text into paragraphs
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.edited_content = ["Paragraph 1", "Line 2 edited", "Line 3 edited"]
        self.editor.save(self.edited_content)
        # Verify the changes in paragraphs
        assert self.editor.paragraphs == ["Paragraph 1", "Line 2 edited", "Line 3 edited", "Paragraph 4", "Paragraph 5", "Paragraph 6", "Paragraph 7"]
        assert self.editor.display == ["Paragraph 1", "Line 2 edited", "Line 3 edited"]
        self.editor.next()
        self.editor.previous()
        assert self.editor.paragraphs ==  ["Paragraph 1", "Line 2 edited", "Line 3 edited", "Paragraph 4", "Paragraph 5", "Paragraph 6", "Paragraph 7"]
        # Verify the updated index
        assert self.editor.index == 3

    # Test Case 2: Add new lines with edited content
    def test_save2(self):
        self.editor.split_text()  # Split the text into paragraphs
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.edited_content = ["Paragraph 1", "Line 2 edited", "Line added", "Line 3 edited"]
        assert self.editor.index == 3
        self.editor.save(self.edited_content, 3)
        # Verify the changes in paragraphs
        assert self.editor.paragraphs == ["Paragraph 1", "Line 2 edited", "Line added", "Line 3 edited", "Paragraph 4", "Paragraph 5", "Paragraph 6", "Paragraph 7"]
        assert self.editor.display == ["Paragraph 1", "Line 2 edited", "Line added", "Line 3 edited"]
        self.editor.next()
        self.editor.previous()
        assert self.editor.paragraphs ==  ["Paragraph 1", "Line 2 edited", "Line added", "Line 3 edited", "Paragraph 4", "Paragraph 5", "Paragraph 6", "Paragraph 7"]
        # Verify the updated index
        assert self.editor.index == 4

    # Test Case 3: Delete lines and adjust index
    def test_save3(self):
        self.editor.split_text()  # Split the text into paragraphs
        self.assertEqual(self.editor.display, ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.edited_content = ["Paragraph 1"]
        assert self.editor.index == 3
        self.editor.save(self.edited_content, 3)
        # Verify the changes in paragraphs
        assert self.editor.paragraphs == ["Paragraph 1", "Paragraph 4", "Paragraph 5", "Paragraph 6", "Paragraph 7"]
        assert self.editor.display == ["Paragraph 1"]
        self.editor.next()
        assert self.editor.display == ["Paragraph 4", "Paragraph 5", "Paragraph 6"]
        self.editor.previous()
        assert self.editor.display == ["Paragraph 1", "Paragraph 4", "Paragraph 5"]
        self.editor.next()
        assert self.editor.display == ["Paragraph 6", "Paragraph 7"]
        assert self.editor.paragraphs ==  ["Paragraph 1", "Paragraph 4", "Paragraph 5", "Paragraph 6", "Paragraph 7"]
        # Verify the updated index
        assert self.editor.index == 5

        

if __name__ == '__main__':
    unittest.main()
