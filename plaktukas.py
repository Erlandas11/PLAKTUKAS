#!/usr/bin/env python3
"""
PLAKTUKAS - A simple poster/placard generator
"""


class Plaktukas:
    """A class representing a placard/poster"""
    
    def __init__(self, title="", content="", width=60):
        """
        Initialize a Plaktukas (poster/placard)
        
        Args:
            title: The title of the poster
            content: The main content/message
            width: Width of the poster (default: 60 characters)
        """
        self.title = title
        self.content = content
        self.width = max(20, min(width, 100))  # Constrain width between 20-100
    
    def generate(self):
        """
        Generate the poster/placard as a formatted string
        
        Returns:
            A string representation of the poster
        """
        lines = []
        
        # Top border
        lines.append("=" * self.width)
        
        # Title
        if self.title:
            lines.append(self._center_text(self.title))
            lines.append("-" * self.width)
        
        # Content
        if self.content:
            # Split content into lines that fit within width
            words = self.content.split()
            current_line = ""
            
            for word in words:
                if len(current_line) + len(word) + 1 <= self.width - 4:
                    if current_line:
                        current_line += " " + word
                    else:
                        current_line = word
                else:
                    if current_line:
                        lines.append(self._pad_text(current_line))
                    current_line = word
            
            if current_line:
                lines.append(self._pad_text(current_line))
        
        # Bottom border
        lines.append("=" * self.width)
        
        return "\n".join(lines)
    
    def _center_text(self, text):
        """Center text within the poster width"""
        padding = (self.width - len(text)) // 2
        return " " * padding + text + " " * (self.width - len(text) - padding)
    
    def _pad_text(self, text):
        """Pad text with spaces on both sides"""
        return "  " + text + " " * (self.width - len(text) - 2)
    
    def __str__(self):
        """String representation of the poster"""
        return self.generate()


def main():
    """Main function to demonstrate PLAKTUKAS"""
    # Create a sample poster
    poster = Plaktukas(
        title="PLAKTUKAS",
        content="Welcome to PLAKTUKAS - A simple poster and placard generator!",
        width=60
    )
    
    print(poster)
    print("\n")
    
    # Create another example
    poster2 = Plaktukas(
        title="Important Notice",
        content="This is an example of a poster created with PLAKTUKAS. "
                "You can customize the title, content, and width to create "
                "your own posters and placards.",
        width=50
    )
    
    print(poster2)


if __name__ == "__main__":
    main()
