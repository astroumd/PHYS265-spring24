
# spectral lines in a MUSE dataset of NGC253

* ngc253_ha.tab - Halpha.    x=Angstrom y=arbitrary units    - this spectrum also has the two [NII] lines
* ngc253_hb.tab - Hbeta      x=Angstrom y=arbitrary units    - nice clean spectrum with one line

My advice is to use the Hbeta line.

A good model would be:

    a+b*exp(-(x-c)^2/(2*d^2)):

where

 a   baseline flux
 b   peak of gauss
 c   location of gauss
 d   with of gauss
