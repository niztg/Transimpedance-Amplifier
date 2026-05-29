<!-- slide -->

# Transimpedance Amplifier Design for Optical Power Meter

## 1. Application

This application, a transimpedance amplifier (TIA), is designed as the front-end amplifier for a benchtop optical power meter measuring modulated laser sources up to 1 MHz in frequency. It uses a Hammatsu S5971 silicon PIN photodiode in order to convert incident light into current, which is subsequently converted into a voltage. This voltage can then be digitized by an ADC for further applications.

The TIA front-end is made necessary by the presence of the photodiode's parasitic capacitance. If the photodiode was run to ground through a resistor a low-pass filter would be formed, as depicted in Fig. 1.

Performing KCL, and taking Ohm's Law across the resistor $R_f$:

$$ V_{out} = R_f (I_{in} - sC_{in}V_{out})$$

$$V_{out} = R_f I_{in} - sR_f C_{in} V_{out}$$

$$V_{out} (1 + s R_f C_{in}) = R_fI_{in}$$

$$ \frac{V_{out}}{I_{in}} = \frac{R_f}{1+sR_fC_{in}}$$

$$ \boxed{\frac{V_{out}}{I_{in}} = \frac{R_f}{1 + \frac{s}{{(1/R_fC_{in})}}}} \quad (1)$$

From the transfer function given by Eqn. (1), we can directly read off the LPF's cornering frequency as $\omega_c = \frac{1}{R_f C_{in}}$ and its DC gain as $R_f$. Therefore, if we decrease $R_f$ in order to increase the cornering frequency, we decrease the DC gain. This tension is what ultimately necessitates a device such as the TIA.

## 2. Design Specifications

| Parameter | Value | Justification |
|---|---|---|
| Transimpedance gain $R_f$ | 10 kΩ | With an expected current of 10 $\mu A$, this leads to an expected voltage output of 10 mV |
| Input capacitance $C_{in}$ | 3 pF | S5971 datasheet, $V_R = 10$ V |
| Target bandwidth $f_{-3dB}$ | 1 MHz | The device seeks to measure modulated laser sources up to 1 MHz |
| Required op-amp GBW | 188 MHz | Derived below |

## 3. Bandwidth Derivation

The circuit diagram of the TIA is depicted in Fig. 2.

The op-amp is modelled as a single-pole system with open-loop gain given in the s-domain by:

$ \boxed{A(s) = \frac{\omega_{GBW}}{s}} \quad (2) $

Where $\omega_{GBW} = 2\pi (GBW)$. This approximation holds at frequencies that significantly exceed the op-amp's internal cornering frequency, typically on the scale of a few Hz.

Performing KCL at the inverting input node:

$$-I_{in} + sC_{in}V_- + \frac{V_--V_{out}}{R_f} = 0 \quad(3)$$

Applying the definition of the open-loop gain of an op-amp:

$$ V_{out} = A(s) (V_+ - V_-)$$

$$ \boxed{V_- = \frac{V_{out}}{A(s)}} \quad (4) $$

Substituting Eqn. 4 into Eqn. 3 and simplifying:

$$ -I_{in} +sC_{in}(\frac{-V_{out}}{A(s)}) + \frac{(\frac{-V_{out}}{A(s)}) \, - \, V_{out}}{R_f} = 0$$

$$ -I_{in} = V_{out}(\frac{sC_{in}}{A(s)} + \frac{\frac{1}{A(s)}+1}{R_f})$$

$$ -I_{in} = V_{out} (\frac{sC_{in}R_f \, +\, 1 \, +\, A(s)}{A(s)R_f}) $$

Substituting Eqn. 2 for $A(s)$:

$$-I_{in} = V_{out} (\frac{sC_{in}R_f \, + \, 1 \, + \, \omega_{GBW}/s}{R_f \omega_{GBW} /s})$$

$$-I_{in} = V_{out} (\frac{s^2C_{in}R_f \, + \, s + \, \omega_{GBW}}{R_f\omega_{GBW}})$$

$$\frac{V_{out}}{I_{in}} = -\frac{\omega_{GBW}R_f}{s^2C_{in}R_f \, + \, s \, + \, \omega_{GBW}}$$

$$\boxed{\frac{V_{out}}{I_{in}} = - \frac{1}{C_{in}R_f} (\frac{\omega_{GBW}R_f}{s^2 \, + \, s \, / \, C_{in}R_f \, + \, \omega_{GBW} \, / \, C_{in}R_f})} \quad (5)$$

The second-order transfer function given by Eqn. 5 has an associated natural angular frequency, $\omega_n$ given by:

$$ \omega_n^2 = \frac{w_{GBW}}{C_{in}R_f}$$

$$ \omega_n = \sqrt{\frac{\omega_{GBW}}{R_fC_{in}}}$$

$$f_n = \frac{1}{2\pi}\sqrt{\frac{2\pi(GBW)}{R_fC_{in}}}$$

$$\boxed{f_n = \sqrt{\frac{GBW}{2\pi R_fC_{in}}}} \quad (6)$$

At last, Eqn. 6 gives the closed-loop bandwidth,valid as an approximation for the $-3$ dB frequency when the damping ratio is close to $1/\sqrt{2}$. 

## 4. Op-Amp GBW Requirement

Rearranging for GBW and substituting the design values:

$$GBW = f_n^2 2\pi R_f C_{in}$$

$$GBW = (10^6)^22\pi( 10^4)(3\times10^{-12} )\approx 188 \text{ MHz}$$

The chosen op-amp must have a GBW of at least 188 MHz. This figure drives the
parametric search in the following stage.

## 5. Noise Analysis

[This section comes after Stage 1 is complete — to be filled in]

The three noise contributors are:

- Johnson noise from $R_f$: $\sqrt{4kT/R_f}$
- Op-amp input voltage noise referred to input
- Op-amp input current noise

## 6. Op-Amp Selection

[To be filled in after Stage 2 — parametric search, candidate comparison table, final choice]

## 7. Simulation Results

[To be filled in after Stage 3 — AC sweep, noise simulation, stability, transient]

## 8. Design Trade-off Analysis

[To be filled in after Stage 4 — $R_f$ sweep across 1 kΩ, 10 kΩ, 100 kΩ]

## 9. Conclusions

[To be filled in last]