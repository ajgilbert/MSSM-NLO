#!/usr/bin/env python
import ROOT
import imp
import json
from array import array
from bisect import bisect_left
from math import pi
wsptools = imp.load_source('wsptools', 'workspaceTools.py')


def takeClosest(myList, myNumber):
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before

def GetFromTFile(str):
    f = ROOT.TFile(str.split(':')[0])
    obj = f.Get(str.split(':')[1]).Clone()
    f.Close()
    return obj


def GetNormed(str):
    h = GetFromTFile(str)
    h.Scale(1. / h.Integral('width'))
    return h

# Boilerplate
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.RooWorkspace.imp = getattr(ROOT.RooWorkspace, 'import')
ROOT.TH1.AddDirectory(0)
ROOT.gROOT.LoadMacro("RooSpline1D.cc+")

w = ROOT.RooWorkspace('w')


masses = ["80", "90", "100", "110", "120", "130", "140", "160", "180", "200", "250", "300", "350", "400", "450", "500", "600", "700", "800", "900", "1000", "1200", "1400", "1500", "1600", "1800", "2000", "2300", "2600", "2900", "3200"]
masses_f = [float(x) for x in masses]

pname = {
    's': 'h',
    'A': 'A',
    'H': 'H'
}

tanb = {
    's': '15',
    'A': '15',
    'H': '50'
}

yt_expr = {
    's': '"cos(@0)/sin(atan(@1))", ref_alpha, ref_tanb_h',
    'H': '"sin(@0)/sin(atan(@1))", ref_alpha, ref_tanb_H',
    'A': '"1/@0", ref_tanb_A'
}

yb_expr = {
    's': '"-sin(@0)/cos(atan(@1))", ref_alpha, ref_tanb_h',
    'H': '"cos(@0)/cos(atan(@1))", ref_alpha, ref_tanb_H',
    'A': '"@0", ref_tanb_A'
}

for p in ['s', 'A', 'H']:
    P = pname[p]
    T = tanb[p]
    xsec_t_2HDM_ref = []
    xsec_b_2HDM_ref = []
    xsec_i_2HDM_ref = []
    with open('xsec.json') as jsonfile:
        xsec = json.load(jsonfile)

    for m in masses:
        xsec_t_2HDM_ref.append(xsec['%s_%s_%s_t_t' % (p, m, T)][0])
        xsec_b_2HDM_ref.append(xsec['%s_%s_%s_b_b' % (p, m, T)][0])
        xsec_i_2HDM_ref.append(xsec['%s_%s_%s_tb_tb' % (p, m, T)][0] - xsec['%s_%s_%s_t_tb' % (p, m, T)][0] - xsec['%s_%s_%s_b_tb' % (p, m, T)][0])

    w.factory('m%s[%g,%g]' % (P, min(masses_f), max(masses_f)))

    spline_xsec_t_2HDM_ref = ROOT.RooSpline1D('gg%s_t_2HDM_xsec' % (P), '', w.var('m%s' % (P)), len(masses_f), array('d', masses_f), array('d', xsec_t_2HDM_ref), 'LINEAR')
    spline_xsec_b_2HDM_ref = ROOT.RooSpline1D('gg%s_b_2HDM_xsec' % (P), '', w.var('m%s' % (P)), len(masses_f), array('d', masses_f), array('d', xsec_b_2HDM_ref), 'LINEAR')
    spline_xsec_i_2HDM_ref = ROOT.RooSpline1D('gg%s_i_2HDM_xsec' % (P), '', w.var('m%s' % (P)), len(masses_f), array('d', masses_f), array('d', xsec_i_2HDM_ref), 'LINEAR')
    w.imp(spline_xsec_t_2HDM_ref)
    w.imp(spline_xsec_b_2HDM_ref)
    w.imp(spline_xsec_i_2HDM_ref)

    w.factory('expr::gg%s_2HDM_xsec("@0+@1+@2", gg%s_t_2HDM_xsec, gg%s_b_2HDM_xsec, gg%s_i_2HDM_xsec)' % (P, P, P, P))

    w.factory('expr::gg%s_t_2HDM_frac("@0/@1", gg%s_t_2HDM_xsec, gg%s_2HDM_xsec)' % (P, P, P))
    w.factory('expr::gg%s_b_2HDM_frac("@0/@1", gg%s_b_2HDM_xsec, gg%s_2HDM_xsec)' % (P, P, P))
    w.factory('expr::gg%s_i_2HDM_frac("@0/@1", gg%s_i_2HDM_xsec, gg%s_2HDM_xsec)' % (P, P, P))


    w.factory('ref_alpha[%g]' % (pi / 4.))
    w.factory('ref_tanb_%s[%g]' % (P, float(T)))

    w.factory('expr::Yt_2HDM_%s(%s)' % (P, yt_expr[p]))
    w.factory('expr::Yb_2HDM_%s(%s)' % (P, yb_expr[p]))

    mA_vals = set()
    tanB_vals = set()
    lookup = {}
    with open('mhmodp_13000_higgs_%s.txt' % P) as scales_file:
        for line in scales_file:
            tanB, mA, ggh, bbh, mAA, Yt, Yb = line.split()
            mA_vals.add(float(mA))
            tanB_vals.add(float(tanB))
            lookup[(float(mA), float(tanB))] = (float(Yt), float(Yb))
    with open('mhmodp_13000_higgs_%s_highmA.txt' % P) as scales_file:
        for line in scales_file:
            tanB, mA, ggh, bbh, mAA, Yt, Yb = line.split()
            mA_vals.add(float(mA))
            tanB_vals.add(float(tanB))
            lookup[(float(mA), float(tanB))] = (float(Yt), float(Yb))
    mA_list = sorted(mA_vals)
    tanB_list = sorted(tanB_vals)

    hist_x = [90.5, 91.5, 92.5, 93.5, 94.5, 95.5, 96.5, 97.5, 98.5, 99.5, 100.5, 101.5, 102.5, 103.5, 104.5,
              105.5, 106.5, 107.5, 108.5, 109.5, 110.5, 111.5, 112.5, 113.5, 114.5, 115.5, 116.5, 117.5,
              118.5, 119.5, 120.5, 121.5, 122.5, 123.5, 124.5, 125.5, 126.5, 127.5, 128.5, 129.5, 130.5,
              131.5, 132.5, 133.5, 134.5, 135.5, 136.5, 137.5, 138.5, 139.5, 140.5, 141.5, 142.5, 143.5,
              144.5, 145.5, 146.5, 147.5, 148.5, 149.5, 150.5, 151.5, 152.5, 153.5, 154.5, 155.5, 156.5,
              157.5, 158.5, 159.5, 160.5, 161.5, 162.5, 163.5, 164.5, 165.5, 166.5, 167.5, 168.5, 169.5,
              170.5, 171.5, 172.5, 173.5, 174.5, 175.5, 176.5, 177.5, 178.5, 179.5, 180.5, 181.5, 182.5,
              183.5, 184.5, 185.5, 186.5, 187.5, 188.5, 189.5, 190.5, 191.5, 192.5, 193.5, 194.5, 195.5,
              196.5, 197.5, 198.5, 199.5, 200.5, 202.5, 207.5, 212.5, 217.5, 222.5, 227.5, 232.5, 237.5,
              242.5, 247.5, 252.5, 257.5, 262.5, 267.5, 272.5, 277.5, 282.5, 287.5, 292.5, 297.5, 302.5,
              307.5, 312.5, 317.5, 322.5, 323.5, 324.5, 325.5, 326.5, 327.5, 328.5, 329.5, 330.5, 331.5,
              332.5, 333.5, 334.5, 335.5, 336.5, 337.5, 338.5, 339.5, 340.5, 341.5, 342.5, 343.5, 344.5,
              345.5, 346.5, 347.5, 348.5, 349.5, 350.5, 351.5, 352.5, 353.5, 354.5, 355.5, 356.5, 357.5,
              358.5, 359.5, 360.5, 361.5, 362.5, 363.5, 364.5, 365.5, 366.5, 367.5, 368.5, 369.5, 370.5,
              372.5, 377.5, 382.5, 387.5, 392.5, 397.5, 402.5, 407.5, 412.5, 417.5, 422.5, 427.5, 432.5,
              437.5, 442.5, 447.5, 452.5, 457.5, 462.5, 467.5, 472.5, 477.5, 482.5, 487.5, 492.5, 497.5,
              502.5, 507.5, 512.5, 517.5, 522.5, 527.5, 532.5, 537.5, 542.5, 547.5, 552.5, 557.5, 562.5,
              567.5, 572.5, 577.5, 582.5, 587.5, 592.5, 597.5, 602.5, 607.5, 612.5, 617.5, 622.5, 627.5,
              632.5, 637.5, 642.5, 647.5, 652.5, 657.5, 662.5, 667.5, 672.5, 677.5, 682.5, 687.5, 692.5,
              697.5, 702.5, 707.5, 712.5, 717.5, 722.5, 727.5, 732.5, 737.5, 742.5, 747.5, 752.5, 757.5,
              762.5, 767.5, 772.5, 777.5, 782.5, 787.5, 792.5, 797.5, 802.5, 807.5, 812.5, 817.5, 822.5,
              827.5, 832.5, 837.5, 842.5, 847.5, 852.5, 857.5, 862.5, 867.5, 872.5, 877.5, 882.5, 887.5,
              892.5, 897.5, 902.5, 907.5, 912.5, 917.5, 922.5, 927.5, 932.5, 937.5, 942.5, 947.5, 952.5,
              957.5, 962.5, 967.5, 972.5, 977.5, 982.5, 987.5, 992.5, 997.5, 1002.5, 1025, 1075, 1125,
              1175, 1225, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875,
              1925, 1975, 2025]
    hist_y = [0.45, 0.55, 0.65, 0.75, 0.85, 0.95, 1.05, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
              10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5,
              24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5,
              39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5, 50.5, 51.5, 52.5, 53.5,
              54.5, 55.5, 56.5, 57.5, 58.5, 59.5, 60.5]
    hYt = ROOT.TH2F('Yt', 'Yt', len(hist_x) - 1, array('d', hist_x), len(hist_y) - 1, array('d', hist_y))
    hYb = ROOT.TH2F('Yb', 'Yb', len(hist_x) - 1, array('d', hist_x), len(hist_y) - 1, array('d', hist_y))
    for x in xrange(1, hYt.GetNbinsX() + 1):
        for y in xrange(1, hYt.GetNbinsY() + 1):
            xc = hYt.GetXaxis().GetBinCenter(x)
            yc = hYt.GetYaxis().GetBinCenter(y)
            xl = takeClosest(mA_list, xc)
            yl = takeClosest(tanB_list, yc)
            hYt.SetBinContent(x, y, lookup[(xl, yl)][0])
            hYb.SetBinContent(x, y, lookup[(xl, yl)][1])
            # print '%f,%f --> %f,%f = %s' % (xc, yc, xl, yl, lookup[(xl, yl)])

    wsptools.SafeWrapHist(w, ['mA', 'tanb'], hYt, name='Yt_MSSM_%s' % P)
    wsptools.SafeWrapHist(w, ['mA', 'tanb'], hYb, name='Yb_MSSM_%s' % P)


    w.factory('expr::gg{P}_t_MSSM_xsec("@0*(@1*@1)/(@2*@2)",gg{P}_t_2HDM_xsec,Yt_MSSM_{P},Yt_2HDM_{P})'.format(P=P))
    w.factory('expr::gg{P}_b_MSSM_xsec("@0*(@1*@1)/(@2*@2)",gg{P}_b_2HDM_xsec,Yb_MSSM_{P},Yb_2HDM_{P})'.format(P=P))
    w.factory('expr::gg{P}_i_MSSM_xsec("@0*(@1*@2)/(@3*@4)",gg{P}_i_2HDM_xsec,Yt_MSSM_{P},Yb_MSSM_{P},Yt_2HDM_{P},Yb_2HDM_{P})'.format(P=P))
    w.factory('expr::gg{P}_MSSM_xsec("@0+@1+@2", gg{P}_t_MSSM_xsec, gg{P}_b_MSSM_xsec, gg{P}_i_MSSM_xsec)'.format(P=P))

    w.factory('expr::gg{P}_t_MSSM_frac("@0/@1", gg{P}_t_MSSM_xsec, gg{P}_MSSM_xsec)'.format(P=P))
    w.factory('expr::gg{P}_b_MSSM_frac("@0/@1", gg{P}_b_MSSM_xsec, gg{P}_MSSM_xsec)'.format(P=P))
    w.factory('expr::gg{P}_i_MSSM_frac("@0/@1", gg{P}_i_MSSM_xsec, gg{P}_MSSM_xsec)'.format(P=P))


    dist = "pt_h1"
    use_dist = {
        's': {
            "400": "pt_h2",
            "450": "pt_h2",
            "500": "pt_h3",
            "600": "pt_h3",
            "700": "pt_h2",
            "800": "pt_h2",
            "900": "pt_h2",
            "1000": "pt_h2",
            "1200": "pt_h2",
            "1400": "pt_h2",
            "1500": "pt_h2",
            "1600": "pt_h2",
            "1800": "pt_h2",
            "2000": "pt_h2",
            "2300": "pt_h2",
            "2600": "pt_h2",
            "2900": "pt_h2",
            "3200": "pt_h2"
        },
        'A': {},
        'H': {}
    }

    for m in masses:
        # We might need to use wider binned distributions for some mass points
        d = dist
        if m in use_dist[p]:
            d = use_dist[p][m]

        wsptools.SafeWrapHist(w, ['h_pt'],
            GetNormed('output_%s_%s_%s.root:analysis/%s/pythia' % (p, m, T, d)), name='%s_%s_pythia' % (P, m))

        wsptools.SafeWrapHist(w, ['h_pt'],
            GetNormed('output_%s_%s_%s.root:analysis/%s/t_t' % (p, m, T, d)), name='%s_%s_t' % (P, m))

        wsptools.SafeWrapHist(w, ['h_pt'],
            GetNormed('output_%s_%s_%s.root:analysis/%s/b_b' % (p, m, T, d)), name='%s_%s_b' % (P, m))

        wsptools.SafeWrapHist(w, ['h_pt'],
            GetNormed('output_%s_%s_%s.root:analysis/%s/int' % (p, m, T, d)), name='%s_%s_i' % (P, m))

        wsptools.SafeWrapHist(w, ['h_pt'],
            GetNormed('output_%s_%s_%s.root:analysis/%s/tot' % (p, m, T, d)), name='%s_%s_f' % (P, m))

        w.factory('expr::{P}_{m}_t_ratio("@0/@1", {P}_{m}_t, {P}_{m}_pythia)'.format(P=P, m=m))
        w.factory('expr::{P}_{m}_b_ratio("@0/@1", {P}_{m}_b, {P}_{m}_pythia)'.format(P=P, m=m))
        w.factory('expr::{P}_{m}_i_ratio("@0/@1", {P}_{m}_i, {P}_{m}_pythia)'.format(P=P, m=m))
        w.factory('expr::{P}_{m}_f_ratio("@0/@1", {P}_{m}_f, {P}_{m}_pythia)'.format(P=P, m=m))
        w.factory('expr::{P}_{m}_2HDM_ratio("@0*@1+@2*@3+@4*@5", gg{P}_t_2HDM_frac, {P}_{m}_t_ratio, gg{P}_b_2HDM_frac, {P}_{m}_b_ratio, gg{P}_i_2HDM_frac, {P}_{m}_i_ratio)'.format(P=P, m=m))
        w.factory('expr::{P}_{m}_MSSM_ratio("@0*@1+@2*@3+@4*@5", gg{P}_t_MSSM_frac, {P}_{m}_t_ratio, gg{P}_b_MSSM_frac, {P}_{m}_b_ratio, gg{P}_i_MSSM_frac, {P}_{m}_i_ratio)'.format(P=P, m=m))



w.importClassCode('RooSpline1D')

w.Print()
w.writeToFile('mssm_hpt_weights.root')
w.Delete()
