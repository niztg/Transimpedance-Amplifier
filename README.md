# Transimpedance Amplifier Design for Optical Power Meter

A complete front-end TIA design for a benchtop optical power meter, targeting 1 MHz bandwidth with a 10 kΩ transimpedance gain.

## Contents

- `Transimpedance_Amplifier_Design.md` — full design report including transfer function derivation, noise analysis, op-amp selection, and LTspice simulation results
- `tia.asc` — LTspice schematic
- `gbwcalc.py` — Python script for GBW back-calculation from simulated bandwidth
- Figures 1—5 — circuit diagrams and simulation plots referenced in the report

## Summary

The design uses a Hamamatsu S5971 PIN photodiode and the LTC6268 FET-input op-amp, selected over the OPA657 based on noise analysis. The closed-loop transfer function is derived from first principles, yielding a second-order system with natural frequency governed by the op-amp GBW and input capacitance. Johnson noise from the feedback resistor dominates the noise floor at 1.29 pA/√Hz across the target bandwidth.

LTspice simulation confirms the expected 80 dBΩ passband and second-order rolloff. Hardware validation is planned.

## Status

Simulation complete. Hardware validation pending.
