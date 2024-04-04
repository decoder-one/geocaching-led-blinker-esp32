#
# geocaching koordinaten blinker alle x min
# rgb led (anode) mit tageslichtschaltung auf esp32c3
# (c) 2024 by norbert ossenkopp aka futurecube @geocaching.com
# kontakt: futurecube@gmx.net
#

from machine import Pin, PWM, ADC
import time

# Definiere die Pins für die RGB-LED
led_r = PWM(Pin(5))   # GPIO Pin 5 für Rot
led_g = PWM(Pin(6))   # GPIO Pin 6 für Grün
led_b = PWM(Pin(7))   # GPIO Pin 7 für Blau

# startsequenz 10x rot blinken
def seq_startend():
    for a in range(10):
                # Grün
                set_color(1023, 0, 0)
                time.sleep(0.2)
                set_color(0, 0, 0)
                time.sleep(0.2)
    time.sleep(3)
    
# Funktion zum Einstellen der Farbe
def set_color(r, g, b):
    # Wertebereich für PWM ist 0-1023
    led_r.duty(1023 - r)
    led_g.duty(1023 - g)
    led_b.duty(1023 - b)

# pin für die photodiode
photodiode_pin = Pin(0)  # Change the pin number as per your connection

# Create an ADC object
adc = ADC(Pin(photodiode_pin))

# Set ADC range to 0-3.3V (default is 0-1.0V)
adc.atten(ADC.ATTN_11DB)

# geocaching koordinaten
number = "5012"

# grün/blau funktion
def control_led(number):
    for digit in str(number):
        digit = int(digit)
        if digit == 0:
            # blau
            set_color(0, 0, 1023)
            time.sleep(0.5)
            set_color(0, 0, 0)
            time.sleep(0.5)
        else:
            for a in range(digit):
                #print ("grün: ", digit)
                # Grün
                set_color(0, 1023, 0)
                time.sleep(0.5)
                set_color(0, 0, 0)
                time.sleep(0.5)
        time.sleep(2)                     

# hauptschleife
while True:
    
    # led komplett ausschalten 
    led_r.deinit()
    led_g.deinit()
    led_b.deinit()
    
    # Read analog value from the photodiode
    analog_value = adc.read()

    # Convert analog value to a light intensity value
    # You might need to calibrate this conversion based on your photodiode's specifications
    light_intensity = analog_value

    # Print the light intensity value
    print("Light Intensity:", light_intensity)

    if light_intensity > 3000:  # Annahme: Schwellenwert für Tageslicht
        
        led_r.init()
        led_g.init()
        led_b.init()
        
        seq_startend() # start signal
        control_led(number) #ko blinker
        seq_startend()  # ende signal
    
    # led komplett ausschalten 
    led_r.deinit()
    led_g.deinit()
    led_b.deinit()
    
    # 10 min Pause bis nächster Durchlauf
    time.sleep(600) #standardwert 600 für 10 min
    
