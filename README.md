# Snake Game GUI

Ein erweitertes Snake-Spiel mit Spieler-System, Datenbank, Special-Food und verschiedenen Maps, entwickelt in Python mit Tkinter. Der Spieler steuert eine Schlange, die durch das Essen von Objekten wächst. Ziel ist es, möglichst viele Punkte zu sammeln, ohne mit sich selbst oder dem Spielfeldrand zu kollidieren.

## Funktionen 

### Spieler-System

- Spieler erstellen und speichern
- Spieler auswählen und löschen

### Score und Zeit
- Score anzeigen
- Timer anzeigen

### Gameplay
- Spielfeld mit Canvas
- Steuerung der Schlange mit Pfeiltasten
- Grundlegende Bewegung der Schlange
- Pausieren des Spiels
- Geschwindigkeit steigt im Laufe des Spiels
- Die Snake ändert beim Essen ihre Farbe
- Level / steigende Geschwindigkeit

### Maps und Hindernisse 

- Verschiedene Maps/Hindernisse
- Zufälliges Secret-Map-Event
- Bewegliche Hindernisse in der Secret Map

### Special Food System
- Einführung eines Special-Food-Systems mit verschiedenen Effekten:
  - (Blau) Punkte-Food: Gibt zusätzlich 3 Punkte
  - (Grün) Wachstums-Food: Die Schlange wächst um 1 Block
  - (Hellblau) Verlangsamungs-Food: Reduziert die Geschwindigkeit für 10 Sekunden
  - (Violett) Gift-Food: Zieht 10 Punkte vom Score ab
  - Special Food spawnt zufällig + Cooldown

## Technologien

- Python (Grundsprache)
- Tkinter (GUI / Benutzeroberfläche)
- SQLite (Datenbank für Spieler & Scores)
- Pillow (Bilder / Backgrounds)
- random (Zufallsmechaniken)
- colorsys (Farbanimationen)

## Voraussetzungen

- Python 3.13+
- Pillow 12.2.0

## Installation

1. Python installieren  
2. Projekt herunterladen oder klonen  
3. Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

4. Spiel starten:

```bash
python main.py
```

## Steuerung

- Pfeiltaste ↑  nach oben bewegen
- Pfeiltaste ↓  nach unten bewegen
- Pfeiltaste ←  nach links bewegen
- Pfeiltaste →  nach rechts bewegen
- P zum Pausieren drücken, erneut drücken zum Fortsetzen 
