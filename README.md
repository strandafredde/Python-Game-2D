# Ett 2D spel skrivit i Python

## Översikt
Detta är ett 2D spel som är skrivt i Python med hjälp av bibliotiket **_Pygame_**. Målet med spelet är att utforska kartan och samla saker till en viss NPC.

## Bibliotek och Verktyg

För att utveckla detta spel krävdes följande bibliotek och verktyg:

### Bibliotek

1. **Pygame**
   - **Beskrivning:** Biblotiket som används för det mesta inom spelet exemeplvis för skärmen, rörelse och kollisionen
   - **Installation:**
     ```bash
     pip install Pygame
     ```
     
2. **Pytmx**
   - **Beskrivning:** Biblotiket som används för att läsa in en tmx fil som skapas i programet **Tiled**. 
   - **Installation:**
     ```bash
     pip install pytmx
     ```
     
### Verktyg

1. **[Tiled](https://www.mapeditor.org/)**
   - **Beskrivning** Tiled är ett program som används för att skapa en tiledmap som sparas i en tmx fil som sedan läses in med hjälp av Pytmx. Kort beskrivet så är en tmx fil en textfil fylld av olika siffror
     där siffrorna representerar olika texturer. Exempelvis så kan 1 representera en gräs textur och 2 kan representera vatten med mera.
   - **Installation** **[Länken](https://www.mapeditor.org/)** och tryck på **Download** knappen
