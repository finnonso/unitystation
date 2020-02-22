using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Instrument : MonoBehaviour, ICheckedInteractable<HandApply>
{
	struct MidiNote
	{
		byte Note;
		char Acc;
		byte Duration;

		MidiNote(byte note, char acc = '\u0000', byte duration = 4)
		{
			Note = note;
			Acc = acc;
			Duration = duration;
		}
	}

	struct MidiSong
	{
		public short BPM;
		public MidiNote[][] Beats;

		MidiSong(short bpm, MidiNote[][] beats)
		{
			BPM = bpm;
			Beats = beats;
		}
	}


	public const string PIANO_DEBUG_TRACK = @"BPM: 200
D5,Db-E5,C5-Gb5,B4-Gn,C-A5,D-Bb5,Dn-Bn/2,D-B/2
G3-D-B,G-E-B,G-G4-F5-B/0,5,G5,C4-G-E6,G4,C5
B3-Gb5-Eb,Gn4,B4,C4-G5-En,G4,C5,E4/2,G5/2,G4-A/2
B5/2,C-C6/2,D6/2,C4-G5-E6,G4,C5,B3-Gb5-Eb,Gn4
B4-A-F6,C4-G5-En,G4,C5,E4,G,C/2,G5/2,D4-F5-D6,G4,B
Db4-E5-D6,Gb,Bb,Dn4-F-D6,Gn,Bn,G3/2,G5/2,G4-A/2
B5/2,B4-C6/2,Db/2,Dn4-F-D6,G,B,B3-B4-G5,G4,B-A-F6
C4-G5-E6,G4,C5,G3,G4,C/2,G5/2,C4-E-G6,G4,E5
B3-D-G6,G4,D5,A3-Db6-G6,A4,D5,D4-G,G4-A6,E/2,G6/2
Dn-D6-F,A4,F5,Db4-D6-F6,A,F5,C-C6-F6,A,F5,B-F6
G4-G6,F5/2,F6/2,C3-E-E6,G4,E5,G3-F5-A5,G4-G5-B5
G4-B-F6,G3-G4-B-E6/2,G3-G4-B-E/2,G3-G4-B-E/0,67
B3-F5-B5/2,C-C4-E5-C6/0,33,Dn5,Db-E,C5-Gb5,B4-Gn
C-A,D-Bb5,Dn-Bn/2,D-B/2,G3-D-B,G-E-B,G-G4-F-B/0,5
G5,C4-G-E6,G4,C5,B3-Gb5-Eb,Gn4,B4,C4-G5-En,G4,C5
E4/2,G5/2,G4-A/2,B5/2,C-C6/2,D6/2,C4-G5-E6,G4,C5
B3-Gb5-Eb,Gn4,B4-A-F6,C4-G5-En,G4,C5,E4,G,C/2,G5/2
D4-F5-D6,G4,B,Db4-E5-D6,Gb,Bb,Dn4-F-D6,Gn,Bn,G3/2
G5/2,G4-A/2,B5/2,B4-C6/2,Db/2,Dn4-F-D6,G,B
B3-B4-G5,G4,B-A-F6,C4-G5-E6,G4,C5,G3,G4,C/2,G5/2
C4-E-G6,G4,E5,B3-D-G6,G4,D5,A3-Db6-G6,A4,D5,D4-G
G4-A6,E/2,G6/2,Dn-D6-F,A4,F5,Db4-D6-F6,A,F5
C-C6-F6,A,F5,B-F6,G4-G6,F5/2,F6/2,C3-E-E6,G4,E5
G3-F5-A5,G4-G5-B5,G4-B-F6,G3-G4-B-E6/2,G3-G4-B-E/2
G3-G4-B-E/0,67,B3-F5-B5/2,C-C4-E5/I";

	// Start is called before the first frame update
	void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

	public bool WillInteract(HandApply interaction, NetworkSide side)
	{
		if(!Validations.CanApply(interaction, side)) return false;

		return true;
	}

	public void ServerPerformInteraction(HandApply interaction)
	{


		SoundManager.PlayNetworkedAtPos("PianoAb#", interaction.TargetObject.WorldPosServer());
	}

	private MidiSong ParseString(string sheet)
	{
		string[] lines = sheet.Split(new[] { "\r\n", "\r", "\n" }, StringSplitOptions.None);
		return new MidiSong();
	}
}
