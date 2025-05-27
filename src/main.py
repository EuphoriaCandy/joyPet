#!/usr/bin/env python3
# If you run linux, the above informs that this file is to be run with python

"""joyPet's main function"""
from __future__ import annotations

from guts import constants, joyPetCreator

def main() -> None:
  """joyPet main function"""
  pet1 = joyPetCreator()
  pet1.createJoyPet()

if __name__ == '__main__':
  main()