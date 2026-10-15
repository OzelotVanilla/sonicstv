How is Image Pattern connects to Rhythm Change
========


By using Different Colour Stripe
--------

Since SSTV use raster scanning and plays in the order of G-B-R,
 putting a horizontal stripe, wider than 10px,
 can make the variation of current playing frequency (main frequency).

**Drum-like sound**: Made by a low/high frequency that is off from the main frequency playing now.

* L off L (Low-freq off from low-freq main freq):
  Should better have a off more than 50 in colour value,
   hearable around 20, clear above 64.
* L off H: clearly heard as a high-drum.
* H off L: bird-like sound

In case the drum sound become melodic (since it could be perceived as a note when wider than 60px),
 a specific frequency might be set for L/H freq for drum-like sound.
Otherwise, if the frequency is varying, it could be sounds like another line of melody.

**Buzz-like sound**: Multiple horizontal off from the main freq.

This is the table summarising the experiment's result.

| Background Colour | Stripe Colour |        Stripe Number | Stripe Width |  Stripe Gap | Effect                                                                 |
| ----------------: | ------------: | -------------------: | -----------: | ----------: | :--------------------------------------------------------------------- |
|           #ff0077 |       #77ff00 |                    1 |         10px |           - | Note-choking                                                           |
|           #ff0077 |       #ffff00 |                    1 |         10px |           - | Note-choking, not in third channel                                     |
|           #ff0077 |       #77ff00 |                    2 |         10px |        10px | Note-buzzing                                                           |
|           #ff0077 |       #ffff00 |                    2 |         10px |        10px | Note-buzzing, not in third channel                                     |
|           #ff0077 |       #77ff00 |                    3 |         10px |        10px | Stronger note-buzzing                                                  |
|           #ff0077 |       #00ff77 |                    3 |         10px |        10px | Stronger note-buzzing, not in second channel                           |
|           #ff0077 |       #ffff00 |                    3 |         10px |        10px | Stronger note-buzzing, not in third channel                            |
|           #ff0077 |       #00ff77 | 6 (2 front 4 middle) |         10px | 10px & 73px | Stronger rhythmic note-buzzing, not in second channel                  |
|           #ff0077 |       #ffff00 |   6 (2 end 4 middle) |         10px | 10px & 73px | Stronger rhythmic note-buzzing, not in third channel                   |
|           #ff0077 |       #77ff00 |                    2 |         10px |        20px | Note-buzzing                                                           |
|           #ff0077 |       #ffff00 |                    2 |         10px |        20px | Note-buzzing, not in third channel                                     |
|           #ff0077 |       #77ff00 |                    3 |         10px |        20px | Stronger note-buzzing (lower-freq buzzing compared to 10px gap)        |
|           #ff0077 |       #77ff00 | 6 (2 front 4 middle) |         10px |        20px | Buzz and echoing sound effect added to main note                       |
|           #ff0077 |       #ffff00 |   6 (2 end 4 middle) |         10px |        20px | Buzz and echoing sound effect added to main note, not in third channel |
|           #ff0077 |       #77ff00 |                    1 |         30px |           - | Bird-perk feeling                                                      |
|           #ff0077 |       #ffff00 |                    1 |         30px |           - | Bird-perk feeling, not in third channel                                |
|           #ff0077 |       #77ff00 |                    2 |         30px |        10px | Bird-perk feeling (denser)                                             |
|           #ff0077 |       #ffff00 |                    2 |         30px |        10px | Bird-perk feeling, not in third channel (denser)                       |
|           #ff0077 |       #77ff00 |                    5 |         30px |        10px | Bit-crusher feeling, nerfing main note                                 |
|           #ff0077 |       #77ff00 |                    1 |         60px |           - | Crystal-like break in main note                                        |
|           #ff0077 |       #ffff00 |                    1 |         60px |           - | Crystal-like break in main note, but not in third channel              |
|           #ff0077 |       #77ff00 |                    2 |         60px |        10px | Bit-crusher feeling, nerfing main note                                 |
|           #ff0077 |       #ffff00 |                    2 |         60px |        10px | Crystal-like feeling in main note (stronger)                           |