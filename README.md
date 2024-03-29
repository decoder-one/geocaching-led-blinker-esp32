Geocaching Koordinatenblinker mit Tagschaltung

Hardware: "ESP32C3 Mini" Microprozessor (o.ä.) mit Micropython, Photodiode, RGB-LED (Anode), Widerstände 3x 220 Ohm, 1x 1 Kiloohm)
Software: Python

Funktion: Zur Tageszzeit (wählbarer Schwellenwert) werden alle 10 min. (wählbar) Koordinaten durch Blinksignale einer RGB-LED angezeigt. 
Grüne Blinker müssen gezählt werden und ergeben Zahlen, ein blauer Blinker stellte eine NULL dar. Zwischen den Zahlen ist eine Pause, so dass 
die Blinker/Zahlen erkennbar sind.
Eine Wiederholung findet alle 10 Minuten statt (wählbar).

Kann verwendet werden für Start/Zwischenstation eines Multis oder Mysteries.

Schaltung kann auch für andere Microprozessoren wie RP2040, Raspi Zero/Pico/etc. verwendet werden. Es können auch andere Photodioden oder 
RGB LED verwendet werden (Kathode).

Bei einer Verwendung des Codes oder Abänderung bitte ich um Mitteilung. Den Code würde ich hier einstellen.

Das Programm muss mit den benötigten librarys als main.py auf den esp32 geflasht werden und startet nach Reset automatisch.

Grüße futurecube (@geocaching.com)
