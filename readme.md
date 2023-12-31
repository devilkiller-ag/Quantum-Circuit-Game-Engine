![Quantum Circuit Game Engine](https://github.com/devilkiller-ag/Quantum-Circuit-Game-Engine/assets/43639341/dd998bca-c47b-44fd-8ed2-19724cbc57a2)

<h1>Quantum Circuit Game Engine for Pygame-based Quantum Games</h1>

This is a Quantum Circuit Game Engine for integrating Quantum Circuits into your Pygame-based quantum game. You can use it simply by creating an object of the `QuantumCircuitGrid` class stored in the `quantum_circuit.py` file.

This Quantum Circuit was originaly created for the **QPong Game** developed by <a href='https://huangjunye.github.io/' target='_blank'>Junye Huang</a> in the <a href="https://www.youtube.com/playlist?list=PLOFEBzvs-VvodTkP_rfrs3RWdeWE9aNRD" target='_blank'>12 Days of Qiskit Program</a>. I created this engine by re-writing its code located <a href='https://github.com/QPong/qpong-livestream' target='_blank'>here</a> to make it modular and abstract for easy use with any quantum game. 

The features I have included are:
- Modular and Abstract Code.
- All configurations in one place in the `config.py` file.
- Developers can create a Quantum Circuit for any number of qubit/wires and circuit width (max. number of gates which can be applied in a wire) of their choice. 
- Easy to change UI by replacing color configs and graphics for gates with those of your choice. 
- Easy to change the size of Quantum Circuit by adjusting `QUANTUM_CIRCUIT_TILE_SIZE`, `GATE_TILE_WIDTH`, and `GATE_TILE_HIEGHT` in the `config.py` file.
- Easily change controls by changing keys in the `handle_input()` method of the `QuantumCircuitGrid` class.


**If this project is helpful for you or you liked my work, consider supporting me through <a href="https://ko-fi.com/jaisarita" target="_blank">Ko.fi🍵</a>. Also, kindly consider giving a star to this repository.😁**

<!-- ------------------------------------------------------------------------- -->
<h2>About me</h2>

I am Ashmit JaiSarita Gupta, an Engineering Physics Undergraduate passionate about Quantum Computing, Machine Learning, UI/UX, and Web Development. I have worked on many projects in these fields, participated in hackathons, and am a part of great organizations in these fields. You can explore more about me, my work, and my experience at various organizations through my portfolio website: <a href='https://jaisarita.vercel.app/' target="_blank">https://jaisarita.vercel.app/</a> ☄️

<!-- ------------------------------------------------------------------------- -->
<h2>Installation</h2>

```bash
pip install qcge
```
<!-- ------------------------------------------------------------------------- -->
<h2>Usage</h2>

You can use it simply by creating an object of the `QuantumCircuitGrid` class stored in the `quantum_circuit.py` file. The constructor of `QuantumCircuitGrid` takes these values as argument:

- `position`: Position of the Quantum Circuit in the game window.
- `num_qubits`: Number of Qubits in the Quantum Circuit.
- `num_columns`: Circuit width (max. number of gates which can be applied in a wire) of their choice.
- `tile_size` (Optional, Default Value = 36): Size of single tile unit of the Quantum Circuit. It is the square area containing single gate in the quantum circuit.
- `gate_dimensions` (Optional Default Value = [24, 24]): [Width, Height] of quantum gates.
- `background_color` (Optional Default Value = '#444654'): Background Color of the Quantum Circuit.
- `wire_color` (Optional Default Value = '#ffffff'): Color of Quantum Wire in the Quantum Circuit.
- `gate_phase_angle_color` (Optional Default Value = '#97ad40'): Color to represent phase angle of Rotation Gates.

You can run your quantum circuit on BasicAer Simulator by using this function:
```python
def run_quantum_circuit(self, quantum_circuit):
        simulator = BasicAer.get_backend("statevector_simulator")
        quantum_circuit.measure_all()
        transpiled_circuit = transpile(quantum_circuit, simulator)
        counts = simulator.run(transpiled_circuit, shots=1).result().get_counts()
        measured_state = int(list(counts.keys())[0], 2)
        return measured_state
```

<!-- ------------------------------------------------------------------------- -->
<h2>Configurations</h2>

All the configurations for Quantum Circuit can be done in the `config.py` file. The controls of the quantum circuit in the game can be changed from the defaults mentioned below by changing keys in the `handle_input()` method of the `QuantumCircuitGrid` class.

- You can change the size of Quantum Circuit by passing optional parameters `tile_size`, and `gate_dimensions` (= [GATE_TILE_WIDTH, GATE_TILE_HIEGHT]) to the `qcge.QuantumCircuitGrid` class as parameters.
- You can change UI colors by passing optional parameters `background_color`, `wire_color`, and `gate_phase_angle_color` to the `qcge.QuantumCircuitGrid` class as parameters.

Default values of these optional parameter are:
```python
tile_size = 36
gate_dimensions = [24, 24]
background_color = '#444654'
wire_color = '#ffffff'
gate_phase_angle_color = '#97ad40'
```

<!-- ------------------------------------------------------------------------- -->
<h2>Game Controls for Building Quantum Circuit</h2>

- **W, A, S, D Keys:** Move the "Circuit Cursor" in the Quantum Circuit to the place where you want to add a gate in the circuit.
- **Backspace Key:** Remove the gate present at the Circuit Cursor.
- **Delete Key:** Clear the Quantum Circuit, i.e., remove all gates from the Quantum Circuit.
- **X Key:** Add X Gate to the quantum circuit.
- **Y Key:** Add Y Gate to the quantum circuit.
- **Z Key:** Add Z Gate to the quantum circuit.
- **H Key:** Add H Gate to the quantum circuit.
- **C, R, E Keys:** Press **C Key** to convert the X, Y, Z, or H gates into CX, CY, CZ, and CH gates respectively, and then press **R Key** and **F Key** to the control to qubit above or below respectively.
- **Q and E Keys:** To convert X, Y, and Z into RX, RY, and RZ gates respectively. **Q Key** decreases the rotation angle by π/8 and **E Key** increases the rotation angle by π/8.

<!-- ------------------------------------------------------------------------- -->
