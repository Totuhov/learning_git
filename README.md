# Git & Github Tutorial

## Begriffe

Verzeichnis – Ordner
Terminal oder Befehlszeile – Schnittstelle für Textbefehle
CLI – Befehlszeilenschnittstelle
cd – Verzeichnis wechseln
Code-Editor – Textverarbeitungsprogramm zum Schreiben von Code
Repository – Projekt oder der Ordner/Ort, in dem Ihr Projekt gespeichert ist
Git – Tool, das die Änderungen am Code im Laufe der Zeit verfolgt
Github – Eine Website zum Online-Hosten Ihrer Repositories

## Git Befehle

clone – Ein Repository, das irgendwo gehostet wird, wie zum Beispiel auf Github, in einen Ordner auf deinem lokalen Rechner kopieren.
add – Deine Dateien und Änderungen in Git verfolgen.
commit – Deine Dateien in Git speichern.
push – Git-Commits auf ein entferntes Repository hochladen, wie zum Beispiel auf Github, Gitlab, etc.
pull – Änderungen von einem entfernten Repository auf deinen lokalen Rechner herunterladen, das Gegenteil von push.

## Install Git on Linux - Debian / Ubuntu (apt-get)

-   Install LINUX on WSL
    windows command line öffnen:
    wsl –list –online
    wsl –install –d <Distro name>
    oder von Microsoft Store Debian herunterladen

-   Installieren Sie Git von Ihrer Shell aus mit apt-get:
    sudo apt-get update
    sudo apt-get install git
-   Überprüfen Sie durch Eingabe, ob die Installation erfolgreich war
    git --version
    git version 2.9.2

## Neues Repository erstellen

-   In github eine neue repo erstellen
-   SSH Schlüssel in github.com erstellen
-   In VS Code Terminal öffnen in einem freiausgewählte datei wo das Repo dupliciert werden soll
    git clone git@github.com:Totuhov/learning_git.git
    cd learning_git
-   Alle Dateien und Verzeichnisse anzeigen, auch versteckte
    ls –la (nicht funktionieren)
    ls –Hidden für VS Code Terminal
