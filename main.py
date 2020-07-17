import autoDirectedHierAndDD as dd
import autoPieAndHistHier as hh
import autoTableAndPivotHier as ph
import autoTimeHistAndHistSegmented as hist_hist

_DirectedHierAndDD = dd.DirectedHierAndDD()
_DirectedHierAndDD.test_case()

_PieAndHistHier = hh.PivotAndTableHier()
_PieAndHistHier.test_case()

_TimeHistAndHistSegmented = hist_hist.TimeHistAndHistSegmented()
_TimeHistAndHistSegmented.test_case()

_PivotAndTableHier = ph.PivotAndTableHier()
_PivotAndTableHier.test_case()
