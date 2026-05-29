import numpy as np

GBW = 500e6
Cin = 3.45e-12
en = 4.3e-9
in_ = 5.5e-15
k = 1.38e-23
T = 300
f = 1e6

Rf_values = [1e3, 10e3, 100e3]

print(f"{'Rf':>10} {'Passband (dBΩ)':>15} {'fn (MHz)':>12} {'Johnson (pA/√Hz)':>18} {'Voltage (pA/√Hz)':>18} {'Current (pA/√Hz)':>18} {'Total (pA/√Hz)':>16}")
print("-" * 115)

for Rf in Rf_values:
    passband = 20 * np.log10(Rf)
    fn = np.sqrt(GBW / (2 * np.pi * Rf * Cin))
    johnson = np.sqrt(4 * k * T / Rf)
    voltage = 2 * np.pi * f * Cin * en
    current = in_
    total = np.sqrt(johnson**2 + voltage**2 + current**2)
    
    print(f"{Rf/1e3:>9.0f}k {passband:>15.1f} {fn/1e6:>12.1f} {johnson*1e12:>18.3f} {voltage*1e12:>18.3f} {current*1e15:>17.3f}f {total*1e12:>16.3f}")