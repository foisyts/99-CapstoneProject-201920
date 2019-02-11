# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

# Set the Button callbacks:
beep_button["command"] = lambda: handle_beep(mqtt_sender, number_entry, frequency_entry)
tone_button["command"] = lambda: handle_tone(mqtt_sender, duration_entry, frequency_entry)
phrase_button["command"] = lambda: handle_phrase(mqtt_sender, phrase_entry)
