import autoDirectedHierAndDD as dd
import autoPieAndHistHier as hh
import autoTableAndPivotHier as ph
import autoTimeHistAndHistSegmented as hist_hist
import ddTable as ddt
import ddPivot as ddp
import ddPie as ddpie

_DirectedHierAndDD = dd.DirectedHierAndDD()
_DirectedHierAndDD.test_case()

_PieAndHistHier = hh.PieAndHistHier()
_PieAndHistHier.test_case()

_TimeHistAndHistSegmented = hist_hist.TimeHistAndHistSegmented()
_TimeHistAndHistSegmented.test_case()

_PivotAndTableHier = ph.PivotAndTableHier()
_PivotAndTableHier.test_case()

_ddtable = ddt.ddTable()
_ddtable.test_case()

_ddpivot = ddp.ddPivot()
_ddpivot.test_case()

__ddpie = ddpie.ddPie()
__ddpie.test_case()
