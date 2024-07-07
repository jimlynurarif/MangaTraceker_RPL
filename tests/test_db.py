import unittest
import sqlite3
import os
import sys
# Add the src directory to the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from MangaTracker.db import add_manga, ubah_manga, get_all_manga, get_genre_by_judul, delete_manga, ganti_status_manga


class TestMangaDatabase(unittest.TestCase):
    def test_db(self):
      self.assertEqual(1,1)

    def test_add(self):
       self.conn = sqlite3.connect("manga_database.db")
       self.c = self.conn.cursor()

       self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Test Manga",))
       manga = self.c.fetchone()
       if manga:
        delete_manga("Test Manga")
       add_manga("Test Manga", "ongoing", 1, 100, "2024-05-01", "2024-05-01", "Great manga", ["action", "adventure"])
       self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Test Manga",))
       manga = self.c.fetchone()
       self.assertEqual(manga[0], "Test Manga")
       self.assertEqual(manga[1], "ongoing")
       self.assertEqual(manga[2], 1)
       self.assertEqual(manga[3], 100)
       self.assertEqual(manga[4], "2024-05-01")
       delete_manga("Test manga")

    def test_delete(self):
      self.conn = sqlite3.connect("manga_database.db")
      self.c = self.conn.cursor()

      self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Test Manga",))
      manga = self.c.fetchone()
      if not manga:
        add_manga("Test Manga", "ongoing", 1, 100, "2024-05-01", "2024-05-01", "Great manga", ["action", "adventure"])
      delete_manga("Test Manga")
      self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Test Manga",))
      manga = self.c.fetchone()
      self.assertEqual(manga, None)

    def test_ubah(self):
      self.conn = sqlite3.connect("manga_database.db")
      self.c = self.conn.cursor()

      self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Test Manga",))
      manga = self.c.fetchone()
      if not manga:
        add_manga("Test Manga", "ongoing", 1, 100, "2024-05-01", "2024-05-01", "Great manga", ["action", "adventure"])
      self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Judul Baru",))
      manga = self.c.fetchone()
      if manga:
        delete_manga("Judul Baru")
      ubah_manga("Test Manga", "Judul Baru", "finished", 2, 200, "2024-06-01", "2024-06-01", "Peak", ["romance"])
      self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Judul Baru",))
      manga = self.c.fetchone()
      self.assertEqual(manga[0], "Judul Baru")
      self.assertEqual(manga[1], "finished")
      self.assertEqual(manga[2], 2)
      self.assertEqual(manga[3], 200)
      self.assertEqual(manga[6], "Peak")
      delete_manga("Judul Baru")

    def test_get_all(self):
      self.conn = sqlite3.connect("manga_database.db")
      self.c = self.conn.cursor()

      self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Test Manga",))
      manga = self.c.fetchone()
      len1 = len(get_all_manga())
      if not manga:
        add_manga("Test Manga", "ongoing", 1, 100, "2024-05-01", "2024-05-01", "Great manga", ["action", "adventure"])
        len2 = len(get_all_manga())
        self.assertEqual(len1, len2-1)
        delete_manga("Test Manga")
      else:
        delete_manga("Test Manga")
        len2 = len(get_all_manga())
        self.assertEqual(len1, len2+1)

    def test_genre(self):
      self.conn = sqlite3.connect("manga_database.db")
      self.c = self.conn.cursor()

      self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Test Manga",))
      manga = self.c.fetchone()
      if manga:
        delete_manga("Test Manga")
      add_manga("Test Manga", "ongoing", 1, 100, "2024-05-01", "2024-05-01", "Great manga", ["action", "adventure"])
      genres = get_genre_by_judul("Test Manga")
      self.assertEqual(genres, "action, adventure")
      delete_manga("Test Manga")
    
    def test_ganti_status(self):
      self.conn = sqlite3.connect("manga_database.db")
      self.c = self.conn.cursor()

      self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Test Manga",))
      manga = self.c.fetchone()
      if not manga:
        add_manga("Test Manga", "ongoing", 1, 100, "2024-05-01", "2024-05-01", "Great manga", ["action", "adventure"])
      
      ganti_status_manga("Test Manga", "finished")
      self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Test Manga",))
      manga = self.c.fetchone()
      self.assertEqual(manga[1], "finished")
      delete_manga("Test Manga")
    # def setUp(self):
    #     # Path to the original database
    #     self.original_db = "manga_database.db"
    #     # Path to the test database
    #     self.test_db = "test_manga_database.db"
        
    #     # Copy the original database to the test database
    #     shutil.copy(self.original_db, self.test_db)
        
    #     # Connect to the test database
    #     self.conn = sqlite3.connect(self.test_db)
    #     self.c = self.conn.cursor()

    # def tearDown(self):
    #     # Close the connection and remove the test database
    #     self.conn.close()
    #     os.remove(self.test_db)

    # def test_add_manga(self):
    #     self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Test Manga",))
    #     manga = self.c.fetchone()
    #     if manga:
    #         delete_manga("Test Manga")
    #     add_manga("Test Manga", "ongoing", 1, 100, "2024-05-01", "2024-05-01", "Great manga", ["action", "adventure"])
    #     manga = self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Test Manga",))
    #     # manga = self.c.fetchone()
    #     self.assertIsNotNone(manga)
    #     self.assertEqual(manga[0], "Test Manga")
    #     self.assertEqual(manga[1], "ongoing")
    #     self.assertEqual(manga[3], 100)
    #     self.c.execute("SELECT genre FROM genre_manga WHERE judul = ?", ("Test Manga",))
    #     genres = self.c.fetchall()
    #     self.assertEqual(len(genres), 2)

    # def test_ubah_manga(self):
    #     add_manga("Test Manga", "ongoing", 1, 100, "2024-05-01", "2024-05-01", "Great manga", ["action", "adventure"])
    #     ubah_manga("Test Manga", "Updated Manga", "finished", 2, 200, "2024-06-01", "2024-06-01", "Even better", ["comedy", "drama"])
    #     self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Updated Manga",))
    #     manga = self.c.fetchone()
    #     self.assertIsNotNone(manga)
    #     self.assertEqual(manga[0], "Updated Manga")
    #     self.assertEqual(manga[1], "finished")
    #     self.assertEqual(manga[3], 200)
    #     self.c.execute("SELECT genre FROM genre_manga WHERE judul = ?", ("Updated Manga",))
    #     genres = self.c.fetchall()
    #     self.assertEqual(len(genres), 2)

    # def test_get_all_manga(self):
    #     add_manga("Manga 1", "ongoing", 1, 100, "2024-05-01", "2024-05-01", "Great manga", ["action", "adventure"])
    #     add_manga("Manga 2", "finished", 2, 200, "2024-05-02", "2024-05-02", "Nice manga", ["comedy", "drama"])
    #     mangas = get_all_manga()
    #     self.assertTrue(len(mangas) >= 2)

    # def test_get_genre_by_judul(self):
    #     add_manga("Manga 1", "ongoing", 1, 100, "2024-05-01", "2024-05-01", "Great manga", ["action", "adventure"])
    #     genres = get_genre_by_judul("Manga 1")
    #     self.assertEqual(genres, "action, adventure")

    # def test_delete_manga(self):
    #     add_manga("Manga to delete", "ongoing", 1, 100, "2024-05-01", "2024-05-01", "Not bad", ["action"])
    #     delete_manga("Manga to delete")
    #     self.c.execute("SELECT * FROM Manga WHERE judul = ?", ("Manga to delete",))
    #     manga = self.c.fetchone()
    #     self.assertIsNone(manga)
    #     self.c.execute("SELECT * FROM genre_manga WHERE judul = ?", ("Manga to delete",))
    #     genre = self.c.fetchone()
    #     self.assertIsNone(genre)

if __name__ == "__main__":
    unittest.main()
