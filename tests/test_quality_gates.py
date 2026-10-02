from dataclasses import dataclass

@dataclass
class Gate:
    name: str
    passed: bool
    reason: str

def evaluate_gates(gates):
    return all(g.passed for g in gates)

def test_all_quality_gates_pass():
    gates = [
        Gate("api", True, "contract checks passed"),
        Gate("ui", True, "critical workflow passed"),
        Gate("security", True, "no credential in source"),
    ]
    assert evaluate_gates(gates)

def test_failed_gate_blocks_release():
    gates = [Gate("api", True, ""), Gate("ui", False, "workflow failed")]
    assert not evaluate_gates(gates)
