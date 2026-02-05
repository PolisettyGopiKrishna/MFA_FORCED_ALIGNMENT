1. Objective

The goal of this assignment was to perform forced alignment between speech audio and its corresponding transcript using the Montreal Forced Aligner (MFA). Forced alignment determines the start and end times of each word and phoneme in an audio recording.

2. Dataset Preparation

The provided dataset contained:

Audio files in WAV format

Corresponding transcript files

All transcripts were cleaned and converted into MFA-compatible .lab files by:

Converting text to uppercase

Removing punctuation

Ensuring one utterance per file

This step ensures proper matching between audio and transcription.

3. Pronunciation Dictionary

The pretrained MFA dictionary english_us_arpa was selected.
However, some words in the transcripts were not present in the dictionary and were considered Out Of Vocabulary (OOV).

To handle OOV words:

All words from transcripts were extracted

Missing words were identified

A G2P (grapheme-to-phoneme) model would normally generate pronunciations

These pronunciations would be added to create a custom.dict

This ensures every word has a phonetic representation required for alignment.

4. Forced Alignment Process

The alignment step would normally be performed using:

mfa align dataset/ custom.dict english_us_arpa aligned_output_fixed/


This process uses an acoustic model to align audio with phoneme sequences derived from the pronunciation dictionary.

5. Expected Output

The alignment produces Praat TextGrid files that can be opened in Praat.

Each TextGrid contains:

Word Tier
Segments showing each word from the transcript aligned with its time boundaries.

Phoneme Tier
Each word further divided into ARPAbet phonemes (e.g., W AA N T IH D for "WANTED").

These tiers allow visual inspection of speech timing and pronunciation alignment.

6. Installation Issue

The forced alignment could not be executed on the local Windows system due to dependency issues while installing MFA. MFA requires Kaldi-based compiled components (_kalpy module), which failed to install without conda-forge binaries.

Despite this, the following steps were fully completed:

✔ Dataset formatting
✔ Transcript normalization
✔ OOV word detection
✔ Dictionary preparation pipeline
✔ Alignment command setup

7. Learning Outcomes

Through this assignment, the following concepts were understood:

How forced alignment links audio and phonetic transcription

The importance of pronunciation dictionaries

Handling Out Of Vocabulary words using G2P

Structure and purpose of Praat TextGrid files

Practical workflow of Montreal Forced Aligner
