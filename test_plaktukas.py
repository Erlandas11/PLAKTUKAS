#!/usr/bin/env python3
"""
Tests for PLAKTUKAS
"""

import unittest
from plaktukas import Plaktukas


class TestPlaktukas(unittest.TestCase):
    """Test cases for the Plaktukas class"""
    
    def test_init_default(self):
        """Test default initialization"""
        p = Plaktukas()
        self.assertEqual(p.title, "")
        self.assertEqual(p.content, "")
        self.assertEqual(p.width, 60)
    
    def test_init_with_parameters(self):
        """Test initialization with parameters"""
        p = Plaktukas(title="Test", content="Content", width=40)
        self.assertEqual(p.title, "Test")
        self.assertEqual(p.content, "Content")
        self.assertEqual(p.width, 40)
    
    def test_width_constraints(self):
        """Test that width is constrained between 20 and 100"""
        p1 = Plaktukas(width=10)
        self.assertEqual(p1.width, 20)
        
        p2 = Plaktukas(width=150)
        self.assertEqual(p2.width, 100)
        
        p3 = Plaktukas(width=50)
        self.assertEqual(p3.width, 50)
    
    def test_generate_empty(self):
        """Test generating an empty poster"""
        p = Plaktukas(width=20)
        result = p.generate()
        lines = result.split("\n")
        
        # Should have top and bottom borders
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], "=" * 20)
        self.assertEqual(lines[1], "=" * 20)
    
    def test_generate_with_title(self):
        """Test generating a poster with only title"""
        p = Plaktukas(title="Test", width=20)
        result = p.generate()
        lines = result.split("\n")
        
        # Should have borders, title, and separator
        self.assertGreaterEqual(len(lines), 4)
        self.assertEqual(lines[0], "=" * 20)
        self.assertIn("Test", lines[1])
        self.assertEqual(lines[2], "-" * 20)
    
    def test_generate_with_content(self):
        """Test generating a poster with content"""
        p = Plaktukas(content="Hello World", width=30)
        result = p.generate()
        
        self.assertIn("Hello World", result)
        self.assertIn("=" * 30, result)
    
    def test_generate_full(self):
        """Test generating a complete poster"""
        p = Plaktukas(
            title="Title",
            content="Content goes here",
            width=40
        )
        result = p.generate()
        
        self.assertIn("Title", result)
        self.assertIn("Content goes here", result)
        self.assertIn("=" * 40, result)
        self.assertIn("-" * 40, result)
    
    def test_str_method(self):
        """Test __str__ method"""
        p = Plaktukas(title="Test", content="Content")
        str_result = str(p)
        gen_result = p.generate()
        
        self.assertEqual(str_result, gen_result)
    
    def test_long_content_wrapping(self):
        """Test that long content wraps correctly"""
        long_content = "This is a very long piece of content that should wrap " \
                      "across multiple lines when the poster is generated"
        p = Plaktukas(content=long_content, width=30)
        result = p.generate()
        lines = result.split("\n")
        
        # Check that content is split across multiple lines
        content_lines = [l for l in lines if l and not l.startswith("=")]
        self.assertGreater(len(content_lines), 1)


if __name__ == "__main__":
    unittest.main()
