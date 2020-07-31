# ARTN-OBS Test Suite

Before performing the tests, make sure your database is up and running!

```bash
   % source etc/OBS.sh `pwd` load
   % python3.7 -m pytest -p no:warnings test_darks.py
   % python3.7 -m pytest -p no:warnings test_flats.py
   % python3.7 -m pytest -p no:warnings test_foci.py
   % python3.7 -m pytest -p no:warnings test_init.py
   % python3.7 -m pytest -p no:warnings test_instruments.py
   % python3.7 -m pytest -p no:warnings test_models.py
   % python3.7 -m pytest -p no:warnings test_non_sidereal.py
   % python3.7 -m pytest -p no:warnings test_sidereal.py
   % python3.7 -m pytest -p no:warnings test_telescopes.py
   % python3.7 -m pytest -p no:warnings test_telescopes_moon.py
   % python3.7 -m pytest -p no:warnings test_telescopes_sun.py
```
