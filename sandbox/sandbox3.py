# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
###############################################################################
# Handlers for Buttons in the Sound System.
###############################################################################
def handle_beep(mqtt_sender, number_entry, frequency_entry):
    print("Beeping", number_entry.get(), "times")
    mqtt_sender.send_message("beep_n_times", [number_entry.get(), frequency_entry.get()])

def handle_tone(mqtt_sender, duration_entry, frequency_entry):
    print('Playing a tone at', frequency_entry.get(), 'for', duration_entry.get(), 'seconds')
    mqtt_sender.send_message("play_a_tone_at_frequency_for_duration", [duration_entry.get(), frequency_entry.get()])

def handle_phrase(mqtt_sender, phrase_entry):
    print('Saying', phrase_entry.get())
    mqtt_sender.send_message('speak_a_phrase', [phrase_entry.get()])
