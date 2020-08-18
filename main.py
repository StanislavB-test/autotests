import autoDirectedHierAndDD as dd
import autoPieAndHistHier as hh
import autoTableAndPivotHier as ph
import autoTimeHistAndHistSegmented as hist_hist
import ddTable as ddt
import ddPivot as ddp
import ddPie as ddpie
import ddLine as ddl
import ddDirected as ddd
import ddTimeHist as ddth
import ddSpeed as dds
import ddHist as ddh

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

_ddpie = ddpie.ddPie()
_ddpie.test_case()

_ddtimehist = ddth.ddTime_Hist()
_ddtimehist.test_case()

_ddline = ddl.ddLine()
_ddline.test_case()

_dddirected = ddd.ddDirected()
_dddirected.test_case()

_ddspeed = dds.ddSpeed()
_ddspeed.test_case()

_ddhist = ddh.ddHist()
_ddhist.test_case()
