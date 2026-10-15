How is Image Pattern connects to Sound Timbre
========


Simple Pattern Test
--------

Used simple pattern such as vertical stripes or gradient rectangle.

* Vertical strip triggers frequency modulation.
  * When it comes to less than 32 px, the sound start to feel like alarm sound.
  * In all 16px stripe 2 colour, the sound is the average of two different colour.
    * Should better have a diff that is `< 32` in colour value.
    * Otherwise the sound will be hard to have a center-freq when hearing.
  * When it is more than 32 px, it sounds like a sound-effect (almost no center-freq),
     which means, the freq does not matter too much.
* Gradient is as expected, glide sound.


Mixed Pattern Test
--------

* For sine/square/triangle/sawtooth FM, although spectrum shows different shape,
   they did not vary so much for hearing.
* Dual-sine is somehow different from sine/square/triangle/sawtooth.
  Still, it is hard to create easy-to-feel-the-different FM.
* For smooth noise, since the granularity is lower than sine/square/triangle/sawtooth FM,
   it has a smoother timbre.
  Quite like the sound made by the tunnel image (in `examples/game_pic/tunnel.png`).
* In RGB combo, the difference of those FM-ed result could be heard.
* Do supercollider-level FM on SSTV sonification seems to be hard.