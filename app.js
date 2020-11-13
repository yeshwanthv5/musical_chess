var MidiPlayer = require('midi-player-js');

// Initialize player and register event handler
var Player = new MidiPlayer.Player(function(event) {
	console.log(event);
});

// Load a MIDI file
Player.loadFile('./data/changes_F_88bpm_dripchord.com/changes_F_88bpm_dripchord.mid');
Player.play();

Player.on('fileLoaded', function() {
    // Do something when file is loaded
    console.log("Player Loaded")
});

Player.on('playing', function(currentTick) {
    // Do something while player is playing
    // (this is repeatedly triggered within the play loop)
    console.log("Playing clip")
});

Player.on('midiEvent', function(event) {
    // Do something when a MIDI event is fired.
    // (this is the same as passing a function to MidiPlayer.Player() when instantiating.
    console.log("Halftime reminder")
});

Player.on('endOfFile', function() {
    // Do something when end of the file has been reached.
    console.log("End of file")
});