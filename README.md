# Ping Pong Spiel in Python

Dies ist ein klassisches Ping-Pong-Spiel, das mit Python und der Pygame-Bibliothek entwickelt wurde. Es war ein Lernprojekt, um grundlegende Konzepte der Spieleentwicklung, eine einfache KI und die Anbindung an eine Datenbank zu erlernen.

---

## ✨ Features

- Spiele gegen einen computergesteuerten Gegner.
- Dynamisches Punktesystem.
- Lokale Highscore-Liste, die in einer Datenbank gespeichert wird.
- Soundeffekte für Spielaktionen.
- Ein sauberes Retro-Design.

---

## 💻 Technologie-Stack

- **Sprache:** Python
- **Bibliothek:** Pygame (für die Spielelogik und Grafik)
- **Datenbank:** SQLite (für die Speicherung der Highscores)

---

## 🚀 Meilensteine der Entwicklung

Dieses Projekt wurde schrittweise in den folgenden Meilensteinen entwickelt:

### Meilenstein 1: Grundlagen und Spielobjekte

- Einrichtung der Entwicklungsumgebung mit Python und Pygame.
- Erstellung eines leeren Spielfensters.
- Zeichnen der statischen Spielobjekte: Spieler-Schläger und Ball.

### Meilenstein 2: Bewegung und Steuerung

- Implementierung der Spielersteuerung über die Pfeiltasten.
- Erstellung einer automatischen Ballbewegung.
- Kollisionserkennung des Balls mit den oberen und unteren Wänden.

### Meilenstein 3: Spielmechanik und Gegner-KI

- Hinzufügen eines computergesteuerten Gegners auf der linken Seite.
- Entwicklung einer einfachen KI, bei der der Gegner dem Ball folgt.
- Kollisionserkennung zwischen dem Ball und beiden Schlägern.

### Meilenstein 4: Punkte und Spielzustand

- Einführung von Variablen zur Zählung der Punkte.
- Anzeige des aktuellen Spielstands auf dem Bildschirm.
- Definition einer "Game Over"-Bedingung beim Erreichen einer bestimmten Punktzahl.

### Meilenstein 5: Highscore-System und Feinschliff

- Anbindung an eine SQLite-Datenbank zur dauerhaften Speicherung von Highscores.
- Implementierung eines Menü- und Game-Over-Bildschirms.
- Möglichkeit für den Spieler, nach einem Highscore seinen Namen einzugeben.
- Visuelle und auditive Verbesserungen wie Soundeffekte und ein neues Farbschema.

---

## ⚙️ Installation & Start

Um das Spiel lokal auszuführen, befolge diese Schritte:

1.  **Klone das Repository:**

    ```bash
    git clone [https://github.com/zGrantelbart/projekt.git](https://github.com/zGrantelbart/projekt.git)
    cd DEIN-REPOSITORY-NAME
    ```

2.  **Installiere die Abhängigkeiten:**
    (Stelle sicher, dass Python 3 installiert ist)

    ```bash
    pip install pygame
    ```

3.  **Starte das Spiel:**
    ```bash
    python main.py
    ```
    Das Spiel startet im Menü. Drücke die Leertaste, um zu spielen!

---

## 📜 Credits & Danksagungen

_Hier ist der Platz, um die Credits für Sounds und Schriftarten einzutragen, wie wir es besprochen haben._

**Beispiel:**

- **Soundeffekte:** "Sci-Fi Blip" von ArtistName (Quelle) - lizenziert unter CC BY 3.0.
- **Schriftart:** "Press Start 2P" von CodeMan38 (Google Fonts) - lizenziert unter der SIL Open Font License.
