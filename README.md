# Pavlo - Ammattikoulun TiVi-alan ohjelmointi loppu projekti. 
Simppeli 2D peli Pythonillä (PyGame kirjasto on kaytössä) 


## Kuinka pelata

1. **Asenna Python** tietokoneellesi, jos sitä ei ole vielä asennettu.  
   - Jos käytät Debiania tai siihen perustuvia jakeluita (kuten Ubuntu tai Mint), avaa pääte ja kirjoita:
     ```
     sudo apt update
     sudo apt install python
     ```
   - Jos käytät Archia tai siihen perustuvia jakeluita:
     ```
     sudo pacman -S python
     ```
   - Jos käytät openSUSEa:
     ```
     sudo zypper install python
     ```
    - Jos käytät Fedora
    ```
    sudo dnf install python
    ```
   - Jos käytät muuta Linux-jakelua, käytä sen omaa pakettienhallintaa.
   - Jos käytät Windowsia — ~~Asenna Arch Linux ja asenna Python pacmanilla~~  
     Lataa ja asenna Python viralliselta sivustolta: [https://www.python.org/](https://www.python.org/)

   Jos Python on jo asennettu — hyvä! Voit siirtyä seuraavaan kohtaan.

2. **Asenna Git**, jos sitä ei ole jo asennettu.  
   Käytä samaa asennusprosessia kuin yllä — pakettienhallinta Linuxilla tai virallinen sivusto Windowsilla: [https://git-scm.com/](https://git-scm.com/)

3. **Kloonaa pelin repository.**  
   Avaa pääte (Linux: Terminal/Konsole, Windows: Command Prompt tai PowerShell), siirry kansioon johon haluat asentaa pelin:
   ```
   cd polku/kansioon
   ```
   Kloonaa repository:
   ```
   git clone https://github.com/PlagueFencer/ICT-Programming-Final-Project-Pavlo.git
   ```
   Siirry pelin kansioon:
   ```
   cd goosegame
   ```
4. **Asenna pygame:**
    Jos olet Linuxillä:
    ```
    pip3 install pygame
    ```
    Jos olen Windowsillä:
    ```
    pip install pygame
    ```
5. **Käynnistä peli:**
    Jos olet Linuxillä:
    ```
    python3 main.py
    ```
    Jos olen Windowsillä:
    ```
    python main.py
    ```

6. **Pelaa!**